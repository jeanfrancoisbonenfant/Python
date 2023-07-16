import sys

import pygame

class EmptyPrint:
    """ Overall class to manage empty screen print key exercice"""

    def __init__(self):
        """ Initialize the screen """
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Empty Print")

        #Set the background color
        self.bg_color = (230, 230, 230)
    def run_game(self):
        """ Start the main loop for the screen. """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    es = EmptyPrint()
    es.run_game()