import pygame
import sys
import random
from gameObject import *
from dna import *
# Initialize Pygame
pygame.init()

# Set up display
width, height = 1000, 1000
window = pygame.display.set_mode((width, height))

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255,255,0)
gray = (128,128,128)
brown = (165, 42, 42)

# Set up square
square_size = 50
x, y = width // 2, height // 2
x_speed = 5
y_speed = 5

# instantiate the players in my game
#mickey = gameObject(400,400,gray,10,10,True,0)
mice = []

#brie = gameObject(200,200,yellow,10,10,False,0)
cheeses = []

poops = []

i = 0
while i < 15:
    mice.append(makeRandomMouse(width,height))
    cheeses.append(makeRandomCheese(width,height))
    i += 1


tick = 0
game_tick = 20
poop_tick = 8
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keypresses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        running = False

    # Ensure the square stays on the screen
    x = max(0, min(x, width - square_size))
    y = max(0, min(y, height - square_size))

    # Draw everything
    window.fill(black)  # Fill the background with black
    #pygame.draw.rect(window, white, (x, y, square_size, square_size))

# Inside your game loop
    for mouse in mice:
        mouse.draw(window)
        mouse.age += 1
        if tick % game_tick == 0 and len(cheeses) > 0:
            nearestInd = nearestObject(mouse, cheeses)
            moveCloser(mouse,cheeses[nearestInd], mouse.dna.speed)
            if calculateDistance(mouse,cheeses[nearestInd]) < 15:
                mouse.eat(cheeses[nearestInd])
            if tick % (game_tick*poop_tick) == 0:
                poops.append(mouse.makePoop(width, height))

    apply_gravity(poops)

    for poop in poops:
        poops,cheeses = makeClumps(poops,cheeses)
        poop.draw(window)

    for cheese in cheeses:
        if cheese.width <= 0:
            cheeses.remove(cheese)
        else:
            cheese.age += 1
            cheese.draw(window)



    pygame.display.flip()  # Update the display
        
    tick += 1

    # Control the frame rate
    pygame.time.Clock().tick(60)

