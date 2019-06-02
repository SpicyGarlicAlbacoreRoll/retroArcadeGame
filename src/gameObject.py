import pygame
import random

class GameObject:
    def __init__(self, surface, position, screen):
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.rect.x = position[0] + 5   # Offset for hit-boxes
        self.rect.y = position[1] + 5
        self.rect.width = surface.get_width() - 10
        self.rect.height = surface.get_height() - 10
        self.position = position
        self.dt = 0
        self.screen = screen

    def update(self, dt):
        self.dt = dt
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]


class Player(GameObject):
    def __init__(self, surface, position, screen, speed):
        GameObject.__init__(self, surface, position, screen)
        self.speed = speed

    def update(self, dt):
        GameObject.update(self, dt)
        self.handle_inputs(dt)

    def handle_inputs(self, dt):
        if pygame.key.get_pressed()[pygame.K_a] and not self.position[0] < 0 + 8:
            self.position[0] -= self.speed * dt
        elif pygame.key.get_pressed()[pygame.K_d] \
                and not self.position[0] > self.screen[0] - self.surface.get_width() - 8:
            self.position[0] += self.speed * dt
        if pygame.key.get_pressed()[pygame.K_s] \
                and not self.position[1] > self.screen[1] - self.surface.get_height() - 16:
            self.position[1] += self.speed * dt
        elif pygame.key.get_pressed()[pygame.K_w] and not self.position[1] < 0 + 16:
            self.position[1] -= self.speed * dt


class Enemy(GameObject):
    def __init__(self, surface, position, screen, speed):
        GameObject.__init__(self, surface, position, screen)
        self.speed = speed

    def update(self, dt):
        GameObject.update(self, dt)
        self.position[1] += self.speed * dt

        if self.position[1] > self.screen[1]:
            self.position[1] = -128
            self.position[0] = random.randint(0, self.screen[0])


class Projectile(GameObject):
    def __init__(self, surface, position, screen, speed, color):
        GameObject.__init__(self, surface, position, screen)
        # self.position[0] = random.randint(0, self.screen[0])
        # self.position[1] = 32
        # self.rect.x = position[0]
        # self.rect.y = position[1]
        self.rect.width = surface.get_width()
        self.rect.height = surface.get_height()
        self.lifeTime = 0
        self.speed = speed
        self.color = color
        self.dt = 0

    def update(self, dt):
        GameObject.update(self, dt)
        self.lifeTime += dt
        self.position[1] += self.speed * dt
