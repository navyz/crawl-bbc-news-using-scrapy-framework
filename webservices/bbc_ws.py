#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from bottle import route, request

# TODO: create a configuration for this
# TODO2: create connection pool for mongodb
mongodb_uri = "mongodb://bbc:password1@aws-ap-southeast-1-portal.2.dblayer.com:15987/bbc?ssl=true&ssl_ca_certs=key.pk" 


# Get a list of all article category
#   ex: http://localhost:8080/category/list
@route('/category/list/', method='GET')
def get_list_category():
	client = MongoClient(mongodb_uri)
	db = client.bbc
	collection = db.article
	doc = collection.distinct("category")
	return dumps(doc)

# Get a list of all article by provided category
#   ex: http://localhost:8080/article/list/category/Asia
@route('/article/list/category/<category>', method='GET')
def get_list_articles_by_category(category):
	client = MongoClient(mongodb_uri)
	db = client.bbc
	collection = db.article
	doc = collection.find({"category": category}, {"_id": 1, "status": 1, "category": 1, "title": 1, "date": 1})
	return dumps(doc)

# Get a list of all article on a given date
# The date must be formated as ddMMMyyyy
# 	ex: http://host:port/article/list/date/5 September 2017
@route('/article/list/date/<article_date>', method='GET')
def get_list_articles_by_date(article_date):
	print(article_date)
	client = MongoClient(mongodb_uri)
	db = client.bbc
	collection = db.article
	doc = collection.find({"date": article_date}, {"_id": 1, "status": 1, "category": 1, "title": 1, "date": 1})
	return dumps(doc)

# Get the article detail by id. A JSON object will be returned
# 	ex: http://127.0.0.1:8080/article/detail/id/59b4a29d96375385bf26cdc0
@route('/article/detail/id/<id>', method='GET')
def get_article_by_id(id):
	client = MongoClient(mongodb_uri)
	db = client.bbc
	collection = db.article
	doc = collection.find({"_id": ObjectId(id)})
	return dumps(doc)

# Get the article content in text-only format
# 	ex: http://127.0.0.1:8080/article/text/id/59b4a29d96375385bf26cdc0
@route('/article/text/id/<id>', method='GET')
def get_article_text_by_id(id):
	client = MongoClient(mongodb_uri)
	db = client.bbc
	collection = db.article
	doc = collection.find_one({"_id": ObjectId(id)}, {"content_text": 1})
	if doc:
		return doc["content_text"]
	else:
		return "Article not found"

# Get the article content in html format
# 	ex: http://127.0.0.1:8080/article/html/id/59b4a29d96375385bf26cdc0
@route('/article/html/id/<id>', method='GET')
def get_article_html_by_id(id):
	client = MongoClient(mongodb_uri)
	db = client.bbc
	collection = db.article
	doc = collection.find_one({"_id": ObjectId(id)}, {"content_html": 1})
	print (doc)
	if doc and len(doc) > 0:
		return doc["content_html"]
	else:
		return "Article not found"

import bottle
application = bottle.default_app()
from paste import httpserver
httpserver.serve(application, host='0.0.0.0', port=8080)


