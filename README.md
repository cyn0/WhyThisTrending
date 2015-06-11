#Why is this trending

The objective of `WhyThisTrending` project is to find why a particular term(hash tag) is trending in the social media.

**This project is in very intial stage of development**

#Example
INPUT : **#WeLoveYouSalmanKhan**

OUTPUT :
  - Bigg Boss 7: Fans show support for Salman Khan - Financial Express
  - Salman Khans bail justified or unusual? Lawyers divided over Bombay HC decision - Firstpost

#Methodology
###Offline process - Crawling
Scrapy tool is used to crawl News sites to extract content and other information from the site. The extracted contents are stored in MongoDB.

###Online process - Searching and scoring
Trending keywords are retrieved from social media(Twitter, Google trends) and articles having those key-words are fetched.

Scoring is the most crucial process as there might be several articles containing the key-words.
  * MongoDB scoring
    + Text search is done for the keywords, and MongoDB returns document’s score associated with the text search.
  * Local scoring
    + Here, an article is scored based on its content, date, tags etc
  - Global scoring
    + Finding importance of an article across all the articles fetched.
    + For example, in the last three days there might be several articles about Mr.Modi but we are interested in the `special event` that made the people to talk about him(here local scoring alone won't be helpful). Our assumption is that `special event` will be in the most number of articles.

Reference : [Algorithms of the Intelligent Web]    

#Initial configurations
###MongoDB
Add your MongoDB params in *crawler/tutorial/settings.py* and to *online_process/Setting.py* file

    #mongodb credentials
    MONGO_URL = "mongodb://localhost:27017/"
    MONGODB_NAME = "WhyThisTrend"
    MONGODB_COLLECTION_NAME = "article"

###Twitter
If your using Twitter API to retrieve current trend, add your twitter keys to *online_process/Setting.py* file
    
    CONSUMER_KEY = 'XXXX'
    CONSUMER_SECRET ='YYYY'
    OAUTH_TOKEN = 'ZZZZ'
    OAUTH_TOKEN_SECRET = 'AAAA'


#Usage
###Offline process
To run all the spiders, run the run_spiders.sh file

`source run_spiders.sh`

or to run a particular spider

`scrapy crawl <spider_name>`

***For example***
`scrapy crawl firstpost -s DEPTH_LIMIT=2 -s LOG_FILE=newscrapy_13may_1.log -s CLOSESPIDER_PAGECOUNT=500`

All settings parameters are optional.

###Online process
`python WhyTheTrend.py`

[Algorithms of the Intelligent Web]:http://www.amazon.in/Algorithms-Intelligent-Web-Haralambos-Marmanis/dp/1933988665
