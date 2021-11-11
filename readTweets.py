import os
import pymongo
from pymongo import MongoClient
import json
import tweepy
import twitter
from pprint import pprint
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

CONSUMER_KEY      = os.environ['CONSUMER_KEY']
CONSUMER_SECRET   = os.environ['CONSUMER_SECRET']
OAUTH_TOKEN       = os.environ['OAUTH_TOKEN']
OATH_TOKEN_SECRET = os.environ['OATH_TOKEN_SECRET']

mongod_connect = os.environ['MONGOD_CONNECT']

client = MongoClient(mongod_connect)
db = client['bigdata02']
tweet_collection = db['twits']

rest_auth = twitter.oauth.OAuth(OAUTH_TOKEN,OATH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
rest_api = twitter.Twitter(auth=rest_auth)

count = 100 #number of returned tweets, default and max is 100
geocode = "38.4392897,-78.9412224,50mi"  # defin the location, in Harrisonburg, VA
q = "@UCDemocratico"                               #@UCDemocratico  @AlvaroUribeVel Matarife define the keywords, tweets contain election

since_id_new = -1
since_id_old = 0
while(since_id_new != since_id_old):
    since_id_old = since_id_new
    try:
        search_results = rest_api.search.tweets(count=count,q=q)
        statuses = search_results["statuses"]
        since_id_new = statuses[-1]['id']
    
        for statuse in statuses:
            try:
                tweet_collection.insert_one(statuse)
                pprint(statuse['created_at']) # print the date of the collected tweets
            except:
               pass
    except:
        since_id_new = since_id_old

q = "@AlvaroUribeVel"                               #@UCDemocratico  @AlvaroUribeVel Matarife define the keywords, tweets contain election

since_id_new = -1
since_id_old = 0
while(since_id_new != since_id_old):
    since_id_old = since_id_new
    try:
        search_results = rest_api.search.tweets(count=count,q=q)
        statuses = search_results["statuses"]
        since_id_new = statuses[-1]['id']
    
        for statuse in statuses:
            try:
                tweet_collection.insert_one(statuse)
                pprint(statuse['created_at']) # print the date of the collected tweets
            except:
               pass
    except:
        since_id_new = since_id_old

q = "Matarife"                               #@UCDemocratico  @AlvaroUribeVel Matarife define the keywords, tweets contain election

since_id_new = -1
since_id_old = 0
while(since_id_new != since_id_old):
    since_id_old = since_id_new
    try:
        search_results = rest_api.search.tweets(count=count,q=q)
        statuses = search_results["statuses"]
        since_id_new = statuses[-1]['id']
    
        for statuse in statuses:
            try:
                tweet_collection.insert_one(statuse)
                pprint(statuse['created_at']) # print the date of the collected tweets
            except:
               pass
    except:
        since_id_new = since_id_old
