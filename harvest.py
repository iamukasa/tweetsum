import tweepy
from tweepy.streaming import StreamListener
from credentials import *
from nltk import sent_tokenize
import sys
import textsummariser as summarise

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
B=str(sys.argv[1])
new_tweets = api.user_timeline(screen_name=B,count=8000)
b=" "
for s in new_tweets:

     
            b= b+ ". "+ s.text

print ("tweets",b)


print("And the summary for  ",B," is")
thesummarised=summarise.FrequencySummariser().summarize(b.strip(),1)
print (thesummarised)
