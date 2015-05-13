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

class dnaindia(CrawlSpider):
    name = "dnaindia"
    allowed_domains = ["dnaindia.com"]
    start_urls = [
	"http://www.dnaindia.com/",
    "http://www.dnaindia.com/india",
    "http://www.dnaindia.com/world",
    "http://www.dnaindia.com/sport",
    "http://www.dnaindia.com/scitech",
    "http://www.dnaindia.com/entertainment"
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
        
        
        x_article = response.xpath('//div[contains(@class, "content-story")]')
        
        #x_article_content = x_article.xpath('.//div[contains(@class, "artWarp")]/div[contains(@class, "fullCont1")]')
        list_article_content = x_article.xpath('.//p/text()').extract()
        article_content = ' '.join(list_article_content).encode('utf8')
        print article_content
        print "\n"
            
        #differentiating article page from other pages by its contents
        if article_content is not None and len(article_content) > 1:        
            print "entering"
            list_article_time = response.xpath('//div[contains(@class, "pubdate")]/text()').extract()
            print list_article_time
            article_time = ''.join(list_article_time)
            #article_time = article_time.encode('utf8')
                
            print str(parser.parse(article_time,fuzzy=True))
            print "\n"
            
            
            item = newsItem()
            item['title'] = response.xpath('//title/text()').extract()[0].encode('utf8')
            item['url'] = response.url
            item['crawled_site'] = "dnaindia"
            item['content'] = article_content
            item['tags'] = " "
            item['article_time'] = str(parser.parse(article_time))
            return item
            
      