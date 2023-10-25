import pygame
import random
import os
from pygame.locals import *
from sys import exit
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640,480),0,32)#create game window
pygame.display.set_caption("Snakes_With_Rohan")#Set the title
snake_size = 15 # length & width of snake
clock = pygame.time.Clock() # create a clock
font = pygame.font.Font(None,25) # Features of font of txt
def plot_snake(screen,color,snake_list,snake_size):
    for x,y in snake_list :
        pygame.draw.rect(screen,color,[x,y,snake_size,snake_size])

def text_screen(text,color,x,y): # to display txt
    screen_text = font.render(text,True,color)
    screen.blit(screen_text,(x,y))
def welcome():
    while True:
        initial = pygame.image.load(r"C:\Users\parab\OneDrive\Pictures\Saved Pictures\initial.jpg").convert_alpha()

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    game_loop()
        screen.blit(initial,(0,0))
        pygame.display.update()
        clock.tick(30)
def game_loop():
    snake_x = 45  # init x & y pos of snake
    snake_y = 30
    fps = 30  # frame per second
    velocity_x = 0  # velocities of snake in x & y
    velocity_y = 0
    init_vel = 5  # initial velocity
    score = 0  # initial score
    food_x = random.randint(20, 640 // 2)  # init x & y pos of food
    food_y = random.randint(20, 480 // 2)
    snake_length = 1
    if (not os.path.exists("Highscore.txt")): # Check if the file exists or not
        file = open("Highscore.txt",'w')
        file.write("0")
        file.close()
    file = open("Highscore.txt", 'r')
    highscore = file.read()
    file.close()
    print("Highscore : ",highscore)
    snake_list = []
    game_over = False
    exit_game = False
    while not exit_game: # game loop
        if game_over:
            screen.fill((255,255,255))
            text_screen("OOPS ! GAME OVER ! PRESS ENTER TO CONTINUE",(255,0,0),50,50)
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_KP_ENTER or event.key == K_RETURN :
                        welcome()
        else:
            for event in pygame.event.get():  # event loop
                if event.type == QUIT:  # clicked on close btn
                    exit()
                elif event.type == KEYDOWN:  # Movement in all dir
                    if event.key == K_RIGHT:
                        velocity_x = init_vel
                        velocity_y = 0
                    elif event.key == K_LEFT:
                        velocity_x = -init_vel
                        velocity_y = 0
                    elif event.key == K_UP:
                        velocity_y = -init_vel
                        velocity_x = 0
                    elif event.key == K_DOWN:
                        velocity_y = init_vel
                        velocity_x = 0
            snake_x += velocity_x
            snake_y += velocity_y
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                food_x = random.randint(20, 640 // 2)  # replotting x & y pos of food
                food_y = random.randint(20, 480 // 2)
                snake_length += 2
                if score > int(highscore):
                    highscore = score
                    file = open("Highscore.txt",'w')
                    file.write(str(highscore))
                    file.close()
            screen.fill((255, 255, 255))  # RGB code for white
            text_screen("Score : " + str(score) + " Highscore : "+ str(highscore), (255, 0, 0), 5, 5)
            pygame.draw.rect(screen, (255, 0, 0),[food_x, food_y, snake_size, snake_size])  # RGB code for red # dim of food same as snake
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load(r"C:\Users\parab\Music\game_over.wav")
                pygame.mixer.music.play()
            if snake_x < 0 or snake_y < 0 or snake_x > 640 or snake_y > 480:
                game_over = True
                pygame.mixer.music.load(r"C:\Users\parab\Music\game_over.wav")
                pygame.mixer.music.play()
            plot_snake(screen,(0, 0, 0),snake_list,snake_size)  # RGB code for black
        pygame.display.update()
        clock.tick(fps) # to update the game frame with time
    exit()
welcome()
