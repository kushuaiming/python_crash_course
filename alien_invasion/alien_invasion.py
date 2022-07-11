import sys
import pygame
from ship import Ship
from setting import Settings

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:
        for envent in pygame.event.get():
            if envent.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()

run_game()