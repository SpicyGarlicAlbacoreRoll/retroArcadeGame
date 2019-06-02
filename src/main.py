import sys
import pygame
import projectile

pygame.init()
display = width, height = 400, 300
gameDisplay = pygame.display.set_mode(display)

pygame.display.set_caption('a bit retro')

clock = pygame.time.Clock()

running = True

playerSpeed = 500

BLACK     = (0, 0, 0)
WHITE     = (255, 255, 255)
WARMWHITE = (255, 241, 215)
DEEPBLUE  = (0, 20, 56)
playerDim = [40, 40]
playerPos = [20, 20]
getTicksLastFrame = 0

# playerSprite = pygame.sprite.Sprite(DEEPBLUE, playerDim[0], playerDim[1])
# player = pygame.sprite([20, 20, 100], 20, 20)

def handleInputs(deltaTime):
    if pygame.key.get_pressed()[pygame.K_a] and not playerPos[0] < 0:
        playerPos[0] -= playerSpeed * deltaTime
    elif pygame.key.get_pressed()[pygame.K_d] and not playerPos[0] > width - playerDim[0]:
        playerPos[0] += playerSpeed * deltaTime
    if pygame.key.get_pressed()[pygame.K_s] and not playerPos[1] > height - playerDim[1]:
        playerPos[1] += playerSpeed * deltaTime
    elif pygame.key.get_pressed()[pygame.K_w] and not playerPos[1] < 0:
        playerPos[1] -= playerSpeed * deltaTime


    
# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
            print(event)
    
    t = pygame.time.get_ticks()
# deltaTime in seconds.
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    gameDisplay.fill(WARMWHITE)
    pygame.draw.rect(gameDisplay, DEEPBLUE, [playerPos[0], playerPos[1], playerDim[0], playerDim[1]], 2)
    pygame.display.update()
    
    # playerPos[0] = playerPos[0] + 1
    # playerPos[1] = playerPos[1] + 1
    handleInputs(deltaTime)
    clock.tick(60)



    # pygame.draw.rect(player, [20, 120, 120], 20)