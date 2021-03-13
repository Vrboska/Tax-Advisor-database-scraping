# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KdpcrCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Tax_Advisor(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    location = scrapy.Field()
    phone_number = scrapy.Field()
    email_address = scrapy.Field()