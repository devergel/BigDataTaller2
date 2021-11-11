import os
import pymongo
import json
from pymongo import MongoClient
from newsapi import NewsApiClient
from datetime import datetime, timedelta

mongod_connect = os.environ['MONGOD_CONNECT']

client = MongoClient(mongod_connect)
db = client['bigdata02']
news_collection = db['news']
# Init
newsapi = NewsApiClient(api_key=os.environ['NEWSAPI'])
to_date = news_collection.find_one(sort=[("publishedAt", 1)])["publishedAt"]
date_time_obj = datetime.fromisoformat(to_date[:-1])
date_time_obj = date_time_obj - timedelta(days=1)
to_date = date_time_obj.strftime("%Y-%m-%d")
print(to_date)
for x in range(5):
    all_articles = newsapi.get_everything(q='colombia', language='es', sort_by='publishedAt', to=to_date, page=x+1)
    news_collection.insert_many(all_articles['articles'])

#with open('data2.json', 'w', encoding='utf-8') as f:
#    json.dump(all_articles['articles'] , f, ensure_ascii=False, indent=4)




