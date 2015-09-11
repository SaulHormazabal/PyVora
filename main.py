#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import pygame
import director
import scenes

from pygame.locals import *

def main():
    dir = director.Director()
    menu = scenes.Menu(dir)
    dir.change_scene(menu)
    dir.loop()

if __name__ == '__main__':
    pygame.init()
    main()
