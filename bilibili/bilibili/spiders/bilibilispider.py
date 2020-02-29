# -*- coding: utf-8 -*-
import scrapy


class BilibilispiderSpider(scrapy.Spider):
    name = 'bilibilispider'
    allowed_domains = ['bilibili.com']
    start_urls = ['http://bilibili.com/']

    def parse(self, response):
        pass
