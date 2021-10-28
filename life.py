import pygame
from pygame.sprite import Sprite


class Life(Sprite):

    def __init__(self, screen):
        """Инициализация жизней"""
        super(Life, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/life.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.right - 20

    def output(self):
        """Выводим жизни на экран"""
        self.screen.blit(self.image, self.rect)
