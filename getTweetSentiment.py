# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:15:59 2020

@author: ptfis
"""

import re
import tweepy
import nltk
from tweepy import OAuthHandler
from textblob import TextBlob
from nltk.corpus import stopwords

class TwitterClient(object):
    def __init__(self):
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''
        nltk.download('stopwords')
        
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("ErrorL authentication failed!")
        
    def clean_tweet(self, tweet):
        #tweet_list = [ele for ele in tweet.split() if ele != 'user']
        #clean_tokens = [t for t in tweet_list if re.match('r[^\W\d]*$', t)]
        #clean_s = ' '.join(clean_tokens)
        tweet = [word for word in tweet.split() if word.lower() not in stopwords.words('english')]
        tweet = ' '.join(tweet)
        tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        return tweet
    
    def form_sentence(self, tweet):
        tweet_blob = TextBlob(tweet)
        return ' '.join(tweet_blob.words)
    
    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
    
    def get_tweets(self, query, count = 10):
        tweets = []
        
        try:
            fetched_tweets = self.api.search(q = query, count = count)#, until="2020-04-21")
            
            for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet['text'] = tweet.text
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                
                #if tweet.retweet_count > 0:
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
            return tweets
        except tweepy.TweepError as e:
            print("Error: " + str(e))    


def returnSentiment(query):
    api = TwitterClient()
    tweets = api.get_tweets(query = query, count = 200)

    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    positive = 100*(len(ptweets))/len(tweets)
    negative = 100*(len(ntweets))/len(tweets)
    neutral = 100 - positive - negative

    returner = {'positive': positive, 'negative': negative, 'neutral': neutral}
    return returner

def main():
    api = TwitterClient()
    query = input("Enter a search keyword:")
    tweets = api.get_tweets(query = query, count = 200)
    
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets))) 
  
    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])
  
    # printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text']) 
  
if __name__ == "__main__": 
    # calling main function 
    main()

