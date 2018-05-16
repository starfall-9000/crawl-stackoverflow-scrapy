# -*- coding: utf-8 -*-
import scrapy
import json
import pdb

from beat.items import BeatItem

def get_start_urls():
    listIndex = [i*5 for i in range(10)]    # [0, 5, ... , 45]
    format_url = 'http://api.beat.vn/api/post/api_get_posts_by_slug/nong/{0}/5?device_id=pc&token='
    start_urls = [format_url.format(index) for index in listIndex]
    return start_urls

class GetPostsBySlugSpider(scrapy.Spider):
    name = 'get_posts_by_slug'
    allowed_domains = ['api.beat.vn']
    start_urls = get_start_urls()

    def parse(self, response):
        print("Process.." + response.url)
        body = json.loads(response.body)
        data = body['data']
        
        for d in data:
            item = self.parse_beat_item(d)
            yield item
    
    def parse_beat_item(self, data):
        item = BeatItem()
        item['content'] = data['content']
        item['publishdate'] = data['publishdate']
        item['title'] = data['title']
        
        return item
