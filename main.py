import pygame
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

def main():
    pygame.init()
    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("PACMAN")
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create a game object
    game = Game()
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(30)
    pygame.quit()

if __name__ == '__main__':
    main()
