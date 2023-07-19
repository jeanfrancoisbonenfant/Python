import pygame.font
from settings import Settings

class Button():

    def __init__(self, ai_game, msg):
        """ Initialize button attribute """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()
        self._create_button()

        if msg:
            if msg == "Play":
                self._play_position()
            elif msg == "Easy":
                self._easy_position()
            elif msg == "Medium":
                self._medium_position()
            elif msg == "Hard":
                self._hard_position()

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ Turn msg into a render image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw blank button and then draw message. """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def _create_button(self):
        """ Create the initial play button. """
        # Set dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)


    def _play_position(self):
        """ Position Play button. """
        # Build the button 's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

    def _easy_position(self):
        """ Create selection of difficulty. """
        self.width, self.height = 200, 50
        self.button_color = (0, 200, 0)
        self.text_color = (0, 0, 0)
        # Build the button's rect object position to the right.
        desired_horizontal = self.settings.screen_width - self.width
        desired_vertical = (self.settings.screen_height / 2) - self.height
        self.rect = pygame.Rect(0, desired_vertical, self.width, self.height)
        self.rect.right = self.screen_rect.right

    def _medium_position(self):
        """ Create selection of difficulty. """
        self.width, self.height = 200, 50
        self.button_color = (255, 255, 0)
        self.text_color = (0, 0, 0)
        # Build the button's rect object position to the right.
        desired_horizontal = self.settings.screen_width - (self.width)
        desired_vertical = (self.settings.screen_height / 2)
        self.rect = pygame.Rect(0, desired_vertical, self.width, self.height)
        self.rect.right = self.screen_rect.right

    def _hard_position(self):
        """ Create selection of difficulty. """
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 0)
        self.text_color = (0, 0, 0)
        # Build the button's rect object position to the right.
        desired_horizontal = self.settings.screen_width - self.width
        desired_vertical = (self.settings.screen_height / 2) + self.height
        self.rect = pygame.Rect(0, desired_vertical, self.width, self.height)
        self.rect.right = self.screen_rect.right
