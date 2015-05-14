#Why is this trending

The objective of `WhyThisTrending` project is to find why a particular term(hash tag) is trending in the social media.

**This project is in very intial stage of developement**

#Example
**#WeLoveYouSalmanKhan**
  - Bigg Boss 7: Fans show support for Salman Khan - Financial Express
  - Salman Khans bail justified or unusual? Lawyers divided over Bombay HC decision - Firstpost

#Methodology
###Offline process - Crawling
Scrapy tool is used to crawl News sites to extract content and other information from the site. The extracted contents are stored in SQL database.

###Online process - Searching and scoring
Trending keywords are retried from social media(Twitter, Google trends) and articles having those key-words are fetched.

Scoring is the most crucial process as there might be several articles containing the key-words.

  * Local scoring
    + Here, an article is scored based on its content, date, tags etc
  - Global scoring
    + Finding importance of an article across all the articles fetched.
    + For example, in the last three days there might be several articles about Mr.Modi but we are interested in the `special event` that made the people to talk about him(here local scoring alone won't be helpful). Our assumption is that `special event` will be in the most number of articles.
    + [Algorithms of the Intelligent Web]
    
#usage
###Offline process
`scrapy crawl <spider_name>`

***For example***
`scrapy crawl firstpost -s DEPTH_LIMIT=2 -s LOG_FILE=newscrapy_13may_1.log -s CLOSESPIDER_PAGECOUNT=500`

All settings parameters are optional.

###Online proces
`python WhyTheTrend.py`

[Algorithms of the Intelligent Web]:http://www.amazon.in/Algorithms-Intelligent-Web-Haralambos-Marmanis/dp/1933988665
