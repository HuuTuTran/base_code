# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectNameItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class author(scrapy.Item):
    name = scrapy.Field()
    born_date = scrapy.Field()
    born_location = scrapy.Field()
    description = scrapy.Field()

