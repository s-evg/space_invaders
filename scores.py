import pygame.font
from life import Life
from pygame.sprite import Group


class Scores():
    """Вывод игровой информации"""
    def __init__(self, screen, stats):
        """Инициализация подсчёта очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (76, 175, 79)
        self.font = pygame.font.SysFont(None, 35)
        self.image_score()
        self.image_high_score()
        self.image_life()

    def image_score(self):
        """Преобразовывает текст счёта в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True,
                                          self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = self.screen_rect.left + 510
        self.score_rect.top = 20

    def image_life(self):
        """Количество жизней"""
        self.lifes = Group()
        for gun_number in range(self.stats.guns_life):
            life = Life(self.screen)
            life.rect.x = life.rect.width * gun_number + 10
            life.rect.y = 18
            self.lifes.add(life)

    def image_high_score(self):
        """Преобразует рекорд в графическое изображение"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True,
                                                 self.text_color, (0,0,0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def show_score(self):
        """Вывод счёта на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.lifes.draw(self.screen)


