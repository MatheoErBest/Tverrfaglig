import pymysql
import pygame
import random

# Initialiserer pygame
pygame.init()

# Definerer vindusstørrelsen
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Lager vinduet til programet
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setter opp hoved løøka til spillet
running = True
while running:
    # Hører etter hendelser
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tegner bakgrunnen
    win.fill(WHITE)

    # Oppdaterer vinduet
    pygame.display.update()

# Lukker programmet
pygame.quit()
