# function for stripping punctuation marks.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def remove_punc_chars(astring):
    for char in punctuation_chars:
        if char in astring:
            astring = astring.replace(char,"")
    return astring 

# function for positive words to use
positive_words = []
with open("C:/Python-learning/projects/Sentiment_classifier/assest/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(astring1):
    astring_new = remove_punc_chars(astring1).lower()
    astring_new_list = astring_new.split()
    pos_words = 0 
    for word in astring_new_list:
        if word in positive_words:
            pos_words += 1 
    return pos_words

# function for negative words to use
negative_words = []
with open("C:/Python-learning/projects/Sentiment_classifier/assest/negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(astring1):
    astring_new = remove_punc_chars(astring1).lower()
    astring_new_list = astring_new.split()
    neg_words = 0 
    for word in astring_new_list:
        if word in negative_words:
            neg_words += 1 
    return neg_words   

# Main Code for Sentiment classifier
with open("C:/Python-learning/projects/Sentiment_classifier/assest/project_twitter_data.csv","r") as f:
     with open("C:/Python-learning/projects/Sentiment_classifier/assest/resulting_data.csv",'w') as out:
    # Header row
      out.write("Number of Retweets,Number of Replies,Positive Scores,Negative Scores,Net Scores\n")
    
      next(f) # Header skipped
    
      for line in f:
         parts = line.strip().split(',')
         join_tweets = ",".join(parts[:-2])
        
         reply = parts[-1]
         retweet =parts[-2]
        
         pos = get_pos(join_tweets)
         neg = get_neg(join_tweets)
         net = pos - neg  
         out.write(retweet + "," + reply + "," + str(pos) + "," + str(neg) + "," + str(net) + "\n")