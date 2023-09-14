import pygame as p
p.init()

# create window          ((width,height))
screen = p.display.set_mode((800,600))
p.display.update()



running  = True
while running:
    p.display.update()
    for event in p.event.get():
        if event.type  == p.QUIT:
            running = False






# opposite of pygame.init()
pygame.quit() 

