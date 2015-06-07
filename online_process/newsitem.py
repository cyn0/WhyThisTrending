from dateutil.parser import parse
class newsitem(object):

    def __init__(self, mongo_result, query, p_query):
        self.title = mongo_result['title'].encode('ascii', 'ignore').lower()
        self.url = mongo_result['url']
        self.key = query.lower()
        self.p_key = p_query.lower()
        self.content = mongo_result['content'].lower()
        self.crawled_site = mongo_result['crawled_site']
        self.article_time = parse(mongo_result['article_time'])
        self.tags = mongo_result['tags'].lower()
        self.score = 0
        self.doc_rank = 0.0
        self.mongo_score = mongo_result['mongo_score']

        
    def __repr__(self):
        #return self.title + "\n" + self.url
        return self.title
        
    def __lt__(self, other):
         return self.score < other.score