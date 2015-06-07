from twitterfinal import getCurrentTrends
from MongoConnect import queryDatabase
from Score import calculateScore
import operator
import json

result = []

def get_news_items(trendList):
    """
    for trend in trendList[0]['trends']:
        hashtag = trend['name']
        twitter_url = trend['url']
		news = 	getNews(title)
        #print title
        
    """
    
    trends = ["#ModiInBangladesh", "#AFLBluesCrows", "#MaxxManual", "Sheikh Mujibur Rahman", "Cheetah Girls", "Fernando Rodney", "Sarajevo"]
    
    result = {}
    for trend in trends:
        newsitems = queryDatabase(trend)
        if len(newsitems) > 0:
            calculateScore(newsitems)
            sortedlist = sorted(newsitems, reverse = True)
            result[trend] = sortedlist[:5]
            
            """
            print "</br>"
            print "*" * 160
            for item in sortedlist[:6]:
                print "<a href='"+ item.url + "'>" + item.title + "</a></br>"
            print "</br>"
            """
        else:
            result[trend] = []
            
    return result        
if __name__ == "__main__":
    trends = getCurrentTrends()
    #print trends
    result = get_news_items(trends)
    
    for key in result.keys():
        print "--->",key
        for item in result[key]:
            print item, "\n"
        print "*"*300 
        print "\n\n\n"