import sys
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((300, 200))
screen.fill((255, 255, 255))
f1 = pygame.font.Font(None, 70) #Создание надписи о оконцании игры
text1 = f1.render('GAME OVER', 1, (0, 0, 0))
f2 = pygame.font.Font(None, 30) #Создание счётчика очков
points = 0
pocoun = f2.render(str(points), 1, (255, 0, 0))

m = pygame.image.load("0.png") #Инициализация слайдов анимации
l1 = pygame.image.load("l1.png")
l2 = pygame.image.load("l2.png")
l3 = pygame.image.load("l3.png")
l4 = pygame.image.load("l4.png")
l5 = pygame.image.load("l5.png")
r1 = pygame.image.load("r1.png")
r2 = pygame.image.load("r2.png")
r3 = pygame.image.load("r3.png")
r4 = pygame.image.load("r4.png")
r5 = pygame.image.load("r5.png")

clock = pygame.time.Clock() #Создание обекта кол-ва кадров

x = 90 #Координаты игрока
y = 60
xp = 180 #Координаты убийственой чёрной точки
yp = 180
xs = random.randint(0, 300) #Координаты хорошей точки
ys = random.randint(0, 200)
i = 1 #Костыль для отображения слайдов анимации

while True: #Костыль что бы остановить игру и вывести надпись смерти
    while abs(x - xp + 10) > 10 or abs(y - yp + 15) > 15: #Создания условия - пока игрок далеко от точки
        pygame.draw.circle(screen, (255, 0, 0), (xs, ys), 7) #Отображение хоршей точки
        screen.blit(pocoun, (260, 10)) #Отображение счётчика очков
        pygame.draw.circle(screen, (255, 255, 255), (xp, yp), 5) #Костыль что бы точка не оставляла чиркаш
        screen.blit(m, (x, y)) #Отображение игрока

        if abs(x - xs + 10) < 15 and abs(y - ys + 15) < 20: #Сбор хороших точек
            points += 1
            xs = random.randint(0, 300)
            ys = random.randint(0, 200)
            pocoun = f2.render(str(points), 1, (255, 0, 0))
            

        if xp - x > 10: #ИИ для расчёта плохо точкой координат до игрока
            xp -= 5
        if xp - x < 10:
            xp += 5
        if yp - y < 15:
            yp += 5
        if yp - y > 15:
            yp -= 5
        pygame.draw.circle(screen, (0, 0, 0), (xp, yp), 5)

        for event in pygame.event.get():#Закрытие игры
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN: #Если нажата клавиша
            if event.key == pygame.K_LEFT: #Если эта клавиша вниз
                x -= 10 
                if x < -10: #Это что бы через стены ходить
                    x = 310   
                screen.fill((255, 255, 255))                        #Отрисока всего ещё раз
                pygame.draw.circle(screen, (0, 0, 0), (xp, yp), 5)
                screen.blit(pocoun, (260, 10))
                pygame.draw.circle(screen, (255, 0, 0), (xs, ys), 7)
                if i == 1:                   #Анимация
                    screen.blit(l1, (x, y))
                elif i == 2:
                    screen.blit(l2, (x, y))
                elif i == 3:
                    screen.blit(l3, (x, y))
                elif i == 4:
                    screen.blit(l4, (x, y))
                elif i == 5:
                    screen.blit(l5, (x, y))
                i += 1
                if i == 5:
                    i = 1

            if event.key == pygame.K_RIGHT: #Тут всё так же
                x += 10
                if x > 310:
                    x = -10
                screen.fill((255, 255, 255))
                pygame.draw.circle(screen, (0, 0, 0), (xp, yp), 5)
                screen.blit(pocoun, (260, 10))
                pygame.draw.circle(screen, (255, 0, 0), (xs, ys), 7)
                if i == 1:
                    screen.blit(r1, (x, y))
                elif i == 2:
                    screen.blit(r2, (x, y))
                elif i == 3:
                    screen.blit(r3, (x, y))
                elif i == 4:
                    screen.blit(r4, (x, y))
                elif i == 5:
                    screen.blit(r5, (x, y))
                i += 1
                if i == 5:
                    i = 1

            if event.key == pygame.K_UP: #Тут так же, но без анимации
                y -= 10
                if y < -20:
                    y = 210
                screen.fill((255, 255, 255))
                pygame.draw.circle(screen, (0, 0, 0), (xp, yp), 5)
                screen.blit(pocoun, (260, 10))
                screen.blit(m, (x, y))
                pygame.draw.circle(screen, (255, 0, 0), (xs, ys), 7)

            if event.key == pygame.K_DOWN:
                y += 10
                if y > 200:
                    y = -30
                screen.fill((255, 255, 255))
                pygame.draw.circle(screen, (0, 0, 0), (xp, yp), 5)
                screen.blit(pocoun, (260, 10))
                screen.blit(m, (x, y))
                pygame.draw.circle(screen, (255, 0, 0), (xs, ys), 7)

        pygame.display.flip() #Обновление экрана
        clock.tick(10) #Кол-во обновлений
    screen.blit(text1, (0, 70)) #Отрисовка надписи смерти
    pygame.display.flip()
    for event in pygame.event.get(): #И ещё одно закрытие окна
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
