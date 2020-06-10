import pygame
import sys

pygame.init()
size = width, height = 600, 400    #设置窗体大小
spped = [1,1]
BLACK = 0,0,0
screen = pygame.display.set_model(size)
pygame.display.set_caption("PyGame壁球")    #设置窗体名字
bail = pygame.image.load("globe.png")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update() #刷新屏幕