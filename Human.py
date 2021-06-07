import random

class Human:
    def __init__(self, x, y, strength, initiative):
        self.x = x
        self.y = y
        self.strength = strength 
        self.initiative = initiative
        self.symbol = 'H'
        
    def movement(self):
        random_direction = random.randint(0,3)
        if (random_direction == 0 and self.x < 5):
            self.x = self.x + 1
        elif (random_direction == 1 and self.x > 0):
            self.x = self.x - 1
        elif (random_direction == 2 and self.y < 5):
            self.y = self.y + 1
        elif (random_direction == 3 and self.y > 0):
            self.y = self.y - 1

    def draw_human(self, grid):
        grid[self.x][self.y] = self.symbol
