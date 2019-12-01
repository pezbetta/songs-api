# -*- coding: utf-8 -*-
import scrapy
from artist_picture.items import ArtistPictureItem


class ArtistsSpider(scrapy.Spider):
    name = 'artist_picture'
    allowed_domains = ['allmusic.com']
    start_urls = ['http://allmusic.com/']

    def __init__(self, search_artist_name='', **kwargs):
        self.search_artist_name = search_artist_name
        self.start_urls = ['https://www.allmusic.com/search/artists/{}'.format(search_artist_name)]
        super(ArtistsSpider, self).__init__(**kwargs)

    def parse(self, response):
        for artist in response.xpath('//div[has-class("results")]/ul/li')[:1]:
            artist_selector = artist.xpath('.//div[has-class("name")]/a')
            # 'artist_name': artist_selector.xpath('.//text()').get(),
            artist_info = response.follow(artist_selector.attrib['href'] + '/discography', self.parse_artist)
            yield artist_info

    def parse_artist(self, response):
        artist_name = response.css("h1.artist-name::text").get()
        if artist_name:
            artist_name = artist_name.strip()
        yield ArtistPictureItem(
            name=artist_name,
            image_urls=[response.css(".media-gallery-image::attr(src)").get()],
            # image_name=[self.search_artist_name]
        )
