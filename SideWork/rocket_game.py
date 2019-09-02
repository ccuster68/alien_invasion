import sys
import pygame
from settings import Settings
from rocket import Rocket


class Rocket_Game():
    ''' simple rocket on screen that can move up down left right '''

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.settings = Settings()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_color = self.settings.bg_color
        self.ship = Rocket(self)

    def run_game(self):
        '''Start main loop for game'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        # Make most recently drawn screen visible
        pygame.display.flip()

    def _check_events(self):
        # Watch for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._self_check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._self_check_key_up(event)

    def _self_check_key_down(self, event):
        ''' Checks key down events '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _self_check_key_up(self, event):
        ''' Checks the key up events '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


if __name__ == "__main__":
    # Make new instance and run game
    ai = Rocket_Game()
    ai.run_game()
