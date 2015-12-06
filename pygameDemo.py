import pygame
from SentimentAnalyze import GetData

pygame.init()
pygame.font.init()

# Defining colors 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Twitter Sentiment Analyzer')

gameExit = False

clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.Font(None, 50)

# Function to display text of specified color to user
def message_to_screen(msg, color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [(display_width/2)-250, display_height/2-20])

# Main Game Loop 
while not gameExit:
	# Event Handling Loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
			
	gameDisplay.fill(white)
	message_to_screen("Twitter Sentiment Analyzer", black)
	pygame.display.update()

		

pygame.quit()
quit()