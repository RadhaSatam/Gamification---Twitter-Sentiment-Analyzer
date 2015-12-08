#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------------------
# Gamification
# ---------------------------------------
# Twitter Sentiment Analyzer
# ---------------------------------------
# CIS 496H - Term Project
# Instructor - Gabriel Murray
# Created by - Radha Satam [300130632]
#
# GetTweets.py
#   Makes use of the tweepy package. 
#   It includes a function that takes the query as the argument, connects to Twitter API and retrieves 
#   the 500 recent public tweets using the query provided as input and stores it in a csv file. 
# ----------------------------------------
#
# !!! Replace 'E:/Twitter Sentiment Anlayzer/Gamification---Twitter-Sentiment-Analyzer/tweet.csv' 
#     with the location of the tweet.csv file in your directoy.
#
import tweepy, csv
from tweepy import OAuthHandler
 
class GetTweets():
    def getting_query_result(self, query):
        # Consumer key and access token information obtained from registering on Twitter
        consumer_key = 'mRJGFxAWklN3ffMzNnbbPwmyi'
        consumer_secret = 'nGSxb13owzSxfSaFofSyTVtziL6PZYmaqpbR0CdUbCJYeU5VYz'
        access_token_raw = '78868741-ioDSiXl5FvBcd6CDqGgBLLul7elMFLbtLFyDdgOwu'
        access_token = access_token_raw.encode('utf-8')
        access_secret = 'EnsD9n880W0TWD6G8pJ5C8n9FUqafi7AdPFszC2IH8ysF'
        
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        
        # Tweepy API verifies authorization
        api = tweepy.API(auth)
        
        # tweet.csv file is opened and written
        csvFile = open('E:/Twitter Sentiment Anlayzer/Gamification---Twitter-Sentiment-Analyzer/tweet.csv', 'wb+')
        
        csvWriter = csv.writer(csvFile)
        
        # query = raw_input("Enter a query search term: ")
       
        # Based on search term (query), it extracts 500 recent tweets
        for tweet in tweepy.Cursor(api.search, 
                            q=query, 
                            show_user = False, 
                            lang="en").items(500):
            csvWriter.writerow([tweet.text.encode('utf-8')])
            # print tweet.text.encode('utf-8')
            
        print "Saved sample tweets from query in tweet.csv"
        csvFile.close()