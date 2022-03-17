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

    def blitme(self):
        """ Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)