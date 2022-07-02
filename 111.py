import pygame
import random
pygame.init()
#разрешение экрана
size_X = 1024
size_Y = 760

display = pygame.display.set_mode((size_X, size_Y))

#настройки окна(ярлык и название соответсвенно)
pygame.display.set_caption('i don\'t know')
icon = pygame.image.load('123.jpg')
pygame.display.set_icon(icon)
#время
clock = pygame.time.Clock()


#персонаж
rost = 64
shir = 64
user_x = 200
user_y = 300
ship = pygame.image.load('ship12.png')




#=========================main===============================
def run_game():
    game = True
    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        move()
        drawing()
        shipp()


#функция описывающая движение персонажа
def move():
    global user_x, user_y, size_X , size_Y
    speed = 9
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        user_x -= speed
        if user_x < 0:
            user_x = 3
    if keys[pygame.K_d]:
        user_x += speed
        if user_x > size_X - shir:
            user_x = size_X - shir - 3
    if keys[pygame.K_w]:
        user_y -= speed
        if user_y < 0:
            user_y = 3
    if keys[pygame.K_s]:
        user_y += speed
        if user_y > size_Y - rost:
            user_y = size_Y - rost - 3
    if keys[pygame.K_ESCAPE]:
        pause()


#бесконечный цикл паузы
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('pause.press enter to play ', 275, 350)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        drawing()
        shipp()


#функция отрисовки фона
def drawing():
    space = pygame.image.load('space13.jpg')
    display.blit(space, (0, 0))
    pygame.display.update()
    clock.tick(100)


#ртрисовка корабля
def shipp():
    global ship
    display.blit(ship, (user_x, user_y))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(100)


#текс во время паузы
def print_text(massege, x, y, font_color=(110, 155, 55), font_type='6600.ttf', font_size=40):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(massege, True, font_color)
    display.blit(text, (x, y))
    pygame.display.update()
    clock.tick(10)

run_game()