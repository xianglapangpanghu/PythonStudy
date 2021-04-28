# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LywProjectItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    put_time = scrapy.Field()
    content = scrapy.Field()
    origin = scrapy.Field() #网页原始url
