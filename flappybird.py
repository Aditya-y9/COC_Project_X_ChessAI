import pygame as p
import sys
import time
p.init()


class Game:
    running = True
    

    def __init__(self):
        # setting window configs
        self.width = 600
        self.height = 650
        self.scale = 1.5
        # surface screen
        self.screen = p.display.set_mode((self.width, self.height))
        self.speed = 10
        self.Bgandground()

        # making a clock obj
        self.clock = p.time.Clock()

        # ye line 60 fps pe apne loop chalane bolegi computer ko
        # jyada load nahi aayega program run karneka cpu pe
        self.clock.tick(60)






        p.display.update()
        self.gameloop()
        self.running = True

    def gameloop(self):
        # delta time is time between last and first frame
        # to get the time before starting the loop

        # ye function iss moment ka time dega
        # LAST TIME KI INITIAL VALUE MILNE KE LIYE
        last_time = time.time()
        
        while self.running:
                # to get time after starting the loop
            
            # ye function 'abhi kitna time hua?' ye dega
            new_time = time.time()
            #DELTA TIME
            dt = new_time - last_time
            # AB ISKA NEW TIME = AGLE KE LIYE LAST TIME
            last_time = new_time

            # taking events form event.get through a for loop
            for event in p.event.get():
                # is a QUIT event appears ,user clicks the x button
                if event.type==p.QUIT:
                    p.quit()
                    # to stop the program
                    sys.exit()
                    self.running = False
            self.moves(dt)
            self.draws()
            p.display.update()

    
    def moves(self, dtime):
        # move ground , matlab move uska rectangle
        # which axis, toh x axis
        # jitna do loops ke bich time lagega utna woh khasakte jaayega
         self.ground1Rect.x -= self.speed*(dtime)
         self.ground2Rect.x -= self.speed*(dtime)
# jab ye corner right wala bahar gya <0 toh woh screen ka rectangle screen ke bahar gya
         if self.ground1Rect.right < 0:
              # toh uthake wapis rakhdo
              self.ground1Rect.x = self.ground2Rect.right
         if self.ground2Rect.right < 0:
              self.ground2Rect.x = self.ground1Rect.right
         
              

        # jab woh rectangle screen ke bahar jaane lagega left side se,
        # toh,
        





    def draws(self):
         # to project one surface on another

            # destination surface.blit(source_surface, co-ordinates of topleft corner of surface)
            self.screen.blit(self.bg_img,(0,0))

            #  blit karna   (kya? ,        kiske upar?)
            self.screen.blit(self.ground1,self.ground1Rect)

            #blit karna h cause woh image rectangle ke saath chalni chaiye.
            self.screen.blit(self.ground2, self.ground2Rect)

            p.display.update()

    def Bgandground(self):
        # transform .scale to scale images  (image to be loaded, (kitna size ho jana chaiye))

        # to adjust surface             # to make surface
        self.bg_img = p.transform.scale(p.image.load("bg.png").convert(), (self.width, self.height))
        # making two grounds to move them as the game is running
        self.ground1 = p.transform.scale(p.image.load("ground.png").convert(),(self.width,self.height))
        self.ground2 = p.transform.scale_by(p.image.load("ground.png").convert(),self.scale)
        # loading images and adjusting them to screen
        # setting scale to fit image
        
        #using a rectangle to place images
        # make a imaginary rectangle around the images
        # while moving the images
        self.ground1Rect = self.ground1.get_rect()
        self.ground2Rect = self.ground2.get_rect()
        # this is a rectangle stored in the variables


        #  -[1][2]
        self.ground1Rect.x = 0
        # we want the 2nd image to come immedediately after first
        # so we put 2nd image after the end of first

        # yeh wali image pehle wali ke just piche banegi
        self.ground2Rect.x = self.ground1Rect.right


        # dono ka y toh same rahega
        self.ground1Rect.y = 568
        self.ground2Rect.y = 568




game = Game()

