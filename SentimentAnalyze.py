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

	# Fetches tweets with sentiment labels
	def all_tweets_sentiments(self):
		tweets = []
		for (x,y) in raw_tweet_sentiments:
			if x == '0':
				sentiment_string = 'negative'
			elif x == '2':
				sentiment_string = 'neutral'
			elif x == '4':
				sentiment_string = 'positive'
			tweets.append((y,sentiment_string))
			
		return tweets
	
	# Fetches the gold standardized test data
	def testData(self):
		raw_test_data = open('E:/Twitter Sentiment Anlayzer/Gamification---Twitter-Sentiment-Analyzer/tweet.csv','r')
		test_tweets = []
		for row in csv.reader(raw_test_data):
			test_tweets.append((row[0], ""))
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

	# Filters to select only words that are longer than 2 charcters from both the positive and negative training dataset
	def filtered_tweets(self, input_list):
		# Regex getting rid of the usernames, periods, commas
		regex = re.compile('[@]{1}\w*|\.+|\,+|(and)|(the)|(you)|[x][\w|\d]*')
		tok = Tokenizer(preserve_case=False)
	
		tweets_filtered = []
		
		for (words,sentiment) in input_list:
			words_filtered = [e.lower().encode('utf-8') for e in tok.tokenize(words) if len(e) >= 3 and not regex.match(e)]
			tweets_filtered.append((words_filtered, sentiment))
		return tweets_filtered
	
	# Function to write add the learned data to the train file
	def update_train_data(self, tweet, sentiment):
		csvFile = open('E:/Twitter Sentiment Anlayzer/Gamification---Twitter-Sentiment-Analyzer/train.csv', 'ab')
		csvWriter = csv.writer(csvFile)
		if(sentiment== "positive"):
			val = "4"
		elif(sentiment == "negative"):
			val = "0"
		elif(sentiment == "neutral"):
			val = "2"
	
		csvWriter.writerow([val,"","","","",tweet])
		print "Updated train.csv"
		csvFile.close()
	
	def run(self):
		
		tweets = self.filtered_tweets(self.all_tweets_sentiments())	
		word_features = self.get_word_features(self.get_words_in_tweets(tweets))
	
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
		
		poscount, negcount, neucount = 0,0,0
		
		raw_test_tweets = self.testData()
		test_tweets = self.filtered_tweets(raw_test_tweets)
	
		sentiment_labels = []
		
		test_tweets_with_sentiments = []
		
		for (words,sentiment) in test_tweets:
			sentiment = classifier.classify(extract_features(words))
			test_tweets_with_sentiments.append((words,sentiment))
			if(sentiment == "positive"):
				poscount += 1
			elif(sentiment == "negative"):
				negcount += 1
			elif(sentiment == "neutral"):
				neucount += 1
			sentiment_labels.append(sentiment)
	
		# print test_tweets
		# print poscount
		# print negcount		
		
		Max = poscount
		if negcount > Max:
			Max = negcount
		if neucount > Max:
			Max = neucount
    
		if poscount == Max:
			result = "positive"
		elif negcount == Max:
			result = "negative"
		elif negcount == Max and poscount == Max:
			result = "neutral"
		else:
			result = "neutral"
		
		questionString = [(x.decode('unicode_escape').encode('ascii','ignore')).replace("\r","") for (x,y) in raw_test_tweets]
		
		returntext = [result, questionString, sentiment_labels] 
		print "Result updated for query"
		#print str(returntext)
		return returntext
		
#def main():
#	f = GetData()
#	f.run()
#main()