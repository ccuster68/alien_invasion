import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    '''Manage game assets and behaviors'''

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)

        pygame.display.set_caption("Alien Invasion")

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
        elif event.key == pygame.K_q:
            sys.exit()

    def _self_check_key_up(self, event):
        ''' Checks the key up events '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == "__main__":
    # Make new instance and run game
    ai = AlienInvasion()
    ai.run_game()
