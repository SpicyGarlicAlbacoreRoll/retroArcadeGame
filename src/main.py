import pygame, random
from gameObject import Player, Enemy, Projectile
from gameManager import GameManager

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

game_objects = [player]

for n in range(3):
    enemyShip = pygame.image.load('../assets/enemyShip00.png')
    enemyShip = pygame.transform.scale(enemyShip, (32, 32))
    randomSpeed = random.randint(50, 250)
    randomPosX = random.randint(0, width)
    e = Enemy(enemyShip, [randomPosX, -128], display, randomSpeed)
    game_objects.append(e)
    

# projectile = Projectile(projectileImg, [64, -128], display, 50, DEEP_BLUE)
#
# game_objects.append(projectile)

game_manager = GameManager(game_objects, display)
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
    game_manager.draw(gameDisplay)
    game_manager.update(deltaTime)
    pygame.display.update()

    clock.tick(60)
