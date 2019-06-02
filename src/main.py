import pygame, random
from gameObject import Player, Enemy, Projectile

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

enemies = []

for n in range(10):
    enemyShip = pygame.image.load('../assets/enemyShip00.png')
    enemyShip = pygame.transform.scale(enemyShip, (32, 32))
    randomSpeed = random.randint(50, 250)
    randomPosX = random.randint(0, width)
    e = Enemy(enemyShip, [randomPosX, -128], display, randomSpeed)
    enemies.append(e)
#
# enemy = Enemy(enemyShip, [64, -128], display, 100)

projectileImg = pygame.image.load("../assets/projectile00.png")
projectileImg = pygame.transform.scale(projectileImg, (16, 16))
projectile = Projectile(projectileImg, [64, -128], display, 50, DEEP_BLUE)
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
    # gameDisplay.blit(enemy.surface, enemy.position)
    gameDisplay.blit(projectile.surface, projectile.position)


    for enemy in enemies:
        gameDisplay.blit(enemy.surface, enemy.position)

        if player.rect.colliderect(enemy.rect):
            print("THAT'S A HIT")
            # print("colliding")
            player.position[0] = 100
            player.position[1] = 150

            enemy.position[1] = 10
            enemy.position[0] = random.randint(0, width)
        enemy.update(deltaTime)
    # enemy.update(deltaTime)

    player.update(deltaTime)
    projectile.update(deltaTime)
    pygame.display.update()


    # if player.position[1] <= enemy.position[1]:

    clock.tick(60)
