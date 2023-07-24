import pygame
import time
import random
from time import sleep

pygame.init()

width = 600
height = 400

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Snake')

c = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("calibri", 50)
score_font = pygame.font.SysFont("calibri", 20)

# snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), [x[0], x[1], snake_block, snake_block])


# puntaje
def Puntaje(score):
    value = score_font.render("Tu Puntaje: " + str(score), True, (0, 0, 0))
    screen.blit(value, [0, 0])


# Function to print the message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Function for game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # comida
    comidax = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    comiday = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # juego
    running = True
    while running:

        while game_close == True:
            screen.fill((0, 0, 0))
            message("Perdiste", (255, 0, 0))
            pygame.display.update()
            delay = 2
            sleep(delay)
            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change -= snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change += snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change -= snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change += snake_block
                    x1_change = 0

        # bordes
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill((255, 255, 255))

        # Comida
        pygame.draw.rect(screen, (0, 0, 0), [comidax, comiday, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

       # contra su propio cuerpo
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True


        snake(snake_block, snake_List)
        Puntaje(Length_of_snake - 1)

        pygame.display.update()
    
        if x1 == comidax and y1 == comiday:
            
            comidax = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            comiday = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            
            Length_of_snake += 1

        c.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()