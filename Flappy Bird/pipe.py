import pygame as p
import random

class Pipe:
    def __init__(self, scale_factor, move_speed):
        # load and adjust and convert to make them transperant
        self.img_up = p.transform.scale(p.image.load(r"C:\Users\MSHOME\Desktop\New folder\COC_Project_X_ChessAI\flappy-bird-pygame\Flappy Bird\pipeup.png").convert_alpha(), (int(52 * scale_factor), int(320 * scale_factor)))
        self.img_down = p.transform.scale(p.image.load(r"C:\Users\MSHOME\Desktop\New folder\COC_Project_X_ChessAI\flappy-bird-pygame\Flappy Bird\pipedown.png").convert_alpha(), (int(52 * scale_factor), int(320 * scale_factor)))

        # Create rectangular boxes for placing
        self.rect_up = self.img_up.get_rect()
        self.rect_down = self.img_down.get_rect()

        # game hard karne ke liye
        self.pipe_distance = 200

        
        # for one pipe make random and calculate for other pipe
        self.rect_up.y = random.randint(100, 500)
        self.rect_up.x = 600

        # Calculate
        self.rect_down.y = self.rect_up.y - self.pipe_distance - self.rect_up.height
        self.rect_down.x = 600

        # wahi speed
        self.move_speed = move_speed

    def drawPipe(self, win):
        # blit the pipes
        win.blit(self.img_up, self.rect_up)
        win.blit(self.img_down, self.rect_down)

    def update(self, dt):
        # Update
        self.rect_up.x -= int(self.move_speed * dt)
        self.rect_down.x -= int(self.move_speed * dt)
