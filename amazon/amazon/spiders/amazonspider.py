# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem


class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonspider'
    # allowed_domains = ['']
    start_urls = ['https://www.amazon.com/s?k=analog+synthesizer&ref=nb_sb_noss']

    def parse(self, response):

        items = AmazonItem()

        # product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_name = response.css('.s-line-clamp-4').css('::text').extract()
        product_price = response.css('.a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image').extract()
    
        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items