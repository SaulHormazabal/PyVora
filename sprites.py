#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import pygame
import random
import config
import graphics

class Food(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = graphics.load_image('images/food.png', True)
        self.rect = self.image.get_rect()

        x = random.randint(2 , config.blocks[0] - 2 )
        y = random.randint(2 , config.blocks[1] - 2 )

        self.rect.left = x * config.scale
        self.rect.top = y * config.scale


    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Worm(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = graphics.load_image('images/block.png')
        self.rect = self.image.get_rect()

        self.speed = [ 1 , 1 ]

        self.rect.left = config.blocks[0] / 2 * config.scale
        self.rect.top = config.blocks[1] / 2 * config.scale

        self.length = 1
        self.grow_to = 5
        self.vx = 0
        self.vy = -1
        self.body = []
        self.crashed = False


    def eat(self):
        self.grow_to += 1


    def moveUp(self):
        if self.vx != 0 and self.vy != 1:
            self.vx = 0
            self.vy = -1


    def moveDown(self):
        if self.vx != 0 and self.vy != -1:
            self.vx = 0
            self.vy = 1


    def moveLeft(self):
        if self.vx != 1 and self.vy != 0:
            self.vx = -1
            self.vy = 0


    def moveRight(self):
        if self.vx != -1 and self.vy != 0:
            self.vx = 1
            self.vy = 0


    def update(self, time):
        """ Move the worm. """

        self.rect.left += self.speed[0] * self.vx * config.scale
        self.rect.top  += self.speed[1] * self.vy * config.scale

        if (self.rect.left, self.rect.top) in self.body:
            self.crashed = True

        self.body.insert(0, (self.rect.left, self.rect.top))

        if (self.grow_to > self.length):
            self.length += 1

        if len(self.body) > self.length:
            self.body.pop()


    def draw(self, screen):
        for x, y in self.body:
            screen.blit(self.image, (x, y))
