import pygame, sys, time
from bullet import Bullet
from ino import Ino


WIDTH = 600
HEIGHT = 800


def events(screen, gun, bullet):
    """Обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_RIGHT:
                gun.m_right = True
            # влево
            elif event.key == pygame.K_LEFT:
                gun.m_left = True
            # огонь
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullet.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_RIGHT:
                gun.m_right = False
            # влево
            elif event.key == pygame.K_LEFT:
                gun.m_left = False


def update_screen(bg_color, screen, stats, sc, gun, inos, bullets):
    """Обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    # life.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, inos, bullets):
    """Обновляем позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullets)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_life()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def create_army(screen, inos):
    """Создание армии пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((WIDTH - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((HEIGHT - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 5):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)


def update_inos(stats, screen, sc, gun, inos, bullets):
    """Обновляет позицию пришельцев"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)


def inos_check(stats, screen, sc, gun, inos, bullets):
    """Добралась ли армия до границы экрана?"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break


def gun_kill(stats, screen, sc, gun, inos, bullets):
    """Столкновение пушки и армии"""
    if stats.guns_life > 0:
        stats.guns_life -= 1
        sc.image_life()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.update_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def check_high_score(stats, sc):
    """Проверка на рекорд"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore', 'w') as f:
            f.write(str(stats.high_score))


def life_count(stats, screen, life):
    """Счётчик жизней"""