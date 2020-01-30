import sys

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Roto Keys")

    color = (0, 0, 0)
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    color = (255, 255, 255)

        screen.fill(color)
        pygame.display.flip()

main()

