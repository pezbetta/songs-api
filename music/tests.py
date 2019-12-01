from django.test import TestCase
from django.conf import settings
from unittest import mock
import os

from music.utils import ArtistPicture


def mocked_requests_response(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        @property
        def ok(self):
            return self.status_code < 200

    return MockResponse(kwargs, 200)


class UtilsArtistPictureTestCase(TestCase):

    def test__encoded_name(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(ArtistPicture()._encoded_name('AC/DC'), 'AC%20DC')

    def test__prepare_request(self):
        dict_request = ArtistPicture()._prepare_request('AC/DC')
        self.assertListEqual(
            list(dict_request.keys()),
            ['request', 'spider_name']
        )
        self.assertEqual(
            dict_request.get('request').get('url'),
            'https://www.allmusic.com/search/artists/AC%20DC'
        )

    def test_recover(self):
        response_data = {'items': [{'name': 'AC/DC', 'url': 'http://url-to-image.jpg'}]}
        with mock.patch('requests.post', return_value=mocked_requests_response(response_data)) \
                as mock_method:
            ArtistPicture().recover('AC/DC')
        mock_method.assert_called_with(
            'http://scrapyrt:9080/crawl.json',
            json={'request': {'url': 'https://www.allmusic.com/search/artists/AC%20DC'},
                  'spider_name': 'artist_picture'}
        )

    @mock.patch('urllib.request.urlretrieve')
    def test_download(self, mock_method):
        return_value = ArtistPicture().download('AC/DC', 'http://url-to-image.jpg')
        mock_method.assert_called_once_with(
            'http://url-to-image.jpg',
            './images/AC%20DC.jpg'
        )
        self.assertEqual(return_value, os.path.join(settings.MEDIA_URL, 'AC%20DC.jpg'))
