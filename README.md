# CRAWL BBC NEWS USING SCRAPY FRAMEWORK

>This project use scrapy python framework to crawl the news data from http://www.bbc.com page, save to mongodb and expose as RESTFul web services.


## Objectives

- The application will crawl the news on www.bbc.com using the scrapy crawler framework (http://scrapy.org/) 
- The appliction use BetifulSoup module to cleanse the articles to obtain only information relevant to the news story, e.g. article text, author, headline, article url.  
- Store the data in a hosted mongo database, e.g. compose.io/mongo, for subsequent search and retrieval.  Ensure the URL of the article is included to enable comparison to the original.
- Write an API that provides access to the content in the mongo database.  The user should be able to search for articles by keyword


## Tools/software used
- Python scrapy framework: crawl and extract data from html response
- BetifulSoup: re-format the html, remove dummy data and extract meaningful text from the article.
- MongoDB: for storing the captured data
- Python Bottle: expose RESTFul web serves to server the stored data.

## Setup

Some command lines which are used to setup environment as well as execute the scripts

### Install packages 

0. Install python3.6
	Package can be downloaded from https://www.python.org/downloads/

1. Crawling framework

`	pip3.6 install --user scrapy  `

OR  

`	sudo python3.6 -m pip3.6 install scrapy	`

2. mongodb driver for python

`	sudo python3.6 -m pip3.6 install pymongo	`

3. python web framework for building RESFul web services

`	sudo python3.6 -m pip3.6 install --user bottle 	`

4. beautifulsoup4

`	sudo python3.6 -m pip3.6 install --user beautifulsoup4	`

### Setup mongodb database 

> For simplicity of demo purpose, this database allow anonymous access. If you want setup db authentication, need to update the settings.py #MONGO_URI

1.  start mongo daemon

`	mongod &	`

2.  create database, collection and index

`	mongo 	`

> ... and in the mongodb shell, run these command to create database, collection and `
indexes

```
use bbc
db.createCollection("article")

db.article.createIndex( { url: 1 } )
db.article.createIndex( { category: 1 } )
db.article.createIndex( { article_date: 1 } )
```

> Verify the indexes created correctly

`	db.article.getIndexes()	`

### start up processes 

1.  start mongd

` mongod & `

2.  start crawling

` scrapy crawl bbc & `

3.  start web service

` python 3.6 bbc_ws.py & `

## TODO

1. Use hosted mongo database instead of local one
2. Let spider run as daemon and incremential crawl
3. Improve the function to clean up the html/text
4. Crawl more information from the page beside news.
