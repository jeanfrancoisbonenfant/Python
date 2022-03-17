import sys

import pygame
from settings import Settings
from rocket import Rocket


class RocketMan:
    """ Overall class to manage game asset and behaviour. """

    def __init__(self):
        """ Initialize the game, and create game resource. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket Man")

        self.rocket = Rocket(self)

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    """ Respond to keypresses. """
                    if event.key == pygame.K_RIGHT:
                        self.rocket.rect.x += 1
                    elif event.key == pygame.K_LEFT:
                        self.rocket.rect.x -= 1
                    elif event.key == pygame.K_q:
                        sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.rocket.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    rm = RocketMan()
    rm.run_game()