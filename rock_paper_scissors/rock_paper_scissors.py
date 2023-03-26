import cv2
import pygame
from pygame.locals import *
import tkinter as tk
from PIL import Image, ImageTk
# img = cv2.imread("Assets/rock.png")

# cv2.imshow('Image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

def on_click(event=None):
    # `command=` calls function without argument
    # `bind` calls function with one argument
    print("image clicked")

pygame.init()
init = tk.Tk()

rarm = pygame.image.load("Assets/rock.png")
rarm_location = rarm.get_rect(center=(100.100,300))

larm = pygame.image.load("Assets/Leftrock.png")
larm_location = larm.get_rect(center=(500,300))

rockico = pygame.image.load("Assets/Rockico.png")
rockico_location = rockico.get_rect(center=(100.400,500.500))
paperico = pygame.image.load("Assets/Paperico.png")
paperico_location = paperico.get_rect(center=(300.400,500.500))
scissorico = pygame.image.load("Assets/Scissorico.png")
scissorico_location = scissorico.get_rect(center=(500.400,500.500))


photo = ImageTk.PhotoImage(rockico)

rocklab = tk.Label(init, rockico=photo)
rocklab.pack()

rocklab.bind('<Button-1>', on_click)

rockbut = tk.Button(init, rockico=photo, command=on_click)
rockbut.pack

rockbut = tk.Button(init, command=init.destroy)
rockbut.pack

init.mainloop()

running = True

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))
pygame.display.update()
pygame.display.set_caption("Rock Paper Scissors")

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.blit(rarm, rarm_location)
    screen.blit(larm, larm_location)
    screen.blit(rockico, rockico_location)
    screen.blit(paperico, paperico_location)
    screen.blit(scissorico, scissorico_location)
    pygame.display.update()
pygame.quit()