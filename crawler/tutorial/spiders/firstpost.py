import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from tutorial.items import newsItem
from dateutil import parser

class firstpost(CrawlSpider):
    name = "firstpost"
    allowed_domains = ["firstpost.com"]
    start_urls = [
	"http://www.firstpost.com/",
    "http://www.firstpost.com/category/politics",
    "http://www.firstpost.com/category/india",
    "http://www.firstpost.com/category/world",
    "http://www.firstpost.com/category/business",
    "http://www.firstpost.com/category/living",
    "http://www.firstpost.com/category/bollywood",
    "http://tech.firstpost.com/"
	
    ]
    blacklists = ['http://www.fakingnews.firstpost.com/*'
	]
    rules = (Rule (SgmlLinkExtractor(deny=blacklists)
    , callback="parse_items", follow = True),
    )
#, follow= True



    def parse_items(self, response):
        print "_"*60
        url = response.url
        print url
        
        x_article = response.xpath('//section[contains(@class, "col_left")]')
        
        x_article_content = x_article.xpath('.//div[contains(@class, "artWarp")]/div[contains(@class, "fullCont1")]')
        list_article_content = x_article_content.xpath('.//p/text()').extract()
        article_content = ' '.join(list_article_content).encode('utf8')
        print article_content
        print "\n"
        
        #differentiating article page from other pages by its contents
        if article_content is not None and len(article_content) > 1:
            list_article_time = x_article.xpath('.//div[contains(@class, "artTps")]/div[contains(@class, "lCont")]/text()').extract()
            print list_article_time
            if len(list_article_time) > 0:
                article_time = ''.join(list_article_time)
                article_time = article_time.encode('utf8')
            else:
                list_article_time = x_article.xpath('.//div[contains(@class, "artTps")]/div[contains(@class, "lCont")]/p[contains(@class, "PT5")]/text()').extract()
                article_time = list_article_time[0]#.encode('utf8')
                print "re" , list_article_time
                article_time = article_time.encode('ascii','ignore')#.decode('unicode_escape').encode('ascii','ignore')
                
            print str(parser.parse(article_time,fuzzy=True))
            print "\n"
            
            list_article_keywords = x_article.xpath('.//div[contains(@class, "artTps")]/div[contains(@class, "lCont")]/p[contains(@class, "PT5")]/a/text()').extract()
            article_keywords = ','.join(list_article_keywords).encode('utf8')
            
            print "key" , article_keywords
            
            
            item = newsItem()
            item['title'] = response.xpath('//title/text()').extract()[0].encode('utf8')
            item['url'] = response.url
            item['crawled_site'] = "firstpost"
            item['content'] = article_content
            item['tags'] = article_keywords
            item['article_time'] = str(parser.parse(article_time))
            return item
            
      