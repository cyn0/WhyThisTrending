import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from tutorial.items import newsItem
from CalaisTopicClassifier import TopicClassifier

from dateutil import parser
# scrapy crawl quora -s DEPTH_LIMIT=1 -s LOG_FILE=newscrapy.log
# scrapy crawl gen_spider -s DEPTH_LIMIT=1 -s LOG_FILE=newscrapy.log -s JOBDIR=crawls/tech-1

class hindustantimes(CrawlSpider):
    name = "hindustantimes"
    allowed_domains = ["hindustantimes.com"]
    start_urls = [
	"http://www.hindustantimes.com/",
    #"http://www.thehindu.com/business/",
    #"http://www.thehindu.com/sport/",
    #"http://www.thehindu.com/sci-tech/",
    #"http://www.thehindu.com/entertainment/"
	
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
        if "h" in url:
            print "entering"
            x_article = response.xpath('//div[contains(@class, "story_page_content_bg")]')
            
            x_article_content = x_article.xpath('.//section[contains(@class, "story_content")]/div[contains(@class, "sty_txt")]')
            list_article_content = x_article_content.xpath('.//p/text()').extract()
            article_content = ' '.join(list_article_content).encode('utf8')
            print article_content
            print "\n"
            
            list_article_time = x_article.xpath('.//div[contains(@class, "common_row")]/ul/li/text()').extract()
            article_time = ''.join(list_article_time)
            article_time = article_time.replace("Updated: ","").encode('utf8')
            print str(parser.parse(article_time))
            print "\n"
            
            list_article_keywords = x_article_content.xpath('.//div[contains(@class, "story_tag_smo")]/ul[contains(@class, "story_tags")]/li/text()').extract()
            article_keywords = ','.join(list_article_keywords)
            print article_keywords
            
            
            list_article_keywords = x_article.xpath('.//div[contains(@class, "story_tag_smo")]/ul/li/text()').extract()
            article_keywords = ','.join(list_article_keywords)
            print "ty", article_keywords
            
            
            item = newsItem()
            item['title'] = response.xpath('//title/text()').extract()[0].encode('utf8')
            item['url'] = response.url
            item['crawled_site'] = "hindustantimes"
            item['content'] = article_content
            item['tags'] = article_keywords
            item['article_time'] = str(parser.parse(article_time))
            return item
            
      