#!/usr/bin/env python
import json
import urllib2
from datetime import datetime
import twitter
from news_search import getNews
import Settings

##**you get trends of previous day mentioned in "htd"**
#'htd': '20140917',

#get the current trending topics (today's ALONE)
def getCurrentTrends():
	auth = twitter.oauth.OAuth(Settings.OAUTH_TOKEN, Settings.OAUTH_TOKEN_SECRET,
                           Settings.CONSUMER_KEY, Settings.CONSUMER_SECRET)

	twitter_api = twitter.Twitter(auth=auth)

	WOE_ID = 23424848
#2295424 - chennai
#23424848 india

	trends = twitter_api.trends.place(_id=WOE_ID)
	#trends = twitter_api.search.tweets(q="#TVDayWithFlipkart",result_type="popular")
	return trends


def findWhyTrending(currentTrends):
	for trend in currentTrends[0]['trends']:
		title = trend['name']
		link = trend['url']
		news = 	getNews(title)
		if len(news) > 0:
			link = news[0]['link']
		list_items = "";
		
		for i in range(2):
			if not news or i >= len(news):
				break;
			list_items = list_items +  news[i]['title'] ;

			#get source from url
			url = news[i]['link']
			index = url.find("&url=http://"); 
			source = url[index + 12 : url.find("/", index + 12)]
			
			list_items = list_items + "\n\n";

		if(len(list_items) < 2):
			list_items = "Trending";
		title = title.replace("'","")
		list_items = list_items.encode('utf8')
        
        #list_items = list_items.replace("'","")
		print "*" * 40
		print title
		#print link
		print list_items
		print "*" * 40

if __name__ == "__main__":
    print str(datetime.now())
    currentTrends = getCurrentTrends()
    print json.dumps(currentTrends)
    findWhyTrending(currentTrends)
