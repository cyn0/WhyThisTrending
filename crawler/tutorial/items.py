# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuoraItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    followers = scrapy.Field()
    upvotes = scrapy.Field()
    topic = scrapy.Field()
    pass

class CommonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    topics = scrapy.Field()
    tags = scrapy.Field()
    docDate = scrapy.Field()
    imgUrl = scrapy.Field()
    source = scrapy.Field()
    sourceUrl = scrapy.Field()
    pass

class newsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    tags = scrapy.Field()
    article_time = scrapy.Field()
    crawled_site = scrapy.Field()
    content = scrapy.Field()
    pass
