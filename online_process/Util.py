from collections import Counter
import nltk
import sys
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")
def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word not in cachedStopWords])
   
def get_term_frequency(sentence):
    #sentence = sentence.translate(None, '.,()!?').decode('utf')
    sentence = sentence.translate('.,()!?') 
    sentence = remove_stopwords(sentence)
    x_tokens = nltk.word_tokenize(sentence)
    return Counter(x_tokens)
    
    