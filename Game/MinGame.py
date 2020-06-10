import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))    #设置窗体大小
pygame.display.set_caption("PyGame最小开发框架")    #设置窗体名字

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update() #刷新屏幕