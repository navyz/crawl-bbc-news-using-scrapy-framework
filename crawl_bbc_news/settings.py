# -*- coding: utf-8 -*-

# Scrapy settings for crawl_bbc_news project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'crawl_bbc_news'

SPIDER_MODULES = ['crawl_bbc_news.spiders']
NEWSPIDER_MODULE = 'crawl_bbc_news.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

COOKIES_ENABLED = False

ITEM_PIPELINES = {
    'crawl_bbc_news.cleansing_pipeline.CleansingPipeline': 100,
    'crawl_bbc_news.mongo_pipeline.MongoPipeline': 200
}

MONGO_URI = "mongodb://localhost:27017"
MONGO_DATABASE = "bbc"

