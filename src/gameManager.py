import pygame
from gameObject import Projectile, Enemy, Player
import random


class GameManager:

    def __init__(self, game_objects, game_screen):
        self.game_objects = game_objects
        self.player = game_objects[0]
        self.game_screen = game_screen
        self.game_screen_width = game_screen[0]
        self.game_screen_height = game_screen[1]
        self.gameOver = False

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def update(self, dt):
        if not self.player.isAlive:
            self.gameOver = True
        for game_object in self.game_objects:
            game_object.update(dt)

            if game_object.isFiring:
                self.create_projectile(game_object)

        if not self.gameOver:
            self.physics()

    def draw(self, game_screen):
        for game_object in self.game_objects:
            game_object.draw(game_screen)

    def create_projectile(self, game_object):
        if isinstance(game_object, Player):
            position = [game_object.position[0], game_object.position[1] - 32]
            projectile = Projectile(game_object.projectileImg, position, game_object.screen, game_object.speed + 10, (255, 255, 255))
        else:
            position = [game_object.position[0], game_object.position[1] + 32]
            projectile = Projectile(game_object.projectileImg, position, game_object.screen, -game_object.speed*1.5, (255, 255, 255))

        self.game_objects.append(projectile)
        game_object.isFiring = False

    def physics(self):
        for enemy in self.game_objects[1:]:
            if self.player.rect.colliderect(enemy.rect):
                print("Taking Damage!")
                self.player.take_damage()
                self.game_objects.remove(enemy)
                print("enemies left: \t" + str(len(self.game_objects[1:])))

        i = 0
        for enemy in self.game_objects[1:]:
            j = 0
            for otherGameObject in self.game_objects[1:]:
                if isinstance(otherGameObject, Enemy) and isinstance(enemy, Projectile):
                    if enemy.rect.colliderect(otherGameObject.rect):
                        print("TARGET HIT")
                        self.game_objects.remove(otherGameObject)
                        self.game_objects.remove(enemy)
                        print("enemies left: \t" + str(len(self.game_objects[1:])))
                j += 1
            i += 1

        for projectile in self.game_objects[1:]:
            if isinstance(projectile, Projectile):
                if not self.game_screen_height > projectile.position[1] > 128:
                    self.game_objects.remove(projectile)