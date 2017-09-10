
# Notes: this file is the guide line for all major commands needed to setup/run this project
# 	Please don't run the whole file in bash. It won't work

# =========== Install packages ===========

# -0- Install python3.6 
#	Package can be downloaded from https://www.python.org/downloads/

# -1- Crawling framework
	pip3.6 install --user scrapy
	#	OR  
	sudo python3.6 -m pip3.6 install scrapy

# -2- mongodb driver for python
	sudo python3.6 -m pip3.6 install pymongo

# -3- python web framework for building RESFul web services
	sudo python3.6 -m pip3.6 install --user bottle

# -4- BeautifulSoup
	sudo python3.6 -m pip3.6 install --user beautifulsoup4

# =========== setup mongodb database =========== 

# For simplicity of demo purpose, this database allow anonymous access. 
# If you want setup db authentication, need to update the settings.py #MONGO_URI

# -1-  start mongo daemon
mongod &

# -2-  create database, collection and index
mongo

# ... and in the mongodb shell, run these command to create database, collection and indexes
use bbc
db.createCollection("article")

db.article.createIndex( { url: 1 } )
db.article.createIndex( { category: 1 } )
db.article.createIndex( { article_date: 1 } )

# Verify the indexes created correctly
db.article.getIndexes()

# =========== start up processes =========== 

# -0-  start mongd
mongod &

# -1-  start crawling
scrapy crawl bbc &

# -2-  start web service 
python 3.6 bbc_ws.py &
