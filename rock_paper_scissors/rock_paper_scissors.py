import cv2
import pygame
from pygame.locals import *
img = cv2.imread("Assets/rock.png")

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

pygame.init()
running = True

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))
pygame.display.update()
pygame.display.set_caption("Rock Paper Scissors")

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
pygame.quit()