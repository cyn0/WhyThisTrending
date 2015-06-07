from __future__ import division
from collections import Counter
from Util import get_term_frequency
#from Matrix import RankMatrix

#doc_rank_matrix = None
total_doc_values = None
def calculate_doc_rank(newsitems):
    global total_doc_values
    total_doc_values = 0.0
    total_counts = Counter()
    for newsitem in newsitems:
        newsitem.counts = get_term_frequency(newsitem.content)
        total_counts += newsitem.counts
    #print total_counts
    for newsitem in newsitems:
        similarity = 0.0
        for term in total_counts.elements():
            #similarity += (( newsitem.counts[term] / len(newsitem.content))/ total_counts[term])
            similarity += ( newsitem.counts[term] / total_counts[term])
        newsitem.doc_rank = similarity
        total_doc_values += similarity

def get_total_doc_values():
    return total_doc_values

def get_page_rank_matrix():
    return None #doc_rank_matrix.get_page_rank_matrix()

 
"""
def calculate_doc_rank(newsitems):
    global doc_rank_matrix
    newsitems_len = len(newsitems)
    doc_rank_matrix = RankMatrix(newsitems_len)
    for i in range(newsitems_len):
        for j in range(newsitems_len):
            if i != j :
                similarity = calculate_similarity(newsitems[i], newsitems[j])
                doc_rank_matrix.set_matrix(i, j, similarity)
    
    mat = doc_rank_matrix.get_matrix()
    for i in range(newsitems_len):
        print "$" * 100
        print newsitems[i].title
        print "_" * 100
        for j in range(newsitems_len):
            print newsitems[j].title, str(mat[i][j])
    doc_rank_matrix.normalize_matrix()


def calculate_similarity(x_newsitem, y_newsitem):
    x_counts = x_newsitem.counts   
    y_counts = y_newsitem.counts
    
    intersection = x_counts & y_counts
    
    #print intersection
    
    commonWordsSum = 0.0;
    for term in intersection.elements():
        xVal = x_counts[term]
        yVal = y_counts[term]
        #print math.tanh(yVal / xVal);
        commonWordsSum += math.tanh(yVal / xVal);
    
    #print "Relevnce---> ", commonWordsSum;
    return commonWordsSum
"""