import pygame
import os
import random

class Grid:
    def __init__(self, game):
        self.g = game
        self.grid_color = (90,90,90)
        self.rows = 16
        self.columns = 16
        self.square_size = 45
        self.grid = []
        self.initialize_grid()

    def draw_squares(self, window):
        for row in range(self.rows):
            for col in range(row % 2, self.rows, 2):
                 pygame.draw.rect(window, self.grid_color, 
                 (row*self.square_size, col*self.square_size, 
                 self.square_size, self.square_size))

    def initialize_grid(self):
        for i in range(self.rows):
            self.grid.append([0] * self.columns)

    def find_random_empty(self, xpos, ypos):
        optionStart = random.randint(0, 7)
        option = optionStart + 1
        candX = candY = 0
        found = False

        while not found:
            option = option % 8
            if option == optionStart:
                return 0
            candX = xpos
            candY = ypos
            if (option == 0):
                candX -= 1
            elif (option == 1):
                candX += 1
            elif (option == 2):
                candY -= 1
            elif (option == 3):
                candY += 1
            elif (option == 4):
                candY += 1
                candX -= 1
            elif (option == 5):
                candY += 1
                candX += 1
            elif (option == 6):
                candY -= 1
                candX += 1
            elif (option == 7):
                candY -= 1
                candX -= 1
            if (candX < 0 or candX > (self.rows - 1) or candY < 0 or candY > (self.columns - 1)):
                option += 1
            elif self.grid[candX][candY] != 0:
                option += 1
            else:
                found = True
        
        result = (candX, candY)
        return result
        

