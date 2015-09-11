# -*- encoding: utf-8 -*-

# Módulos
import pygame
import config

class Director:

    def __init__(self):
        
        self.surface = pygame.display.set_mode((config.width, config.height))
        pygame.display.set_caption(config.name)
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()

    def loop(self):

        while not self.quit_flag:
            self.time = self.clock.tick(16)

            # Eventos de Salida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            # detecta eventos
            self.scene.on_event()
 
            # actualiza la escena
            self.scene.on_update()

            # dibuja la pantalla
            self.scene.on_draw(self.surface)
            pygame.display.flip()

    def change_scene(self, scene):
        self.scene = scene
 
    def quit(self):
        self.quit_flag = True
