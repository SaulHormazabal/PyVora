# -*- coding: utf-8 -*-

import pygame

def load_image( path , transparent = False , pixel = ( 0 , 0 ) ):

    try:
        image = pygame.image.load(path)

    except pygame.error, message:
        raise SystemExit, message

    image = image.convert()

    if transparent:
            color = image.get_at(pixel)
            image.set_colorkey(color, pygame.RLEACCEL)

    return image


def text_render( text , posx , posy , color = ( 0 , 0 , 0 ) , size = 24 ):

    font = pygame.font.Font( pygame.font.get_default_font() , size )

    surface = pygame.font.Font.render(font, text, 1, color)

    rect = surface.get_rect()

    rect.centerx = posx
    rect.centery = posy

    return surface, rect
