# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:32:13 2021

@author: hp
"""
import scrapy
from scrapy.loader import ItemLoader
from kdpcr_crawler.items import Tax_Advisor

class TaxSpider(scrapy.Spider):
    name = "TaxSpider"
    allowed_domains = ["www.kdpcr.cz"]
    start_urls = (
        "https://www.kdpcr.cz/seznam-danovych-poradcu?count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=500&count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=1000&count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=1500&count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=2000&count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=2500&count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=3000&count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=3500&count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=4000&count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=4500&count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=5000&count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=5500&count=500",
        "https://www.kdpcr.cz/seznam-danovych-poradcu?from=6000&count=500"
        
    )

    def parse(self, response):
        urls = response.xpath("//div[@class='consultants_list_data']//div[@class='item']//a[@class='image']/@href").extract()
        urls=['www.kdpcr.cz'+x for x in urls]
        
        #print("urls is", urls)
        # for url in urls:
        #     request = scrapy.Request(url, callback=self.tax_advisor_page)
        #     yield request        
                
        for ta in response.xpath("//div[@class='consultants_list_data']//div[@class='item']"):
            item = Tax_Advisor()
            item['name']= ta.xpath("./h2/a/span/text()").get()
            item['location']=ta.xpath("./div[@class='infos']/div[@class='inside']/div[@class='place']/text()").get()
            item['location']=item['location'] and item['location'].replace('\r', '').replace('\t', '').replace('\n', '')
            item['phone_number']=ta.xpath("./div[@class='infos']/div[@class='inside']/div[@class='phone']/text()").get()
            item['phone_number']=item['phone_number'] and item['phone_number'].replace('\r', '').replace('\t', '').replace('\n', '')

            item['email_address']=ta.xpath("./div[@class='infos']/div[@class='inside']/div[@class='email']/a/text()").get()
            print(item)
            yield item

        
    def tax_advisor_page(self, response):
        pass
        
        