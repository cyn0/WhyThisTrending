#!/usr/bin/env python
import json
import urllib, urllib2
from HTMLParser import HTMLParser
from datetime import datetime


#class for parsing the html tags and symbols
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()



##**you get trends of previous day mentioned in "htd"**
#'htd': '20140917',

#get the current trending topics (today's ALONE)
def getCurrentTrends():
	param = {'ajax': '1', 'pn': 'p3', 'htv': 'l'}
	value = urllib.urlencode(param)

	req = urllib2.Request("https://www.google.co.in/trends/hottrends/hotItems", value)
	response = urllib2.urlopen(req)
	#print response.read()
	result =  json.load(response)
	return result['trendsByDateList']

def printCurrentTrends(currentTrends):
    for trend in currentTrends['trendsList']:
        title = trend['title'].encode('latin-1', 'replace')
        #hotness = trend['hotnessLevel']
        #newslink = trend['newsArticlesList'][0]['link'].encode('latin-1', 'replace')
        #content = strip_tags(trend['newsArticlesList'][0]['snippet'].encode('latin-1', 'replace'))
        """if content.count('?') > 4:
            if trend['newsArticlesList'].length > 1:
                content = strip_tags(trend['newsArticlesList'][1]['snippet'].encode('latin-1', 'replace'))
        source = trend['newsArticlesList'][0]['source'].encode('latin-1', 'replace')
        """
        print title
        

if __name__ == "__main__":
    print "_"*90
    print str(datetime.now())			

    currentTrends = getCurrentTrends()
    #print json.dumps(currentTrends)
    printCurrentTrends(currentTrends[1])