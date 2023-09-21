import pygame
import time
import random
 
pygame.init()
 
display = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("courier", 25)
 
def UpdateScore(score):
    value = font_style.render("Your score: " + str(score), True, (255, 255, 180))
    display.blit(value, [0, 0])


def Snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, (0, 250, 0), [x[0], x[1], snake_block, snake_block])


def Message(message, color):
    msg = font_style.render(message, True, color)
    display.blit(msg, [80, 110])


def gameLoop():
    game_over = False
    game_close = False
 
    x1 = 300
    y1 = 200
    x1_change = 0
    y1_change = 0
 
    snake_list = []
    length_of_snake = 1
 
    foodx = round(random.randrange(0, 590) / 10.0) * 10.0
    foody = round(random.randrange(0, 390) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            display.fill((0, 0, 0))
            Message("Press P(play again) or Q(quit)", (252, 20, 20))
            UpdateScore(length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = 10
                    x1_change = 0
 
        if x1 >= 600 or x1 < 0 or y1 >= 400 or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill((0, 0, 0))
        pygame.draw.rect(display, (252, 60, 90), [foodx, foody, 10, 10])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
 
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
 
        Snake(10, snake_list)
        UpdateScore(length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, 590) / 10.0) * 10.0
            foody = round(random.randrange(0, 390) / 10.0) * 10.0
            length_of_snake += 1
 
        clock.tick(15)
 
    pygame.quit()
 
 
gameLoop()