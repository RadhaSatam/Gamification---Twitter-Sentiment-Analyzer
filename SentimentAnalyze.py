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
from tokenize import Tokenizer

raw_train_data = open('E:/Twitter Sentiment Anlayzer/Gamification---Twitter-Sentiment-Analyzer/train.csv', 'r')
raw_tweet_sentiments = []
for row in csv.reader(raw_train_data):
	raw_tweet_sentiments.append((row[0],row[5]))

class GetData:	
		
	# Fetches the positive tweets -- for now it's a list, later figure to take this from a document or use the API
	def positive(self):
		pos_tweets = [(y,'positive') for (x,y) in raw_tweet_sentiments if x=='4']
		return pos_tweets
		
	# Fetches the negative tweets
	def negative(self):
		neg_tweets = [(y,'negative') for (x,y) in raw_tweet_sentiments if x=='0']
		return neg_tweets
	
	# Fetches the gold standardized test data
	def testData(self):
		raw_test_data = open('E:/Twitter Sentiment Anlayzer/Gamification---Twitter-Sentiment-Analyzer/tweet.csv','r')
		test_tweets = []
		for row in csv.reader(raw_test_data):
			test_tweets.append(row[0])
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
	
	def run(self):
		# Regex getting rid of the usernames, periods, commas
		regex = re.compile('[@]{1}\w*|\.+|\,+|(and)|(the)|(you)|[x][\w|\d]*')
		fetch = GetData()
		tok = Tokenizer(preserve_case=False)
		tweets = []
		
		# Filters to select only words that are longer than 2 charcters from both the positive and negative training dataset
		# Stores in tweets list in the format [(word, sentiment)]
		for (words, sentiment) in fetch.positive() + fetch.negative():
			words_filtered = [e.lower().encode('utf-8') for e in tok.tokenize(words) if len(e) >= 3 and not regex.match(e)]
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
		
		raw_test_tweets = fetch.testData()
		test_tweets = []
		for words in raw_test_tweets:
			words_filtered = [e.lower().encode('utf-8') for e in tok.tokenize(words) if len(e) >= 3 and not regex.match(e)]
			test_tweets.append(words_filtered)
			
		poscount = 0
		negcount = 0
		sentiment_lables = []
		for tweet in test_tweets:
			classifier1 = classifier.classify(extract_features(tweet))
			sentiment_lables.append(classifier1)
			if(classifier1 == "positive"):
				poscount += 1
			elif(classifier1 == "negative"):
				negcount += 1
		
		# print poscount
		# print negcount		
		# print test_tweets 
		
		if poscount > negcount:
			print "The sentiment analysis from the last 600 tweets is - positive"
		elif negcount > poscount:
			print "The sentiment analysis from the last 600 tweets is - negative"
		else:
			print "The sentiment analysis from the last 600 tweets is - neutral"
		
		print "\nOne random tweet and the sentiment -"
		print raw_test_tweets[2]
		print sentiment_lables[2]

def main():
	f = GetData()
	f.run()
	
main()