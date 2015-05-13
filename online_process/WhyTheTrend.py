from twitterfinal import getCurrentTrends
from query import queryDatabase
from Score import calculateScore
import operator

result = []

def get_news_items(trendList):
    """
    for trend in trendList[0]['trends']:
        hashtag = trend['name']
        twitter_url = trend['url']
		news = 	getNews(title)
        #print title
        
        queryDatabase(hashtag)
    """
    
    trends = ["#MIvsDD", "#WeLoveYouSalmanKhan", "#ABadDecisionIsWhen", "#PikuThisFriday", "Dawood", "Greenpeace India", "#WordsThatDontGetUsedEnough", "Simmons", "Tiger Shroff", "Nepal Earthquake"]
    
    for w in trends:
        newsitems = queryDatabase(w)
        #for i in range(len(newsitems)):
        #    print str(i) + "  " + newsitems[i].title
        calculateScore(newsitems)
        sortedlist = sorted(newsitems)
        
        print "*" * 160
        for item in sortedlist[-6:]:
            print item.title

if __name__ == "__main__":
    trends = getCurrentTrends()
    print trends
    newsitems = get_news_items(trends)