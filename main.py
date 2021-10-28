""" Space invaders v 0.0.2 |  """
import pygame, controller
from gun import Gun
from pygame.sprite import Group
from controller import WIDTH, HEIGHT
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Космические защитники')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controller.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)
    # life = Life(screen)

    while True:
        controller.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controller.update_bullets(screen, stats, sc, inos, bullets)
            controller.update_screen(bg_color, screen, stats, sc, gun, inos, bullets)
            controller.update_inos(stats, screen, sc, gun, inos, bullets)


run()
