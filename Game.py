import pygame
from Menu import MainMenu
from World import World

class Game:
    FPS = 60
    clock = pygame.time.Clock()
    def __init__(self):
        self.WIDTH = 720
        self.HEIGHT = 720
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.TITLE = pygame.display.set_caption("Virtual World Simulator")
        self.game_running = True #when the program is running
        self.m = MainMenu(self)
        self.w = World(self)
    
    def game_loop(self):
        while self.game_running:
            self.clock.tick(self.FPS) #60 times per second
            self.m.main_menu_running = True
            self.m.main_menu_loop()
            self.update()
            
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   self.m.main_menu_running = True

    def update(self):
        pygame.display.update()

        