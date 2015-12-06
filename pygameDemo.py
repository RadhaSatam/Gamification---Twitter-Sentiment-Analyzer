import pygame
pygame.init()

# Defining colors 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Twitter Sentiment Analyzer')
# pygame.display.update()

gameExit = False

lead_x = 300
lead_y = 300

clock = pygame.time.Clock()

# Main Game Loop 
while not gameExit:
	# Event Handling Loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x -= 10
			if event.key == pygame.K_RIGHT:
				lead_x += 10

	gameDisplay.fill(white)
	# Draw what we want between the display and the update

	pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])
	# gameDisplay.fill(red, rect=[200,200,50,50])
		
	# Updating in the end
	pygame.display.update()

# Quit	
pygame.quit()
quit()