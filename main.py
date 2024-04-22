import pygame

# Initialiserer pygame
pygame.init()

# Definerer vindusstørrelsen
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Lager vinduet til programmet
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Farger
WHITE = (255, 255, 255)
RED = (255, 0, 0)  # Fargen til firkanten

# Setter firkantens posisjon og størrelse
square_x = 100
square_y = 100
square_width = 20
square_height = 20

# Setter opp hovedløkken til spillet
running = True
while running:
    # Hører etter hendelser
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            pass

    # Tegner bakgrunnen
    win.fill(WHITE)

    # Tegner firkanten
    pygame.draw.rect(win, RED, (square_x, square_y, square_width, square_height))

    # Oppdaterer vinduet
    pygame.display.update()

# Lukker programmet
pygame.quit()
