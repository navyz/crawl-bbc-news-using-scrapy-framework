# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

# Object contains all fields/data which need to be saved to MongoDB
class CrawlBbcNewsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    article_date = scrapy.Field()
    category = scrapy.Field()
    introduction = scrapy.Field()
    content_text = scrapy.Field()
    content_html = scrapy.Field()
