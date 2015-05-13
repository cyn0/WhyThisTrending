from dateutil import parser
import datetime
from DocRank import calculate_doc_rank
from DocRank import get_page_rank_matrix
from Util import get_term_frequency
from DocRank import get_total_doc_values
#datetime.datetime(2015, 3, 15, 9, 11)

__score__ = 0.001
__key__ = ""
__processed_keys__ = ""

__match_title__ = 90

__partial_match_content__ = 50

__match_tag__ = 75

__max_age_of_article__ = 10

__article_time__ = 75

__doc_rank_weight__ = 0.6

def calculateScore(newsitems):
    __key__ = newsitems[0].key
    __processed_keys__ = newsitems[0].p_key.split(" ")
    
    
    for newsitem in newsitems:
        title = newsitem.title
        content = newsitem.content
        article_time = newsitem.article_time
        current_time = datetime.datetime.now()
        tags = newsitem.tags
        delta = current_time - article_time
        #print "scoring---->", title 
        #scoring only the articles that are created recently
        if delta.days > __max_age_of_article__:
            newsitem.score = 0.0

        else:
            score = 0
            
            #article date
            score += (__max_age_of_article__ - delta.days) * __article_time__
            
            #checking in title
            if __key__ in title:
                score += (5 * __match_title__)
            else:
                for key in __processed_keys__:
                    if key in title:
                        score += __match_title__
            
            #checking content
            newsitem.counts = get_term_frequency(content)
            
            for key in __processed_keys__:
                score += (newsitem.counts[key] * __partial_match_content__)
	    if __key__ in tags:
		score += (5 * __match_tag__) 
	    else:
		for key in __processed_keys__:
			if key in tags:
				score += __match_tag__
	         
            base = (__article_time__ + __match_title__ + __partial_match_content__)
            
            newsitem.score = score / base
    
    calculate_doc_rank(newsitems) 
    doc_rank_base = get_total_doc_values()
    newsitem.score = __doc_rank_weight__  * (newsitem.doc_rank/doc_rank_base)
    
    """pR = get_page_rank_matrix()
       
    print pR    
    print sorted(range(len(pR)), key=lambda i: pR[i], reverse=True)[:5]
    sortedIndex = sorted(range(len(pR)), key=lambda i: pR[i], reverse=True)
    
    for i in range(len(sortedIndex)):
       	print "score--->" , pR[sortedIndex[i]]
        print "title", newsitems[sortedIndex[i]].title
    """ 
    
        

