# -*- coding: utf-8 -*-
import scrapy
from crawl_bbc_news.items import CrawlBbcNewsItem
import re


# Eventhose bbc have many kind of content (video, weather, ...)
#  this spider does only care for the news ones and ignore all the rest
class BbcSpider(scrapy.Spider):
    name = 'bbc'
    allowed_domains = ['bbc.com']

    start_urls = ['http://bbc.com/news']

    # Parse the request get the major content and next link
    # The result (item), will be pass through to 2 pipeline 
    # - CleansingPipeline: to clean up html
    # - MongoPipeline: save to Mongo database
    def parse(self, response):

		# Parsing the response and store in the item object
		title = response.xpath('(//h1)[1]/text()').extract_first()
	        if title and (not title.isspace()):
	            mini_info = response.css('ul.mini-info-list');
	            article_date = mini_info.xpath("(./li)[1]/div/text()").extract_first() 
	            article_category = mini_info.xpath("(./li)[2]/a/text()").extract_first() 
	            if article_category and not article_category.isspace():
	                article_body = response.css("div.story-body__inner")    
	                introduction = article_body.css("p.story-body__introduction::text").extract_first()
	                body_content = article_body.extract_first()
	                if article_body and introduction and body_content:
		                yield CrawlBbcNewsItem(
							title= title, 
							url= response.url, 
							article_date= article_date, 
							category= article_category, 
		                    introduction= introduction,
		                    content_html= body_content,
		                    content_text = ""                    	
		                )
		 
		 # Parsing all the a tag for the next requests               
		for url in response.xpath('//a/@href').extract():
			url = response.urljoin(url)
			if len(url) < 100:
				if re.search(".*bbc.com/news.*", url) and not (re.search(".*search.*keyword.*", url)):
					yield scrapy.Request(url, callback=self.parse)