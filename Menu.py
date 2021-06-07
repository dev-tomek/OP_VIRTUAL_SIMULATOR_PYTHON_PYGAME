import pygame
import os
from Instruction import Instruction
from World import World

class MainMenu:
    def __init__(self, game):
        #Menu.__init__(self, game) #inheriting from the base class
        #components
        self.main_menu_running = True
        self.bg_color = (255,221,158)
        self.g = game
        self.i = Instruction(self.g)
        self.w = World(self.g)
        #loading assets
        self.text_image = pygame.image.load(os.path.join('assets', 'name.png'))
        self.new_game_button_image = pygame.image.load(os.path.join('assets', 'new_game_button.png'))
        self.load_button_image = pygame.image.load(os.path.join('assets', 'load_button.png'))
        self.instruction_button_imgae = pygame.image.load(os.path.join('assets', 'instruction_button.png'))
        self.quit_button_image = pygame.image.load(os.path.join('assets', 'quit_button.png'))
        self.cursor_image = pygame.image.load(os.path.join('assets', 'eti_cursor.png'))
        self.author = pygame.image.load(os.path.join('assets', 'author.png'))
        #button positions tuples with offset for the cursor
        self.at_new_game = (480, 155)
        self.at_load = (480, 275)
        self.at_instruction = (480, 395)
        self.at_quit = (480, 525)
        self.cursor_state = self.at_new_game #default
        #creating rectangles
        self.cursor_rect = pygame.Rect(self.cursor_state, (45, 45)) 

    def handle_main_menu_cursor_for_w(self):
        if self.cursor_state == self.at_new_game:
            self.cursor_state = self.at_quit
        elif self.cursor_state == self.at_load:
            self.cursor_state = self.at_new_game
        elif self.cursor_state == self.at_instruction:
            self.cursor_state = self.at_load
        elif self.cursor_state ==  self.at_quit:
            self.cursor_state = self.at_instruction
        self.cursor_rect = pygame.Rect(self.cursor_state, (45, 45))

    def handle_main_menu_cursor_for_s(self):
        if self.cursor_state == self.at_new_game:
            self.cursor_state = self.at_load
        elif self.cursor_state == self.at_load:
            self.cursor_state = self.at_instruction
        elif self.cursor_state == self.at_instruction:
            self.cursor_state = self.at_quit
        elif self.cursor_state ==  self.at_quit:
            self.cursor_state = self.at_new_game
        self.cursor_rect = pygame.Rect(self.cursor_state, (45, 45))

    def change_scene(self):
        if self.cursor_state == self.at_new_game:
            self.w.world_running = True
            self.w.world_loop()
        elif self.cursor_state == self.at_load:
            self.w.load(self.w.gr)
        elif self.cursor_state == self.at_instruction:
            self.i.instruction_running = True
            self.i.instruction_loop()
        elif self.cursor_state ==  self.at_quit:
            pygame.quit()

    def check_main_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.handle_main_menu_cursor_for_w()
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.handle_main_menu_cursor_for_s()
                if event.key == pygame.K_RETURN:
                    self.change_scene()

    def main_menu_loop(self):
        while self.main_menu_running:
            self.g.WINDOW.fill(self.bg_color)
            self.g.WINDOW.blit(self.text_image, (0, 0))
            self.g.WINDOW.blit(self.cursor_image, (self.cursor_rect.x, self.cursor_rect.y))
            self.g.WINDOW.blit(self.new_game_button_image, (150, 130))
            self.g.WINDOW.blit(self.load_button_image, (-283, 250))
            self.g.WINDOW.blit(self.instruction_button_imgae, (-283, 370))
            self.g.WINDOW.blit(self.quit_button_image, (-128, 510))
            self.g.WINDOW.blit(self.author, (160, 650))
            self.check_main_menu_events()
            self.g.update()