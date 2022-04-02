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
            self._check_event()
            self.rocket.update()
            self._update_screen()



    def _check_event(self):
        """ Respond to keypresses and mouse events. """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_event(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_event(event)

    def _check_keydown_event(self,event):
        """ Respond to keydown events. """
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_foward = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_back = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self,event):
        """ Respond to keyup events. """
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_foward = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_back = False

    def _update_screen(self):
        """ Update image on the screen and flip to the new screen. """
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    rm = RocketMan()
    rm.run_game()