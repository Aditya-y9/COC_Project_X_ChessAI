import pygame as pg
import sys
import time
import random
from pipe import Pipe
from bird import Bird

pg.init()

class Game:
    def __init__(self):
        # setting window config
        self.width = 600
        self.height = 768
        self.scale_factor = 1.5
        self.win = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.move_speed = 250
        self.bird = Bird(self.scale_factor)

        self.is_enter_pressed = False
        self.pipes = []
        self.pipe_generate_counter = 71

        # loading images for bg and ground
        self.bg_img = pg.transform.scale_by(pg.image.load(r"C:\Users\MSHOME\Desktop\New folder\COC_Project_X_ChessAI\flappy-bird-pygame\Flappy Bird\bg.png").convert(),self.scale_factor)
        self.ground_img = pg.transform.scale_by(pg.image.load(r"C:\Users\MSHOME\Desktop\New folder\COC_Project_X_ChessAI\flappy-bird-pygame\Flappy Bird\ground.png").convert(), self.scale_factor)
        self.ground_rect1 = self.ground_img.get_rect()
        self.ground_rect2 = self.ground_img.get_rect()

        self.ground_rect1.x = 0
        self.ground_rect2.x = self.ground_rect1.right
        self.ground_rect1.y = 568
        self.ground_rect2.y = 568
        
        self.gameLoop()

    def gameLoop(self):
        # delta time is time between last and first frame
        # to get the time before starting the loop

        # ye function iss moment ka time dega
        # LAST TIME KI INITIAL VALUE MILNE KE LIYE
        last_time = time.time()

        while True:
            # to get time after starting the loop

            # ye function 'abhi kitna time hua?' ye dega
            new_time = time.time()
            # DELTA TIME
            dt = new_time - last_time
            # AB ISKA NEW TIME = AGLE KE LIYE LAST TIME
            last_time = new_time

            # taking events form event.get through a for loop
            for event in pg.event.get():
                # is a QUIT event appears, user clicks the x button
                if event.type == pg.QUIT:
                    pg.quit()
                    # to stop the program
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.is_enter_pressed = True
                        self.bird.update_on = True
                    if event.key == pg.K_SPACE and self.is_enter_pressed:
                        self.bird.flap(dt)
            self.updateGame(dt)
            self.checkCollisions()
            self.drawGame()
            pg.display.update()
            self.clock.tick(60)

    def checkCollisions(self):
        if len(self.pipes):
            if self.bird.rect.bottom > 568:
                self.bird.update_on = False
                self.is_enter_pressed = False
            if (self.bird.rect.colliderect(self.pipes[0].rect_down) or
                    self.bird.rect.colliderect(self.pipes[0].rect_up)):
                self.is_enter_pressed = False

    def updateGame(self, dt):
        if self.is_enter_pressed:
            # move ground, matlab move uska rectangle
            # which axis, toh x axis
            # jitna do loops ke bich time lagega utna woh khasakte jaayega
            self.ground_rect1.x -= self.move_speed * dt
            self.ground_rect2.x -= self.move_speed * dt

            # jab ye corner right wala bahar gya <0 toh woh screen ka rectangle screen ke bahar gya
            if self.ground_rect1.right < 0:
                # toh uthake wapis rakhdo
                self.ground_rect1.x = self.ground_rect2.right
            if self.ground_rect2.right < 0:
                self.ground_rect2.x = self.ground_rect1.right

            if self.pipe_generate_counter > 70:
                self.pipes.append(Pipe(self.scale_factor, self.move_speed))
                self.pipe_generate_counter = 0

            # moving the pipes
            self.pipe_generate_counter += 1

            for pipe in self.pipes:
                pipe.update(dt)

            # removing pipes if out of screen
            if len(self.pipes) != 0:
                if self.pipes[0].rect_up.right < 0:
                    self.pipes.pop(0)

            # moving the bird
            self.bird.update(dt)

    def drawGame(self):
        self.win.blit(self.bg_img, (0, -300))
        for pipe in self.pipes:
            pipe.drawPipe(self.win)

        # to project one surface on another
        # destination surface.blit(source_surface, co-ordinates of top left corner of surface)
        self.win.blit(self.ground_img, self.ground_rect1)
        self.win.blit(self.ground_img, self.ground_rect2)

        # Draw the bird
        self.win.blit(self.bird.image, self.bird.rect)

if __name__ == "__main__":
    game = Game()

