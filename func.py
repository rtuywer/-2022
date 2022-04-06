import pygame
from pygame.draw import *
from math import *

pygame.init()

FPS = 200
screen = pygame.display.set_mode((500, 500))
screen.fill((128,128,128))

ginger = (200, 115, 5)
def smile():
    circle(screen, (255, 255, 0), (250, 250), 100)
    circle(screen, (255, 0, 0), (200, 210), 20)
    circle(screen, (255, 0, 0), (300, 210), 15)
    circle(screen, (0, 0, 0), (200, 210), 10)
    circle(screen, (0, 0, 0), (300, 210), 7)
    rect(screen, (0, 0, 0), (200, 290, 100, 20))
    polygon(screen, (0, 0, 0), [(230,210), (240,200),(150,120), (140,130)])
    polygon(screen, (0, 0, 0), [(280,210), (272,200),(340,150), (348,160)])

def draw_ellipse_angle(surface, color, rect, angle, width=0):  # функция поворота эллипса (взята с стаковерфлоу)
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))


def window(x, y, i, screen):  # рисует окно с параметрами
    i = i / 10
    x0 = 415
    y0 = 10
    x1 = - x0 * i + x
    y1 = - y0 * i + y
    rect(screen, (55, 208, 208), (415 * i + x1, 10 * i + y1, 375 * i, 325 * i))  # стекло
    rect(screen, (210, 250, 250), (415 * i + x1, 10 * i + y1, 375 * i, 325 * i), 20)  # рама 1
    line(screen, (210, 250, 250), (415 * i + x1, 130 * i + y1), (785 * i + x1, 130 * i + y1), 15)  # рама 2
    line(screen, (210, 250, 250), (600 * i + x1, 10 * i + y1), (600 * i + x1, 325 * i + y1), 15)  # рама 3


def cat(x, y, i, screen, color):  # рисует кота с параметрами
    i = i / 10
    x0 = 20
    y0 = 370
    x1 = - x0 * i + x
    y1 = - y0 * i + y

    draw_ellipse_angle(screen, color, [563 * i + x1, 360 * i + y1, 250 * i, 80 * i], 30, 0)  # хвост
    draw_ellipse_angle(screen, (0, 0, 0), [563 * i + x1, 360 * i + y1, 250 * i, 80 * i], 30, 1)

    ellipse(screen, color, (100 * i + x1, 360 * i + y1, 530 * i, 165 * i))  # тело
    ellipse(screen, (0, 0, 0), (100 * i + x1, 360 * i + y1, 530 * i, 165 * i), 1)

    ellipse(screen, color, (60 * i + x1, 430 * i + y1, 60 * i, 65 * i))  # лапа под головой
    ellipse(screen, (0, 0, 0), (60 * i + x1, 430 * i + y1, 60 * i, 65 * i), 1)

    ellipse(screen, color, (20 * i + x1, 375 * i + y1, 220 * i, 110 * i))  # голова
    ellipse(screen, (0, 0, 0), (20 * i + x1, 375 * i + y1, 220 * i, 110 * i), 1)

    ellipse(screen, color, (130 * i + x1, 480 * i + y1, 130 * i, 50 * i))  # лапа передняя
    ellipse(screen, (0, 0, 0), (130 * i + x1, 480 * i + y1, 130 * i, 50 * i), 1)

    ellipse(screen, color, (450 * i + x1, 425 * i + y1, 180 * i, 115 * i))  # лапа задняя (бедро)
    ellipse(screen, (0, 0, 0), (450 * i + x1, 425 * i + y1, 180 * i, 115 * i), 1)

    ellipse(screen, color, (607 * i + x1, 480 * i + y1, 50 * i, 90 * i))  # лапа задняя (бедро)
    ellipse(screen, (0, 0, 0), (607 * i + x1, 480 * i + y1, 50 * i, 90 * i), 1)

    polygon(screen, color,
            [(x, y), (63 * i + x1, 392 * i + y1), (30 * i + x1, 410 * i + y1)])  # левое ухо снаружи
    polygon(screen, (0, 0, 0), [(x, y), (63 * i + x1, 392 * i + y1), (30 * i + x1, 410 * i + y1)], 1)

    polygon(screen, (250, 180, 240),
            [(27 * i + x1, 377 * i + y1), (55 * i + x1, 392 * i + y1), (34 * i + x1, 403 * i + y1)])  # левое ухо внутри
    polygon(screen, (0, 0, 0), [(27 * i + x1, 377 * i + y1), (55 * i + x1, 392 * i + y1), (34 * i + x1, 403 * i + y1)],
            1)

    polygon(screen, color, [(210 * i + x1, 355 * i + y1), (197 * i + x1, 395 * i + y1),
                                    (160 * i + x1, 382 * i + y1)])  # правое ухо снаружи
    polygon(screen, (0, 0, 0),
            [(210 * i + x1, 355 * i + y1), (197 * i + x1, 395 * i + y1), (160 * i + x1, 382 * i + y1)], 1)

    polygon(screen, (250, 180, 240), [(202 * i + x1, 363 * i + y1), (192 * i + x1, 388 * i + y1),
                                      (172 * i + x1, 381 * i + y1)])  # правое ухо внутри
    polygon(screen, (0, 0, 0),
            [(202 * i + x1, 363 * i + y1), (192 * i + x1, 388 * i + y1), (172 * i + x1, 381 * i + y1)], 1)

    ellipse(screen, (114, 158, 47), (55 * i + x1, 410 * i + y1, 55 * i, 40 * i))  # левый глаз
    ellipse(screen, (0, 0, 0), (55 * i + x1, 410 * i + y1, 55 * i, 40 * i), 1)

    ellipse(screen, (114, 158, 47), (150 * i + x1, 410 * i + y1, 55 * i, 40 * i))  # правый глаз
    ellipse(screen, (0, 0, 0), (150 * i + x1, 410 * i + y1, 55 * i, 40 * i), 1)

    ellipse(screen, (0, 0, 0), (85 * i + x1, 410 * i + y1, 10 * i, 40 * i))  # левый зрачок

    ellipse(screen, (0, 0, 0), (180 * i + x1, 410 * i + y1, 10 * i, 40 * i))  # правый зрачок

    draw_ellipse_angle(screen, (255, 255, 255), [73 * i + x1, 410 * i + y1, 8 * i, 20 * i], 220, 0)  # левый блик

    draw_ellipse_angle(screen, (255, 255, 255), [168 * i + x1, 410 * i + y1, 8 * i, 20 * i], 220, 0)  # правый блик

    polygon(screen, (250, 180, 240),
            [(127 * i + x1, 450 * i + y1), (139 * i + x1, 450 * i + y1), (127 * i + x1, 457 * i + y1),
             (115 * i + x1, 450 * i + y1)])  # нос
    polygon(screen, (0, 0, 0),
            [(127 * i + x1, 450 * i + y1), (139 * i + x1, 450 * i + y1), (127 * i + x1, 457 * i + y1),
             (115 * i + x1, 450 * i + y1)], 1)

    line(screen, (0, 0, 0), (127 * i + x1, 457 * i + y1), (127 * i + x1, 467 * i + y1), 1)

    arc(screen, (0, 0, 0), [127 * i + x1, 462 * i + y1, 16 * i, 10 * i], pi, 15 * pi / 8)  # рот
    arc(screen, (0, 0, 0), [111 * i + x1, 462 * i + y1, 16 * i, 10 * i], pi, 15 * pi / 8)

    # усы
    arc(screen, (0, 0, 0), [-80 * i + x1, 444 * i + y1, 700 * i, 500 * i], 1.55, 1.9)
    arc(screen, (0, 0, 0), [-78 * i + x1, 455 * i + y1, 700 * i, 200 * i], 1.55, 1.9)
    arc(screen, (0, 0, 0), [-145 * i + x1, 463 * i + y1, 700 * i, 200 * i], 1.3, 1.7)

    arc(screen, (0, 0, 0), [-375 * i + x1, 440 * i + y1, 700 * i, 500 * i], 1.2, 1.65)
    arc(screen, (0, 0, 0), [-410 * i + x1, 448 * i + y1, 700 * i, 200 * i], 1.1, 1.5)
    arc(screen, (0, 0, 0), [-345 * i + x1, 460 * i + y1, 700 * i, 200 * i], 1.3, 1.75)


def ball(x, y, i, screen):  # рисует клубок с параметрами
    i = i / 10
    x0 = 400
    y0 = 560
    x1 = - x0 * i + x
    y1 = - y0 * i + y

    ellipse(screen, (180, 180, 180), (400 * i + x1, 560 * i + y1, 135 * i, 100 * i))  # клубок
    ellipse(screen, (0, 0, 0), (400 * i + x1, 560 * i + y1, 135 * i, 100 * i), 1)
    arc(screen, (0, 0, 0), (420 * i + x1, 570 * i + y1, 100 * i, 75 * i), 0, pi / 2)
    arc(screen, (0, 0, 0), (405 * i + x1, 580 * i + y1, 100 * i, 50 * i), 0, pi / 2)
    arc(screen, (0, 0, 0), (325 * i + x1, 590 * i + y1, 185 * i, 100 * i), 0, pi / 2)
    arc(screen, (0, 0, 0), (430 * i + x1, 600 * i + y1, 80 * i, 80 * i), 2 * pi / 3, pi)
    arc(screen, (0, 0, 0), (450 * i + x1, 610 * i + y1, 80 * i, 80 * i), 2 * pi / 3, pi)

    arc(screen, (180, 180, 180), (310 * i + x1, 590 * i + y1, 300 * i, 60 * i), pi, 3 * pi / 2)  # нить
    arc(screen, (180, 180, 180), (160 * i + x1, 600 * i + y1, 150 * i, 40 * i), 0, pi)


def big_cat():  # рисует стандартных окно, кота и клубок (задание 2)
    screen = pygame.display.set_mode((800, 700))
    screen.fill((95, 80, 30))
    rect(screen, (140, 120, 50), (0, 350, 800, 350))  # стол
    window(415, 10, 10, screen)  # окно
    cat(20, 370, 10, screen, ginger)  # кот
    ball(400, 560, 10, screen)  # клубок

def many_cats():  #  рисует картину с множеством котов (задание 3)
    screen = pygame.display.set_mode((800, 700))
    screen.fill((95, 80, 30))
    rect(screen, (140, 120, 50), (0, 350, 800, 350))  # стол
    window(415, 10, 10, screen)
    window(10, 10, 10, screen)
    ball(20, 370, 10, screen)
    ball(50, 450, 3, screen)
    ball(280, 550, 4, screen)
    ball(111, 650, 4, screen)
    ball(350, 500, 3, screen)
    ball(550, 370, 6, screen)
    cat(20, 370, 2, screen, ginger)
    cat(50, 450, 3, screen, ginger)
    cat(100, 600, 2, screen, ginger)
    cat(350, 370, 3, screen, ginger)
    cat(700, 370, 2, screen, ginger)
    cat(450, 560, 4, screen, ginger)






def ready():
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()