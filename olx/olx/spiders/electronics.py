# -*- coding: utf-8 -*-
import scrapy


class ElectronicsSpider(scrapy.Spider):
    name = 'electronics'
    allowed_domains = ['www.olx.com.pk']
    start_urls = ['http://www.olx.com.pk/']

    def parse(self, response):
        pass
