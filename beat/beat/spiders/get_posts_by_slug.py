# -*- coding: utf-8 -*-
import scrapy
import pdb


class GetPostsBySlugSpider(scrapy.Spider):
    name = 'get_posts_by_slug'
    allowed_domains = ['api.beat.vn']
    start_urls = ['http://api.beat.vn/api/post/api_get_posts_by_slug/nong/0/5?device_id=pc&token=']

    def parse(self, response):
        print("Process.." + response.url)
        pdb.set_trace()
        pass
