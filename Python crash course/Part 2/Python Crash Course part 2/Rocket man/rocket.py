import pygame

class Rocket:
    """ class to manage the rocket. """

    def __init__(self, rm_game):
        self.screen = rm_game.screen
        self.settings = rm_game.settings
        self.screen_rect = rm_game.screen.get_rect()

        #Load the rocket image and get its rect.
        self.image = pygame.image.load('image/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each new rocket at the bottom center of screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_foward = False
        self.moving_back = False

    def update(self):
        """ Update thr rocket's position based on the movement flag"""
        # Update rocket's rect positions.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1

        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1

        if self.moving_foward and self.rect.top > 0:
            self.rect.y -= 1

        if self.moving_back and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
    def blitme(self):
        """ Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)