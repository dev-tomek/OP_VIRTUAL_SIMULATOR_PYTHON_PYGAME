import pygame
from Game import Game

def main():
    pygame.init()
    g = Game()
    g.game_loop()
    pygame.quit()

if __name__ == "__main__":
    main()
    
