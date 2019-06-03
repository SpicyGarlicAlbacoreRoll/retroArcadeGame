import pygame
import random


class GameManager:

    def __init__(self, game_objects, game_screen):
        self.game_objects = game_objects
        self.player = game_objects[0]
        self.game_screen_width = game_screen[0]
        self.game_screen_height = game_screen[1]

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def update(self, dt):
        for game_object in self.game_objects:
            game_object.update(dt)
        self.physics()

    def draw(self, game_screen):
        for game_object in self.game_objects:
            game_object.draw(game_screen)

    def physics(self):
        for enemy in self.game_objects[1:]:
            if self.player.rect.colliderect(enemy.rect):
                print("THAT'S A HIT")
                # print("colliding")
                self.player.position[0] = 100
                self.player.position[1] = 150

                enemy.position[1] = 10
                enemy.position[0] = random.randint(0, self.game_screen_width)
