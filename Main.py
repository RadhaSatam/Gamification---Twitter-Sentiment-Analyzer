# Gamification
# ---------------------------------------
# Twitter Sentiment Analyzer
# ---------------------------------------
# CIS 496H - Term Project
# Instructor - Gabriel Murray
# Created by - Radha Satam [300130632]
#
# Main.py
#	This is the main file which contains the code for the game. 
#	The user interface is generated here. 
#	The actions are specified based on certain events and based on which screen the user is currently on. 
#	This file makes use of the pygame package and uses GetTweets to get the tweets 
#	 based on user query and SentimentAnalyze for training and tagging the dataset.
#
# ----------------------------------------

import pygame, math
from SentimentAnalyze import GetData
from GetTweets import GetTweets

# Objects declared for the two other classes
sentimentAnalysis = GetData()
getTweets = GetTweets()

# Initialized
pygame.init()

# Defining colors 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Width and Height of the surface
display_width = 800
display_height = 600

half_width = display_width/2
half_height = display_height/2

# Display surface specified
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Twitter Sentiment Analyzer')

gameExit = False

# clock = pygame.time.Clock()
pygame.font.init()

# Function to display text of specified color to user
def message_to_screen(msg, color, location, fontsize):
	font = pygame.font.Font(None, fontsize)
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, location )

# Variable declarations
screen = 0
query = ""
returnedresult = ""
user_response = ""
response_printed = 0
tweet_number = 1

# Main Game Loop 
while not gameExit:
	# Event Handling Loop
	save_to_file = 0
	
	# Event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		# For screen 0 
		if screen == 0:
			if(event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
				screen = 1
		# For screen 1
		if screen == 1:
			if event.type == pygame.KEYDOWN:
				if event.unicode.isalpha():
					query += event.unicode
				elif event.key == pygame.K_BACKSPACE:
					query = query[:-1]
				elif event.key == pygame.K_SPACE:
					query += " "
				elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					if(query!=""):
						screen = 2
						getTweets.getting_query_result(query)
						returnedresult = sentimentAnalysis.run()	
		# For screen 2	
		if screen == 2:
			if event.type == pygame.KEYDOWN:
				if response_printed == 0:
					if event.key == pygame.K_p:
						user_response = "positive"
						save_to_file = 1
					elif event.key == pygame.K_n:
						user_response = "negative"
						save_to_file = 1
					elif event.key == pygame.K_x:
						user_response = "neutral"
						save_to_file = 1
				elif(response_printed == 1):
					if event.key == pygame.K_y:
						tweet_number += 1
						user_response = ""
						response_printed = 0					
					if event.key == pygame.K_e:
						query = ""
						user_response = ""
						response_printed = 0
						screen = 1
						
	gameDisplay.fill(white)
	if(screen == 0):
		message_to_screen("Twitter Sentiment Analyzer", black, [half_width-250, half_height-80], 50)
		message_to_screen("Press any key to continue...", green, [half_width-250, half_height-20], 30)
	elif(screen == 1):
		message_to_screen("Enter a query search term - ", black, [half_width-250, half_height-80], 50)
		# pygame.draw.circle(gameDisplay, (192,192,192), (half_width,half_heiht + 150), 50)
		message_to_screen(query, black, [half_width-250, half_height], 30)
		if(query!=""):
			message_to_screen("Press enter to submit...", blue, [half_width-250, half_height+50], 30)
			message_to_screen("(Kindly wait a minute for processing)", blue, [half_width-250, half_height+80], 20)
		# TODO - Notify user that system is processing
	elif(screen == 2):
		message_to_screen("Your query:", black, [50, 50], 30)
		message_to_screen(query, black, [50, 80], 25)
		if(returnedresult[0] == "positive"):
			color = green
		elif(returnedresult[0] == "negative"):
			color = red
		elif(returnedresult[0] == "neutral"):
			color = black
		message_to_screen("The sentiment analysis for the query from the last 500 tweets - " + returnedresult[0], color, [50,130],25)	
		message_to_screen("For the following tweet, enter positive (P), negative (N) or neutral (X) - ", blue, [50,170],25)
	
		tweet_question = returnedresult[1]
		tweet_sentiment = returnedresult[2]
		
		# Dividing the tweet in half for easier display (Max chars in tweet = 140 so it's not a problem)
		t = (tweet_question[tweet_number]).split(' ')
		firstpart, secondpart = t[:len(t)/2], t[len(t)/2:]
		message_to_screen(' '.join(firstpart), black, [50,200],25)
		message_to_screen(' '.join(secondpart), black, [50,225],25)
		
		if(user_response!=""):	
			if(user_response == "positive"):
				color = green
			elif(user_response == "negative"):
				color = red
			else:
				color = black
			message_to_screen("Your response: " + user_response, color, [50,280],25)
			
			if(tweet_sentiment[tweet_number] == "positive"):
				color = green
			elif(tweet_sentiment[tweet_number] == "negative"):
				color = red
			else:
				color = black
			message_to_screen("System response: " + tweet_sentiment[tweet_number], color, [50,310],25)
			response_printed = 1
		
		if(response_printed == 1):
			color = red
			if(user_response == tweet_sentiment[tweet_number]):
				color = green
				message_to_print = "Congratulations your answer matched the system response!!"
				if(save_to_file==1):
					sentimentAnalysis.update_train_data(tweet_question[tweet_number], tweet_sentiment[tweet_number])
			else:
				message_to_print = "Sorry, your answer didn't match the system response."
				# If the answers don't match but the overall sentiment matches, we add it to the train data
				if(user_response == returnedresult[0] and save_to_file ==1):
					sentimentAnalysis.update_train_data(tweet_question[tweet_number], user_response)						
			message_to_screen(message_to_print, color, [50,360],25)
			message_to_screen("Press (Y) to see another tweet from the same query...", black, [50,420],20)
			message_to_screen("Press (E) to enter a new query...", black, [50,440],20)
			
	elif(screen == 3):
		message_to_screen("Screen 3 now: I guess this will contain, do you want to play again portion", black, [100, 50], 30)
	
	# Update is where it gets shown to the user
	pygame.display.update()
pygame.quit()
quit()