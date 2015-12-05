# Gamification
# ---------------------------------------
# Twitter Sentiment Analyzer
# ---------------------------------------
# CIS 496H - Term Project
# Instructor - Gabriel Murray
# Created by - Radha Satam [300130632]
# ----------------------------------------

# Imports
from __future__ import division
from nltk import *
import nltk, re, pprint, csv

raw_train_data = open('E:/train.csv', 'r')
raw_tweet_sentiments = []
for row in csv.reader(raw_train_data):
	raw_tweet_sentiments.append((row[0],row[5]))

class GetData:	
		
	# Fetches the positive tweets -- for now it's a list, later figure to take this from a document or use the API
	def positive(self):
		pos_tweets = [(y,'positive') for (x,y) in raw_tweet_sentiments if x=='4']
		# pos_tweets = [('I love this car', 'positive'),('This view is amazing', 'positive'), ('I feel great this morning', 'positive'),('I am so excited about the concert', 'positive'),('He is my best friend', 'positive')]
		return pos_tweets
		
	# Fetches the negative tweets
	def negative(self):
		neg_tweets = [(y,'negative') for (x,y) in raw_tweet_sentiments if x=='0']
		# neg_tweets = [('I do not like this car', 'negative'), ('This view is horrible', 'negative'), ('I feel tired this morning', 'negative'), ('I am not looking forward to the concert', 'negative'),('He is my enemy', 'negative')]
		return neg_tweets
	
	# Fetches the gold standardized test data
	def testData(self):
		test_tweets = [(['feel', 'happy', 'this', 'morning'], 'positive'),(['larry', 'friend'], 'positive'),(['not', 'like', 'that', 'man'], 'negative'),(['house', 'not', 'great'], 'negative'),(['your', 'song', 'annoying'], 'negative')]
		return test_tweets
	
	# Gets a list of all the words in the tweets, without the sentiments
	def get_words_in_tweets(self, tweets):
		all_words = []
		for (words, sentiment) in tweets:
			all_words.extend(words)
		return all_words
		
	# Gets a list of ordered set of words which occur most frequently  
	def get_word_features(self, wordlist):
		wordlist = nltk.FreqDist(wordlist)
		word_features = wordlist.keys()
		return word_features
	

def main():
	fetch = GetData()
	tweets = []
	
	# Filters to select only words that are longer than 2 charcters from both the positive and negative training dataset
	# Stores in tweets list in the format [(word, sentiment)]
	for (words, sentiment) in fetch.positive() + fetch.negative():
		words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
		tweets.append((words_filtered, sentiment))
		
	word_features = fetch.get_word_features(fetch.get_words_in_tweets(tweets))

	# Function that creates a dictionary that has entires like - {contains(word): False, ...}
	def extract_features(document):
		document_words = set(document)
		features = {}
		for word in word_features:
			features['contains(%s)' % word] = (word in document_words)
		return features
	
	# Training set and Naive Bayes Classifier are used to classify the words - ends up classifying the above dictionary format with the sentiment associated
	training_set = nltk.classify.apply_features(extract_features, tweets)
	classifier = nltk.NaiveBayesClassifier.train(training_set)
	
		
	tweet = 'Larry is weird horrible insane. Fuck. Amaze.'
	print classifier.classify(extract_features(tweet.split()))

main()	
	