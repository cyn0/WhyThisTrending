from nltk.corpus import stopwords


"""
#salmanKhan -> Salman Khan
#SpanishGP -> Spanish GP
"""

remove_list = ['this', 'on', 'a', 'is', 'when', 'we', 'you', 'that' 'are']
def process_twitter_hashtag(string):
    m_string = []
    string_len = len(string);
    if string[0] == '#':
        i = 1
        while i < string_len:
            if i < string_len -1 and string[i].islower() and string[i+1].isupper():
                m_string.append(string[i])
                m_string.append(" ")
                m_string.append(string[i+1])
                i = i +2;
            elif i < string_len -1 and string[i].isupper() and string[i+1].islower():
                m_string.append(" ")
                m_string.append(string[i])
                m_string.append(string[i+1])
                i = i +2;
            else:
                m_string.append(string[i])
                i = i +1
                
        processed_query =  "".join(m_string).lower()
        
        word_list = processed_query.split()
        processed_query = ' '.join([i for i in word_list if i not in remove_list])
        return processed_query
    else:
        return string

   
if __name__ == "__main__":
    process_twitter_hashtag("#salmanKhan")
    process_twitter_hashtag("#ABadDecisionIsWhen")