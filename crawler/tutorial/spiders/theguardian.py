from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from tutorial.items import newsItem
import datetime
from dateutil import parser
import unicodedata

class theguardian(CrawlSpider):
    name = "theguardian"
    allowed_domains = ["theguardian.com"]
    start_urls = [
	"http://www.theguardian.com/",
    "http://www.theguardian.com/international",
    "http://www.theguardian.com/uk/technology"
    ]
    blacklists = [".*jsp","http://membership.theguardian.com/*","http://techcrunch.com/event.*",
	]
    rules = (Rule (SgmlLinkExtractor(deny=blacklists)
    , callback="parse_items", follow = True),
    )
#, follow= True


    def parse_article_time(self, url):
        words = url.split("/")
        print str(datetime.datetime.now().year)
        yearIndex = words.index(str(datetime.datetime.now().year))
        year = words[yearIndex]
        month = words[yearIndex + 1]
        date = words[yearIndex + 2]
        return str(parser.parse(year + " " + month + " "+ date))
     
    def parse_items(self, response):
        print "_"*60
        url = response.url
        print url
        
        if "/2015/" in url:
            print "entering"
            
            x_article_content = response.xpath('//div[contains(@class, "content__article-body")]')
            list_article_content = x_article_content.xpath('.//p/text()').extract()
            article_content = ' '.join(list_article_content).encode('utf8')           
            
            article_time = self.parse_article_time(url)

            list_article_keywords = response.xpath('.//ul[contains(@class, "keyword-list")]/li/a/text()').extract()
            article_keywords = ','.join(list_article_keywords).replace("\n","")

            item = newsItem()
            item['title'] = response.xpath('//title/text()').extract()[0].encode('utf8')
            item['url'] = response.url
            item['crawled_site'] = "theguardian"
            item['content'] = article_content
            item['tags'] = article_keywords
            item['article_time'] = article_time
            print item
            return item
            