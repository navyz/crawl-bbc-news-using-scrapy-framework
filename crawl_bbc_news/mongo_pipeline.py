import pymongo
from pymongo import MongoClient
from crawl_bbc_news.items import CrawlBbcNewsItem

# Insert crawled data to MongoDB
class MongoPipeline(object):

    collection_name = 'article'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        combined_uri = crawler.settings.get('MONGO_URI') + "&ssl_ca_certs=" + crawler.settings.get('SSL_CA_FILE') 
        return cls(
            mongo_uri=combined_uri,
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        article_id = self.db[self.collection_name].insert_one(dict(item))
        return item