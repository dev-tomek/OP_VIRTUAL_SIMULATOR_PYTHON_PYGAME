import pygame
import os

class Instruction:
    def __init__(self, game):
        self.g = game
        self.instruction_running = False
        self.bg_color = (255,221,158)
        self.back_button = pygame.image.load(os.path.join('assets', 'back_button.png'))
        self.cursor_image = pygame.image.load(os.path.join('assets', 'eti_cursor.png'))
        self.text = pygame.image.load(os.path.join('assets', 'texts.png'))

    def check_instruction_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.instruction_running = False
                if event.key == pygame.K_RETURN:
                    self.instruction_running = False

    def instruction_loop(self):
        while self.instruction_running:
            self.g.WINDOW.fill(self.bg_color)
            self.g.WINDOW.blit(self.back_button, (450, 600))
            self.g.WINDOW.blit(self.cursor_image, (1210, 625))
            self.g.WINDOW.blit(self.text, (0,0))
            self.check_instruction_events()
            self.g.update()