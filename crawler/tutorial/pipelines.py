# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import json
import sys; sys.path.append("/usr/local/lib/python2.7/site-packages")
import MySQLdb
from pymongo import MongoClient
from scrapy import signals
from scrapy.exceptions import DropItem
import os
import re
from scrapy.dupefilter import RFPDupeFilter
from scrapy.utils.request import request_fingerprint

from scrapy.conf import settings

"""
class CustomFilter(RFPDupeFilter):
    def __getid(self, url):
        mm = url.split("&refer")[0] #or something like that
        return mm

    def request_seen(self, request):
        fp = self.__getid(request.url)
        #if fp in self.fingerprints:
        #print "duplicate " +request.url
            #return True
        self.fingerprints.add(fp)
        if self.file:
            if "http://techcrunch.com/" in request.url:
                #print "techcrunch page visited"
                if "http://techcrunch.com/2014" in request.url:
                        self.file.write(fp + os.linesep)            
                else:
                        return
                self.file.write(fp + os.linesep)

"""
#class DuplicatesPipeline(object):

#    def __init__(self):
#        self.ids_seen = set()

#    def process_item(self, item, spider):
#        if item['link'] in self.ids_seen:
#       print "duplicates"
#            raise DropItem("Duplicate item found: %s" % item)
#        else:
#            self.ids_seen.add(item['link'])
#            return item


class dataProcessing(object):
    def __init__(self):
            pass
            
    def process_item(self, item, spider):
            if spider.name not in ['thehindu', 'firstpost', 'dnaindia', 'indiatoday', 'theguardian']:
                    return item
                    
            #for now, fixing single and double quotes problem by removing them :/
            item['title'] = str(item['title']).translate(None,"'\"")
            item['content'] = str(item['content']).translate(None,"'\"")
            print "^^" * 30
            print item['content']
            return item
            
            
class urlProcessing(object):
    def __init__(self):
            pass
            
    def process_item(self, item, spider):
            if spider.name not in ['thehindu']:
                    return item
                    
            #removing unwanted values (url params)
            print item
            if str(item['crawled_site']) is "thehindu":
                url = item['url']
                item['url'] = url[:url.index(".ece") + 4]
            
            return item

            
class SQLDBInsertion(object):
    def __init__(self):
            self.db = MySQLdb.connect(settings.get('DB_HOST'),settings.get('DB_USERNAME'),settings.get('DB_PASSWORD'),settings.get('DB_NAME') ) 
            # prepare a cursor object using cursor() method
            self.cursor = self.db.cursor()
            pass
            
    def process_item(self, item, spider):
            if spider.name not in ['thehindu', 'firstpost', 'dnaindia', 'indiatoday1']:
                    return item 
            print "*"*50
            print item['title']
            print item['url']
            print item['crawled_site']
            print item['content']
            print item['tags']
            print item['article_time'] 
            print "*"*50            
            #sql = "INSERT INTO NEWS(TITLE, URL, CONTENT, CRAWLED_SITE,ARTICLE_TIME, TAGS) VALUES('" + item['title'] +"', '" + item['url'] + "', '" + item['content'] + "','" + item['crawled_site'] + "', '" + item['article_time'] + "', '" + item['tags'] + "')"
            sql = "INSERT INTO NEWS(TITLE, URL, CONTENT, CRAWLED_SITE, ARTICLE_TIME, TAGS) VALUES(%s,%s,%s,%s,%s,%s)"
            keys_values = (item['title'], item['url'], item['content'], item['crawled_site'], item['article_time'], item['tags'])
            try:
                print sql
                self.cursor.execute(sql, keys_values)
                self.db.commit()
            except Exception as e:
                print "_____exception____"  
                print e
                self.db.rollback()
            return item
    def close_spider(self,spider):
        pass

class NOSQLDBInsertion(object):
    def __init__(self):
            client = MongoClient(settings.get('MONGO_URL'))
            db = client[settings.get('MONGODB_NAME')]
            self.collection = db[settings.get('MONGODB_COLLECTION_NAME')]
            pass
            
    def process_item(self, item, spider):
            print "*"*50
            print item['title']
            print item['url']
            print item['crawled_site']
            print item['content']
            print item['tags']
            print item['article_time'] 
            print "*"*50          
            document = {
                'title' : item['title'],
                'url': item['url'],
                'crawled_site' : item['crawled_site'],
                'content' : item['content'],
                'tags' : item['tags'],
                'article_time' : item['article_time']
            }
            self.collection.insert_one(document)
            return item
    def close_spider(self,spider):
        pass