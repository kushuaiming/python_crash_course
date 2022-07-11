import sys
import pygame

# Watch for keyboard and mouse events.
def check_events():
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()