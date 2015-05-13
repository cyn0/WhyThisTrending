class newsitem(object):

    def __init__(self, title, url, query, p_query, content, crawled_site, article_time, tags):
        self.title = title
        self.url = url
        self.key = query.lower()
        self.p_key = p_query.lower()
        self.content = content.lower()
        self.crawled_site = crawled_site
        self.article_time = article_time
        self.tags = tags.lower()
        self.score = 0
        self.doc_rank = 0.0
    def __repr__(self):
        return self.title + "\n" + self.url
 
    def __lt__(self, other):
         return self.score < other.score