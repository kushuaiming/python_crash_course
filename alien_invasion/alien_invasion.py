import sys

import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for envent in pygame.event.get():
            if envent.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

run_game()