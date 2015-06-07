from dateutil import parser
from collections import Counter
import datetime
from DocRank import calculate_doc_rank
from DocRank import get_page_rank_matrix
from DocRank import get_total_doc_values

__key__ = ""
__processed_keys__ = ""

__match_title__ = 90

__partial_match_content__ = 50

__match_tag__ = 75

__max_age_of_article__ = 5

__article_time__ = 75

__doc_rank_weight__ = 0.6
__mongo_score_weight__ = 0.75

def calculateScore(newsitems):
    __key__ = newsitems[0].key
    __processed_keys__ = newsitems[0].p_key.split(" ")
    
    #calculate the global score of document
    calculate_doc_rank(newsitems)
    
    for newsitem in newsitems:
        title = newsitem.title
        content = newsitem.content
        article_time = newsitem.article_time
        current_time = datetime.datetime.now()
        tags = newsitem.tags
        delta = current_time - article_time
        #print "scoring---->", title 
        score = 0.0
            
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
            
        for key in __processed_keys__:
            score += (newsitem.counts[key] * __partial_match_content__)
        
        #checking tags
        if __key__ in tags:
	         score += (5 * __match_tag__) 
        else:
	           for key in __processed_keys__:
		             if key in tags:
		                score += __match_tag__
	         
        base = (__article_time__ + __match_title__ + __partial_match_content__ + __match_tag__)
            
        newsitem.score = score / base
    
     
        doc_rank_base = get_total_doc_values()
        
        newsitem.score += __doc_rank_weight__  * (newsitem.doc_rank/doc_rank_base)
        newsitem.score += __mongo_score_weight__ * newsitem.mongo_score 
    """pR = get_page_rank_matrix()
       
    print pR    
    prinrted(range(len(pR)), key=lambda i: pR[i], reverse=True)[:5]
    sortedIndex = sorted(range(len(pR)), key=lambda i: pR[i], reverse=True)
    
    for i in range(len(sortedIndex)):
       	print "score--->" , pR[sortedIndex[i]]
        print "title", newsitems[sortedIndex[i]].title
    """ 
    
        

