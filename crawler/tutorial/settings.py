# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
#DUPEFILTER_CLASS = 'tutorial.pipelines.CustomFilter'
ITEM_PIPELINES = {
    'tutorial.pipelines.dataProcessing' : 300,
    'tutorial.pipelines.urlProcessing' : 400,
    'tutorial.pipelines.NOSQLDBInsertion': 500 
}
HTTP_PROXY = 'http://127.0.0.1:8123'

#database credentials
DB_HOST = "YYYY"
DB_USERNAME = "cyno"
DB_PASSWORD = "XXXX"
DB_NAME = "myDB"


#mongodb credentials
MONGO_URL = "mongodb://localhost:27017/"
MONGODB_NAME = "WhyThisTrend"
MONGODB_COLLECTION_NAME = "article"

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
	'tutorial.random_user_agent.RotateUserAgentMiddleware' : 400,
#	'tutorial.proxy_setting.ProxyMiddleware' : 410,
	'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware' : 420
}
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
DOWNLOAD_DELAY = 1
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
