import requests
from urllib.parse import quote
from urllib.request import urlretrieve
from os import path, makedirs


SCRAPYRT_URL = 'http://scrapyrt:9080/'
LOCALPATH = './images/'


class ArtistPicture:

    @staticmethod
    def _encoded_name(artist_name):
        return quote(artist_name.replace('/', ' '))

    def _prepare_request(self, artist_name):
        artist_name_encoded = self._encoded_name(artist_name)
        return {
            "request": {
                "url": "https://www.allmusic.com/search/artists/{}".format(artist_name_encoded)},
            "spider_name": "artist_picture"
        }

    def recover(self, artist_name):
        response = requests.post(
            SCRAPYRT_URL + 'crawl.json',
            json=self._prepare_request(artist_name)
        )
        if response.ok:
            try:
                return response.json().get('items')[0]
            except IndexError:
                return

    @staticmethod
    def _create_image_localpath():
        if not path.exists(LOCALPATH):
            makedirs(LOCALPATH)

    def download_image(self, artist_name):
        self._create_image_localpath()
        encoded_artist_name = self._encoded_name(artist_name)
        local_path = path.join(LOCALPATH, '{}.jpg'.format(encoded_artist_name))
        image_url = self.recover(artist_name).get('image_urls')[0]
        print(image_url)
        urlretrieve(image_url, local_path)
        return path.abspath(local_path)
