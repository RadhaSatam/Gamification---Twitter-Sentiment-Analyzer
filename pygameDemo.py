import pygame, math
from SentimentAnalyze import GetData
from GetTweets import GetTweets

sentimentAnalysis = GetData()
getTweets = GetTweets()

pygame.init()

# Defining colors 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

display_width = 800
display_height = 600

half_width = display_width/2
half_height = display_height/2

x = half_width -160
y = half_height - 15

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


screen = 0
query = ""
returnedresult = ""
hint = 0

# Main Game Loop 
while not gameExit:
	# Event Handling Loop
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if screen == 0:
			if(event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
				screen = 1
		if screen == 1:
			if event.type == pygame.KEYDOWN:
				if event.unicode.isalpha():
					hint = 1
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
		
			
	gameDisplay.fill(white)
	if(screen == 0):
		message_to_screen("Twitter Sentiment Analyzer", black, [half_width-250, half_height-80], 50)
		message_to_screen("Press any key to continue...", green, [half_width-250, half_height-20], 30)
	elif(screen == 1):
		message_to_screen("Enter a query search term - ", black, [half_width-250, half_height-80], 50)
		# pygame.draw.circle(gameDisplay, (192,192,192), (half_width,half_heiht + 150), 50)
		message_to_screen(query, black, [half_width-250, half_height], 30)
		if hint == 1:
			message_to_screen("Press enter to submit...", blue, [half_width-250, half_height+100], 30)
		# TODO - Notify user that system is processing
	elif(screen == 2):
		message_to_screen("Your query:", black, [100, 50], 30)
		message_to_screen(query, blue, [100, 100], 30)
		message_to_screen(returnedresult, green, [200,200],20)
		# TODO - Format properly
		# TODO - Insert Question Tweet - Ask for answer
		# TODO - Take input (Positive or Negative) P/N
		# Disply result
		# If matches, send this back to SentimentAnalyze GetData class and add it
		# to the csv training data file :D
		# Otherwise, tell the user that the system answered otherwise
	elif(screen == 3):
		message_to_screen("Screen 3 now: I guess this will contain, do you want to play again portion", black, [100, 50], 30)
	
	pygame.display.update()
pygame.quit()
quit()