import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    # Overall calls to manage game assets and behavior

    def __init__(self):
        # Initialize the game, and create game resources
        pygame.init()
        self.settings = Settings()
        pygame.display.set_caption(self.settings.window_title)

        # Set the background color
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = self.settings.bg_color

        self.ship = Ship(self)

    def run_game(self):
        # Start the main loop for the game.

        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Redraw the screen during each pass through the loop
                self.screen.fill(self.bg_color)
                self.ship.blitme()

                # Make the most recently drawn screen visible.
                pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


