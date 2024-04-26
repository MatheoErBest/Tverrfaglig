import pygame
import pymysql
import sys

# Farger
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Funksjon for å vise popup-vinduet
def show_popup(screen):
    input_box = pygame.Rect(100, 150, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    user_input = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode

        screen.fill((30, 30, 30))
        
        font = pygame.font.Font(None, 24)
        text_surface = font.render("Enter your username:", True, (255, 255, 255))
        screen.blit(text_surface, (100, 100))
        
        txt_surface = pygame.font.Font(None, 32).render(user_input, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

    return user_input



# Funksjon for å sette inn brukernavn i databasen
def insert_username(username, highscore):
    conn = pymysql.connect(
        host='172.20.128.63',
        user='matheo',
        password='123Akademiet',
        database='score',
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO spilldata(id, highscore) VALUES (%s, %s)", (username, highscore))
        conn.commit()
    finally:
        conn.close()

# Display
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Enter Username')


# Funksjon for å starte spillet
def playGame():

    # Definerer vindusstørrelsen
    WINDOW_WIDTH = 1080
    WINDOW_HEIGHT = 700

    # Lager vinduet til programmet
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Farger
    

    # Setter firkantens posisjon og størrelse
    square_x = 100
    square_y = 100
    square_width = 20
    square_height = 20

    # Bevegelseshastighet
    speed = 10

    # Setter opp hovedløkken til spillet
    running = True
    while running:
        # Hører etter hendelser
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
        
        # Håndterer tastetrykk
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            square_y -= speed
        if keys[pygame.K_s]:
            square_y += speed
        if keys[pygame.K_a]:
            square_x -= speed
        if keys[pygame.K_d]:
            square_x += speed
        if keys[pygame.K_ESCAPE]:
            running = False

        # Sørger for at firkanten ikke går utenfor vinduet
        square_x = max(0, min(square_x, WINDOW_WIDTH - square_width))
        square_y = max(0, min(square_y, WINDOW_HEIGHT - square_height))

        # Tegner bakgrunnen
        win.fill(WHITE)

        # Tegner firkanten
        pygame.draw.rect(win, RED, (square_x, square_y, square_width, square_height))

        # Oppdaterer vinduet
        pygame.display.update()

# Display
pygame.init()
clock = pygame.time.Clock()
screenX, screenY = 1080, 700
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption('Super Duper Kul')

# Funksjoner for hovedmenyen
def drawText(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def screenUpdate():
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

def changeRes():
    res = 'liten'

    if res == 'liten':
        screenX, screenY = 1080, 1620
        res = 'stor'
        pygame.display.update()
    
    if res == 'stor':
        screenX, screeny = 900, 1000
        res = 'liten'
        pygame.display.update()

highscore = 300

# Meny verdier
menuItems = ['Start game', 'Options', 'Exit']
selectedItem = 0
in_options_menu = False

# Alternativmeny verdier
optionMenuItems = ['Resolution', 'Sound', 'Controls', 'Back']
selectedOptionItem = 0

keys = pygame.key.get_pressed()
# Hovedløkke for hovedmenyen
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if not in_options_menu:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selectedItem = (selectedItem + 1) % len(menuItems)
                elif event.key == pygame.K_UP:
                    selectedItem = (selectedItem - 1) % len(menuItems)
                elif event.key == pygame.K_RETURN:
                    if selectedItem == 0:
                        # Vis popup-vinduet for å få brukernavnet
                        username = show_popup(screen)

                        # Sett inn brukernavnet i databasen
                        insert_username(username, highscore)
                        playGame()  # Starter spillet når "Start game" er valgt
                    elif selectedItem == 1:
                        in_options_menu = True
                    elif selectedItem == 2:
                        pygame.quit()
                        sys.exit()

        elif in_options_menu:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selectedOptionItem = (selectedOptionItem + 1) % len(optionMenuItems)
                elif event.key == pygame.K_UP:
                    selectedOptionItem = (selectedOptionItem - 1) % len(optionMenuItems)
                elif event.key == pygame.K_RETURN:
                    if selectedOptionItem == 0:
                        changeRes()
                    if selectedOptionItem == 3:  # Back option selected
                        in_options_menu = False
                elif event.key == pygame.K_BACKSPACE:
                    in_options_menu = False
               

    # Tegne menyen
    if not in_options_menu:
        screen.fill((0, 0, 0))
        menu_font = pygame.font.Font(None, 36)
        for i, item in enumerate(menuItems):
            color = (255, 255, 255) if i == selectedItem else (128, 128, 128)
            drawText(item, menu_font, color, screenX // 2, 200 + i * 50)
            drawText("Use UP / Down Arrow Keys To Navigate And Enter To Choose", menu_font, (128, 128, 128), screenX // 2, 400)

    if in_options_menu:
        screen.fill((0, 0, 0))
        sub_menu_font = pygame.font.Font(None, 36)
        for i, item in enumerate(optionMenuItems):
            color = (255, 255, 255) if i == selectedOptionItem else (128, 128, 128)
            drawText(item, sub_menu_font, color, screenX // 2, 200 + i * 50)
            drawText("Press Backspace to go back", sub_menu_font, (128, 128, 128), screenX // 2, 400)

    screenUpdate()

pygame.quit()
sys.exit()
