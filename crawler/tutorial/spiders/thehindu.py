import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from tutorial.items import newsItem
from dateutil import parser

class thehindu(CrawlSpider):
    name = "thehindu"
    allowed_domains = ["thehindu.com"]
    start_urls = [
	"http://www.thehindu.com/",
    "http://www.thehindu.com/business/",
    "http://www.thehindu.com/sport/",
    "http://www.thehindu.com/sci-tech/",
    "http://www.thehindu.com/entertainment/"
	"http://www.thehindu.com/news/",
    
    ]
    blacklists = [
	]
    rules = (Rule (SgmlLinkExtractor(deny=blacklists)
    , callback="parse_items", follow = True),
    )
#, follow= True



    def parse_items(self, response):
        print "_"*60
        url = response.url
        print url
        if ".ece" in url:
            print "entering"
            x_article = response.xpath('//div[contains(@id, "left-column")]')
            
            x_article_content = x_article.xpath('//div[contains(@class, "article-text")]')
            list_article_content = x_article_content.xpath('.//p[contains(@class,"body")]/text()').extract()
            article_content = ' '.join(list_article_content).encode('utf8')
            print article_content
            print "\n"
            
            list_article_time = x_article.xpath('.//div[contains(@class, "artPubUpdate")]/text()').extract()
            article_time = ''.join(list_article_time)
            article_time = article_time.replace("Updated: ","").encode('utf8')
            print str(parser.parse(article_time))
            print "\n"
            
            list_article_keywords = x_article.xpath('.//div[contains(@id, "articleKeywords")]/p/a/text()').extract()
            article_keywords = ','.join(list_article_keywords)
            print article_keywords
            
            item = newsItem()
            item['title'] = response.xpath('//title/text()').extract()[0].encode('utf8')
            item['url'] = response.url
            item['crawled_site'] = "thehindu"
            item['content'] = article_content
            item['tags'] = article_keywords
            item['article_time'] = str(parser.parse(article_time))
            return item