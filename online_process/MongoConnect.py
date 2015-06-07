from pymongo import MongoClient
from newsitem import newsitem
from QueryProcessor import process_twitter_hashtag
from Util import remove_stopwords
from dateutil import parser
import datetime
import Settings
import sys, json

__max_age_of_article__ = 10
__client__ = MongoClient(Settings.MONGO_URL)
__db__ = __client__[Settings.MONGODB_NAME]
__collection__ = __db__[Settings.MONGODB_COLLECTION_NAME]
    
def queryDatabase(query):
    print "query ----> ", query
    processed_hashtag = process_twitter_hashtag(query)
    processed_hashtag = remove_stopwords(processed_hashtag)
    newslist = []
    print "query keywords ----> ", processed_hashtag
    
    fiveDaysAgo = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%d 00:00:00")
    
    """
    Performing the "text search" on document that are created less than 5 days ago.
    """
    results = __collection__.find({
                                'article_time' : {
                                    "$gte": fiveDaysAgo
                                },
                                '$text': 
                                        { 
                                            '$search': processed_hashtag, 
                                            '$language': "en" 
                                        } 
                                },{ 
                                    'mongo_score': { '$meta': "textScore" }
                                }
                                ).sort( 
                                   #{ 
                                   [('mongo_score', 
                                        { '$meta': "textScore" }) ]
                                   #} 
                                   ).limit(25)
    for result in results:
        newslist.append( newsitem(result, query, processed_hashtag) )

    return newslist
    

if __name__ == "__main__":
    newslist = queryDatabase(sys.argv[1])
    for news in newslist:
        print news
        