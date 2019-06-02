import pygame, random
from gameObject import Player, Enemy

pygame.init()
display = width, height = 400, 300
gameDisplay = pygame.display.set_mode(display)
pygame.display.set_caption('a bit retro')

clock = pygame.time.Clock()

running = True

playerSpeed = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WARM_WHITE = (255, 241, 215)
DEEP_BLUE = (0, 20, 56)
playerDim = [32, 32]
enemyDim00 = [32, 32]
playerPos = [20, 20]
getTicksLastFrame = 0

playerShip = pygame.image.load('../assets/playerShip.png')
playerShip = pygame.transform.scale(playerShip, (32, 32))
player = Player(playerShip, playerPos, display, playerSpeed)

enemyShip = pygame.image.load('../assets/enemyShip00.png')
enemyShip = pygame.transform.scale(enemyShip, (32, 32))
enemy = Enemy(enemyShip, [64, -128], display, 100)

# main loop


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(event)
    
    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    gameDisplay.fill(WARM_WHITE)
    gameDisplay.blit(player.surface, player.position)
    gameDisplay.blit(enemy.surface, enemy.position)
    pygame.display.update()
    player.update(deltaTime)
    enemy.update(deltaTime)

    if player.position[1] <= enemy.position[1]:
        player.position[0] = 200
        player.position[1] = 150

        enemy.position[1] = -64
        enemy.position[0] = 50
    clock.tick(60)
