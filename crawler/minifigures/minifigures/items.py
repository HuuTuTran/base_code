# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MinifiguresItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    SKU= scrapy.Field()
    tag	= scrapy.Field()
    price= scrapy.Field()
    img_url = scrapy.Field()
    cates = scrapy.Field()