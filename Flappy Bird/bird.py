import pygame as p


# It inherits from the Sprite class to enable specialmoving class sprite functionality
class Bird(p.sprite.Sprite):
    def __init__(self, scale):
        # Initialize the Bird object constructor se
        super(Bird, self).__init__()
        # superclass constructor call karne

        # Load and adjusting and convert_alpha to remove transperant
        self.img_list = [
            p.transform.scale_by(p.image.load(r"C:\Users\MSHOME\Desktop\New folder\COC_Project_X_ChessAI\flappy-bird-pygame\Flappy Bird\birdup.png").convert_alpha(), scale),
            p.transform.scale_by(p.image.load(r"C:\Users\MSHOME\Desktop\New folder\COC_Project_X_ChessAI\flappy-bird-pygame\Flappy Bird\birddown.png").convert_alpha(), scale)
        ]

        # first image first
        self.image_index = 0
        self.image = self.img_list[self.image_index]

        # a rectangle around our object pehle jaisa same
        self.rect = self.image.get_rect(center=(100, 100))

        # Birds physics parameters
        self.y_velocity = 0
        self.gravity = 20  # gravity pull.
        self.flap_speed = 325  # vel rise on enter.
        self.anim_counter = 0  # Counter for animation
        self.update_on = False  # control bird's update

    def update(self, dt):
        # Update the bird's position and animation frame
        if self.update_on:
            self.playAnimation()  # Animate the bird's wings
            self.applyGravity(dt)  # Apply gravity to bird's movement

            # Limit bird's upward movement to prevent it from going above the screen
            if self.rect.y <= 0 and self.flap_speed == 250:
                self.rect.y = 0
                self.flap_speed = 0
                self.y_velocity = 0
            # Enable flapping animation when bird moves down
            elif self.rect.y > 0 and self.flap_speed == 0:
                self.flap_speed = 250

    def applyGravity(self, dt):
        # Apply gravity to the bird's vertical velocity
        self.y_velocity += self.gravity * dt
        # Update the bird's vertical position
        self.rect.y += self.y_velocity

    def flap(self, dt):
        # Simulate a flap by giving the bird an upward velocity
        self.y_velocity = -self.flap_speed * dt

    def playAnimation(self):
        # Animate the bird's wings.
        if self.anim_counter == 5:
            self.image = self.img_list[self.image_index]

            # images switching and animation
            if self.image_index == 0:
                self.image_index = 1
            else:
                self.image_index = 0

            self.anim_counter = 0

        self.anim_counter += 1





