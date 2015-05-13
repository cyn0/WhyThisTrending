import MySQLdb
from newsitem import newsitem
from QueryProcessor import process_twitter_hashtag
from Util import remove_stopwords
from dateutil import parser
import datetime
import Settings


db = MySQLdb.connect(Settings.DB_HOST, Settings.DB_USERNAME, Settings.DB_PASSWORD, Settings.DB_NAME)
cursor = db.cursor() 

__max_age_of_article__ = 10
def queryDatabase(query):
    print "query ----> ", query
    processed_hashtag = process_twitter_hashtag(query)
    processed_hashtag = remove_stopwords(processed_hashtag)
    newslist = []
    print "query keywords ----> ", processed_hashtag
    split_words = processed_hashtag.split(" ")
    sql = "SELECT * FROM `NEWS` WHERE "
    
    for word in split_words:
        if len(word) > 1:
            sql = sql + "`CONTENT` LIKE '%"+ word +"%' OR "
    
    #`CONTENT` LIKE '%salman%' 
    sql = sql[:-3]
    sql = sql + "ORDER BY `ARTICLE_TIME` DESC"
    
    #print sql
    
    try:
        # Execute the SQL command
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            title = row[1]
            url = row[2]
            content = row[3]
            crawled_site = row[4]
            article_time = row[5]
            tags = row[6]
            
            #article_time = parser.parse(article_time)
            current_time = datetime.datetime.now()
            
            delta = current_time - article_time
       
            #adding only the articles that are created recently
            if delta.days < __max_age_of_article__:
                newslist.append(newsitem(title, url, query, processed_hashtag, content, crawled_site, article_time, tags))
            """
            # Now print fetched result
            print "*" * 60
            print title
            print tags
            print article_time
            print url
            print "*" * 60
            print"\n"
            """
    except Exception as e:
        print "_____exception____"  
        print e
        
    #print newslist
    return newslist
    
if __name__ == "__main__":
    newslist = queryDatabase('salman')