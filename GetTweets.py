#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, csv
from tweepy import OAuthHandler
 
class GetTweets():
    consumer_key = 'mRJGFxAWklN3ffMzNnbbPwmyi'
    consumer_secret = 'nGSxb13owzSxfSaFofSyTVtziL6PZYmaqpbR0CdUbCJYeU5VYz'
    access_token_raw = '78868741-ioDSiXl5FvBcd6CDqGgBLLul7elMFLbtLFyDdgOwu'
    access_token = access_token_raw.encode('utf-8')
    access_secret = 'EnsD9n880W0TWD6G8pJ5C8n9FUqafi7AdPFszC2IH8ysF'
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    api = tweepy.API(auth)
    
    csvFile = open('E:/tweet.csv', 'w+')
    
    csvWriter = csv.writer(csvFile)
    
    # print api.rate_limit_status()
    print ""
    query = raw_input("Enter a query search term: ")
    print ""
    
    for tweet in tweepy.Cursor(api.search, 
                        q=query, 
                        show_user = False, 
                        lang="en").items(2):
        csvWriter.writerow([tweet.text.encode('utf-8')])
        print tweet.text.encode('utf-8')
    
    csvFile.close()
    
    # Read from csv to list
    # with open('E:/tweet.csv', 'rb') as f:
        #reader = csv.reader(f)
        #your_list = list(reader)
        
    #print your_list
    
    # To display the firt 10 statuses from your timeline
    #
    #for status in tweepy.Cursor(api.home_timeline).items(10):
        # Process a single status
        #print((status.text).encode('utf8'))