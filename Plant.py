import pygame
from Organism import Organism
import random
import os

class Plant(Organism):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.initiative = 0

    def action(self, gr, world):
        result = random.randint(0, 100) < 10
        if result:
            new_random_coordinates = gr.find_random_empty(self.rect.x // 45, self.rect.y // 45)
            if new_random_coordinates == 0:
                return
            else:
                world.create_entity(type(self)(new_random_coordinates[0] * 45, new_random_coordinates[1] * 45, self.game))

    def collision(self, enemy, gr, world):
        if self.strength > enemy.strength:
                world.entities.remove(enemy)
                gr.grid[self.rect.x // 45][self.rect.y // 45] = self
        else:
            world.entities.remove(self)
            gr.grid[self.rect.x // 45][self.rect.y // 45] = enemy

class Grass(Plant):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'grass.png'))
        self.game = game
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.name = "grass"
        self.strength = 0

class Sowthistle(Plant):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'sowthistle.png'))
        self.game = game
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.name = "sowthistle"
        self.strength = 0

    def action(self, gr, world):
        for i in range(3):
            result = random.randint(0, 100) < 10
            if result == True:
                break
        if result:
            new_random_coordinates = gr.find_random_empty(self.rect.x // 45, self.rect.y // 45)
            if new_random_coordinates == 0:
                return
            else:
                world.create_entity(type(self)(new_random_coordinates[0] * 45, new_random_coordinates[1] * 45, self.game))

class Guarana(Plant):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'guarana.png'))
        self.game = game
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.name = "guarana"
        self.strength = 0

    def collision(self, enemy, gr, world):
        if self.strength > enemy.strength:
                world.entities.remove(enemy)
                gr.grid[self.rect.x // 45][self.rect.y // 45] = self
        else:
            world.entities.remove(self)
            enemy.strength += 3
            gr.grid[self.rect.x // 45][self.rect.y // 45] = enemy

class Belladonna(Plant):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'belladonna.png'))
        self.game = game
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.name = "belladonna"
        self.strength = 99

    def collision(self, enemy, gr, world):
        gr.grid[self.rect.x // 45][self.rect.y // 45] = 0
        world.entities.remove(enemy)
        world.entities.remove(self)

class Hogweed(Plant):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'hogweed.png'))
        self.game = game
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.name = "hogweed"
        self.strength = 10

    def action(self, gr, world):
        if gr.grid[(self.rect.x - 45) // 45][self.rect.y // 45] != 0 and (self.rect.x - 45) > 0:
            if gr.grid[(self.rect.x - 45) // 45][self.rect.y // 45].name != "cybersheep":
                world.entities.remove(gr.grid[(self.rect.x - 45) // 45][self.rect.y // 45])
                gr.grid[(self.rect.x - 45) // 45][self.rect.y // 45] = 0
        if gr.grid[(self.rect.x + 45) // 45][self.rect.y // 45] != 0 and (self.rect.x + 45) < 675:
            if gr.grid[(self.rect.x + 45) // 45][self.rect.y // 45].name != "cybersheep":
                world.entities.remove(gr.grid[(self.rect.x + 45) // 45][self.rect.y // 45])
                gr.grid[(self.rect.x + 45) // 45][self.rect.y // 45] = 0
        if gr.grid[self.rect.x // 45][(self.rect.y - 45) // 45] != 0 and (self.rect.y - 45) > 0:
            if gr.grid[self.rect.x // 45][(self.rect.y - 45) // 45].name != "cybersheep":
                world.entities.remove(gr.grid[self.rect.x // 45][(self.rect.y - 45) // 45])
                gr.grid[self.rect.x // 45][(self.rect.y - 45) // 45] = 0
        if gr.grid[self.rect.x // 45][(self.rect.y + 45) // 45] != 0 and (self.rect.y + 45) < 675:
            if gr.grid[self.rect.x // 45][(self.rect.y + 45) // 45].name != "cybersheep":
                world.entities.remove(gr.grid[self.rect.x // 45][(self.rect.y + 45) // 45])
                gr.grid[self.rect.x // 45][(self.rect.y + 45) // 45] = 0
        if gr.grid[(self.rect.x + 45) // 45][(self.rect.y + 45) // 45] != 0 and (self.rect.y + 45) < 675 and (self.rect.x + 45) < 675:
            if gr.grid[(self.rect.x + 45) // 45][(self.rect.y + 45) // 45].name != "cybersheep":
                world.entities.remove(gr.grid[(self.rect.x + 45) // 45][(self.rect.y + 45) // 45])
                gr.grid[(self.rect.x + 45) // 45][(self.rect.y + 45) // 45] = 0
        if gr.grid[(self.rect.x - 45) // 45][(self.rect.y - 45) // 45] != 0 and (self.rect.y - 45) > 0 and (self.rect.x - 45) > 0:
            if gr.grid[(self.rect.x - 45) // 45][(self.rect.y - 45) // 45].name != "cybersheep":
                world.entities.remove(gr.grid[(self.rect.x - 45) // 45][(self.rect.y - 45) // 45])
                gr.grid[(self.rect.x - 45) // 45][(self.rect.y - 45) // 45] = 0
        if gr.grid[(self.rect.x + 45) // 45][(self.rect.y - 45) // 45] != 0 and (self.rect.y - 45) > 0 and (self.rect.x + 45) < 675:
            if gr.grid[(self.rect.x + 45) // 45][(self.rect.y - 45) // 45].name != "cybersheep":
                world.entities.remove(gr.grid[(self.rect.x + 45) // 45][(self.rect.y - 45) // 45])
                gr.grid[(self.rect.x + 45) // 45][(self.rect.y - 45) // 45] = 0
        if gr.grid[(self.rect.x - 45) // 45][(self.rect.y + 45) // 45] != 0 and (self.rect.y + 45) < 675 and (self.rect.x - 45) > 0:
            if gr.grid[(self.rect.x - 45) // 45][(self.rect.y + 45) // 45].name != "cybersheep":
                world.entities.remove(gr.grid[(self.rect.x - 45) // 45][(self.rect.y + 45) // 45])
                gr.grid[(self.rect.x - 45) // 45][(self.rect.y + 45) // 45] = 0

    def collision(self, enemy, gr, world):
        if enemy.name == "cybersheep":
            world.entities.remove(self)
            gr.grid[self.rect.x // 45][self.rect.y // 45] = enemy
        else:
            world.entities.remove(enemy)

        

        

    


