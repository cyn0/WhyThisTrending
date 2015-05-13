import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from tutorial.items import newsItem
from CalaisTopicClassifier import TopicClassifier

from dateutil import parser
import unicodedata
# scrapy crawl quora -s DEPTH_LIMIT=1 -s LOG_FILE=newscrapy.log
# scrapy crawl gen_spider -s DEPTH_LIMIT=1 -s LOG_FILE=newscrapy.log -s JOBDIR=crawls/tech-1

class indiatoday(CrawlSpider):
    name = "indiatoday"
    allowed_domains = ["indiatoday.intoday.in"]
    start_urls = [
	"http://indiatoday.intoday.in/" ,
    "http://indiatoday.intoday.in/section/113/1/world.html",
    "http://indiatoday.intoday.in/technology/",
    "http://indiatoday.intoday.in/section/214/1/cricket.html",
    "http://indiatoday.intoday.in/section/84/1/sports.html"
    
    ]
    blacklists = ['http://techcrunch.com/contact/',"http://techcrunch.com/author/*","http://techcrunch.com/topic/.*","http://techcrunch.com/video/","http://techcrunch.com/event.*",
	
	]
    rules = (Rule (SgmlLinkExtractor(deny=blacklists)
    , callback="parse_items", follow = True),
    )
#, follow= True



    def parse_items(self, response):
        print "_"*60
        url = response.url
        print url
        
        if "/story/" in url:
            print "entering"
            x_article = response.xpath('//div[contains(@class, "strleft")]')
            
            x_article_content = x_article.xpath('//div[contains(@class, "mediumcontent")]')
            list_article_content = x_article_content.xpath('.//p/text()').extract()
            article_content = ' '.join(list_article_content).encode('utf8')
            print article_content
            print "\n"
            
            list_article_time = x_article.xpath('.//div[contains(@class, "strstrap")]/text()').extract()
            article_time = ''.join(list_article_time)
            print list_article_time
            article_time = article_time[1] #.encode('utf8')
            
            #removing unwanted unicode
            article_time = unicodedata.normalize('NFKD', article_time).encode('ascii', 'ignore')
            article_time = article_time.replace("\r\n","")
            article_time = article_time[article_time.index(", ") + 2 :].replace(" | UPDATED")
            print article_time
            print str(parser.parse(article_time))
            print "\n"
            
            item = newsItem()
            item['title'] = response.xpath('//title/text()').extract()[0].encode('utf8')
            item['url'] = response.url
            item['crawled_site'] = "indiatoday"
            item['content'] = article_content
            item['tags'] = " "
            item['article_time'] = str(parser.parse(article_time))
            return item