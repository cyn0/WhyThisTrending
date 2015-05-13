# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import json
import sys; sys.path.append("/usr/local/lib/python2.7/site-packages")
import MySQLdb
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

class QuoraPipeline(object):
    def __init__(self):
            self.db = MySQLdb.connect(settings.get('DB_HOST'),settings.get('DB_USERNAME'),settings.get('DB_PASSWORD'),settings.get('DB_NAME') ) 
            # prepare a cursor object using cursor() method
            self.cursor = self.db.cursor()
            pass
            
    def process_item(self, item, spider):
            if spider.name not in ['quora']:
                return item 
            title = " ".join(item['title'])
            title = title.replace("'","")
            topic = ",".join(item['topic']).encode('utf8')
            link = str(item['link']).encode('utf8')
            followers = " ".join(item['followers']).encode('utf8')
            upvotes =  ",".join(item['upvotes']).encode('utf8')
            sql = "INSERT INTO QUORA(TITLE,LINK, TOPICS, FOLLOWERS, UPVOTES) VALUES('" + title +"', '" +link+ "', '" +topic+ "','" + followers+ "', '" + upvotes + "')"
            print title
            print topic
            print link
            print followers
            print upvotes
            
            try:
                # Execute the SQL command
                self.cursor.execute(sql)
                # Commit your changes in the database
                self.db.commit()
            except Exception as e:
                # Rollback in case there is any error
                print "_____exception____"  
                print e
                self.db.rollback()
            return item
    def close_spider(self,spider):
        pass

class TechPipeline(object):
    def __init__(self):
            self.db = MySQLdb.connect(settings.get('DB_HOST'),settings.get('DB_USERNAME'),settings.get('DB_PASSWORD'),settings.get('DB_NAME') ) 
            # prepare a cursor object using cursor() method
            self.cursor = self.db.cursor()
            pass
            
    def process_item(self, item, spider):
            if spider.name not in ['gen_spider']:
                    return item 
            print "____________Techcrunch_________________"*20;
            #print title
            title = item['title'].encode('ascii','ignore')
            
            topic = ",".join(item['topics']).encode('utf-8')
            link = item['link']
            imgUrl = item['imgUrl']
            tag = ",".join(item['tags'])
            docDate = item['docDate']
            print docDate + "_______sql"
            crawlsite = "Techcrunch"
            sql = "INSERT INTO GENERAL(TITLE,LINK, TOPICS, TAGS,CRAWLEDSITE, IMGURL, DOCDATE) VALUES('" + title +"', '" +link+ "', '" +topic+ "','" + tag+ "','" + crawlsite + "', '" + imgUrl + "', '" + docDate + "')"
            
            try:
                # Execute the SQL command
                print sql
                self.cursor.execute(sql)
                # Commit your changes in the database
                self.db.commit()
            except Exception as e:
                print "_____exception____"  
                print e
                self.db.rollback()
            return item
    def close_spider(self,spider):
        pass




class MashablePipeline(object):
    def __init__(self):
            self.db = MySQLdb.connect(settings.get('DB_HOST'),settings.get('DB_USERNAME'),settings.get('DB_PASSWORD'),settings.get('DB_NAME') ) 
            # prepare a cursor object using cursor() method
            self.cursor = self.db.cursor()
            pass
            
    def process_item(self, item, spider):
            if spider.name not in ['mashable']:
                    return item 
            print "____________Mashable_________________"*20;
            title = item['title'].encode('ascii','ignore')
            
            topic = ",".join(item['topics']).encode('utf-8')
            link = item['link']
            imgUrl = item['imgUrl']
            tag = ",".join(item['tags'])
            docDate = item['docDate']
            print docDate + "_______sql"
            crawlsite = "Mashable"
            sql = "INSERT INTO GENERAL(TITLE,LINK, TOPICS, TAGS,CRAWLEDSITE, IMGURL, DOCDATE) VALUES('" + title +"', '" +link+ "', '" +topic+ "','" + tag+ "','" + crawlsite + "', '" + imgUrl + "', '" + docDate + "')"
            
            try:
                # Execute the SQL command
                print sql
                self.cursor.execute(sql)
                # Commit your changes in the database
                self.db.commit()
            except Exception as e:
                print "_____exception____"  
                print e
                self.db.rollback()
            return item
    def close_spider(self,spider):
        pass




class EngadgetPipeline(object):
    def __init__(self):
            self.db = MySQLdb.connect(settings.get('DB_HOST'),settings.get('DB_USERNAME'),settings.get('DB_PASSWORD'),settings.get('DB_NAME') ) 
            self.cursor = self.db.cursor()
            pass
            
    def process_item(self, item, spider):
            if spider.name not in ['engadget']:
                    return item 
            print "_____________________________________-Engadget____________________________"
            title = item['title'].encode('ascii','ignore')
            
            topic = ",".join(item['topics']).encode('utf-8')
            link = item['link']
            imgUrl = item['imgUrl']
            tag = ",".join(item['tags'])
            docDate = item['docDate']
            source = item['source']
            sourceUrl = item['sourceUrl']
            crawledsite = "Engadget"
            print docDate + "_______sql"
            sql = "INSERT INTO GENERAL(TITLE,LINK, TOPICS, TAGS,CRAWLEDSITE, SOURCE,SOURCELINK,IMGURL, DOCDATE) VALUES('" + title +"', '" +link+ "', '" +topic+ "','" + tag + "', '" + crawledsite+ "', '" + source + "', '" + sourceUrl +  "', '" + imgUrl + "', '" + docDate + "')"
            
            try:
                # Execute the SQL command
                print sql
                self.cursor.execute(sql)
                # Commit your changes in the database
                self.db.commit()
            except Exception as e:
                print "_____exception____"  
                print e
                self.db.rollback()
            return item
    def close_spider(self,spider):
        pass

"""
class gnewsPipeline(object):
    def __init__(self):
            self.db = MySQLdb.connect(settings.get('DB_HOST'),settings.get('DB_USERNAME'),settings.get('DB_PASSWORD'),settings.get('DB_NAME') ) 
            # prepare a cursor object using cursor() method
            self.cursor = self.db.cursor()
            pass
            
    def process_item(self, item, spider):
            if spider.name not in ['gnewsj']:
                return item 
            title = item['title'].encode('ascii','ignore')
            topic = ",".join(item['topics']).encode('utf-8')
            link = item['link']
            tag = ",".join(item['tags'])
            docDate = item['docDate']
            print docDate + "_______"
            sql = "INSERT INTO GNEWS(TITLE,LINK, TOPICS, TAGS,DOCDATE) VALUES('" + title +"', '" +link+ "', '" +topic+ "','" + tag+ "', '" + docDate + "')"
            
            try:
                print sql
                self.cursor.execute(sql)
                self.db.commit()
            except Exception as e:
                print "_____exception____"  
                print e
                self.db.rollback()
            return item
    def close_spider(self,spider):
        pass
"""

class dataProcessing(object):
    def __init__(self):
            pass
            
    def process_item(self, item, spider):
            if spider.name not in ['thehindu', 'firstpost', 'dnaindia', 'indiatoday']:
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

            
class dbInsertion(object):
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
