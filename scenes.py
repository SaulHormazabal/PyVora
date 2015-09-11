# -*- encoding: utf-8 -*-

import pygame
import graphics
import config
import sprites

class Scene:

    def __init__(self, director):
        self.director = director

    def on_update(self):
        raise NotImplemented("Not Implemented the method on_update.")

    def on_event(self, event):
        raise NotImplemented("Not Implemented the method on_event.")

    def on_draw(self, surface):
        raise NotImplemented("Not Implemented the method on_draw.")


class Menu(Scene):

    def __init__(self, director):
        Scene.__init__(self, director)

        text = 'Press Enter'
        font = pygame.font.Font( pygame.font.get_default_font() , 24 )
        color = (255, 255, 255)

        self.text = pygame.font.Font.render(font, text, 1, color)

        self.text_rect = self.text.get_rect()
        self.text_rect.centerx = config.width / 2
        self.text_rect.centery = config.height / 2

    def on_update(self):
        pass

    def on_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.director.change_scene(Game(self.director))
        elif keys[pygame.K_ESCAPE]:
            self.director.quit()

    def on_draw(self, surface):
        surface.blit(self.text, self.text_rect)

class Game(Scene):

    def __init__(self, director):
        Scene.__init__(self, director)

        self.background = pygame.Surface( ( config.width , config.height) )
        self.background.fill( ( 187 , 200 , 0) )

        block = graphics.load_image('images/block.png')

        for x in xrange( 0 , config.blocks[0] ):
            self.background.blit( block , ( x * config.scale , 0 ) )
            self.background.blit( block , ( x * config.scale , config.height - config.scale ) )

        for x in xrange( 1 , config.blocks[1] - 1):
            self.background.blit( block , ( 0 , x * config.scale ) )
            self.background.blit( block , ( config.width - config.scale , x * config.scale ) )

        self.score = 0

        self.worm = sprites.Worm()
        self.food = sprites.Food()


    def on_update(self):
        self.time = self.director.time

        self.worm.update(self.time)

        if self.worm.crashed:
            print "crashed"
            self.director.change_scene(Menu(self.director))

        elif self.worm.rect.left < config.scale or self.worm.rect.right > config.width - config.scale:
            self.worm.crashed = True

        elif self.worm.rect.top < config.scale or self.worm.rect.bottom > config.height - config.scale:
            self.worm.crashed = True

        elif self.food.rect.colliderect( self.worm.rect ):
            self.score += 1
            self.worm.eat()
            print "Score: %d" % self.score
            self.food = sprites.Food()


    def on_event(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.worm.moveUp()

        elif keys[pygame.K_DOWN]:
            self.worm.moveDown()

        elif keys[pygame.K_LEFT]:
            self.worm.moveLeft()

        elif keys[pygame.K_RIGHT]:
            self.worm.moveRight()


    def on_draw(self, surface):
        surface.blit(self.background, (0,0))
        self.worm.draw(surface)
        self.food.draw(surface)
