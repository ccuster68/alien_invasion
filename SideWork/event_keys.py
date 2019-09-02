import sys
import pygame


class EventKeys():
    ''' print out event keys '''

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def run_game(self):
        '''Start main loop for game'''
        while True:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill((200, 200, 200))
        # Make most recently drawn screen visible
        pygame.display.flip()

    def _check_events(self):
        # Watch for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._self_check_key_down(event)

    def _self_check_key_down(self, event):
        ''' Checks key down events '''
        if event.key == pygame.K_q:
            sys.exit()
        else:
            print(event.key)


if __name__ == "__main__":
    # Make new instance and run game
    ai = EventKeys()
    ai.run_game()
