#Social Sensing Project - Twitter Crawler
#Lizzie Gidley, Connor Bach, Patrick Fischer

import sys
import csv
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

#key declaration
api_key = ''
api_secret_key = ''

access_token = ''
access_token_secret = ''

# set up the tweepy connection to twitter
auth = OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.wait_on_rate_limit = True
api.wait_on_rate_limit_notify = True

company = input("What company would you like to view? ")

results = api.search(q=company,count=50)
for r in results:
        blob = TextBlob(r.text)
        print(r.text, " Sentiment: ", blob.sentiment, "\n\n")
