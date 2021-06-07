from Grid import Grid
import pygame
from Organism import Organism
import os
import random

class Animal(Organism):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)

    def collision(self, enemy, gr, world):
        print(self.name + " collides with " + enemy.name)
        if enemy.name == self.name:
            new_random_coordinates = gr.find_random_empty(self.rect.x // 45, self.rect.y // 45)
            if new_random_coordinates == 0:
                pass
            else:
                world.create_entity(type(self)(new_random_coordinates[0] * 45, new_random_coordinates[1] * 45, self.game))
        else:
            if self.strength > enemy.strength:
                world.entities.remove(enemy)
                gr.grid[self.rect.x // 45][self.rect.y // 45] = self
            else:
                world.entities.remove(self)
                gr.grid[self.rect.x // 45][self.rect.y // 45] = enemy

    def action(self, gr, world):
        self.oldX = self.rect.x
        self.oldY = self.rect.y
        gr.grid[self.rect.x // 45][self.rect.y // 45] = 0
        result = random.randint(0, 3)
        if result == 0 and self.rect.y > 0:
            self.rect.y -= 45
        elif result == 1 and self.rect.y < 675:
            self.rect.y += 45
        elif result == 2 and self.rect.x > 0:
            self.rect.x -= 45
        elif result == 3 and self.rect.x < 675:
            self.rect.x += 45

        if gr.grid[self.rect.x // 45][self.rect.y // 45] == 0:
            gr.grid[self.rect.x // 45][self.rect.y // 45] = self
        else:
            gr.grid[self.rect.x // 45][self.rect.y // 45].collision(self, gr, world)


class Human(Animal):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'human.png'))
        self.game = game
        self.strength = 5
        self.initiative = 4
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.name = "human"
        self.oldX = self.rect.x
        self.oldY = self.rect.y
        self.special_ability_activated = False
        self.special_ability_turns_left = 0
        self.special_ability_rest = 0
    
    def collision(self, enemy, gr, world):
        print(self.name + " collides with " + enemy.name)
        if self.strength > enemy.strength:
            world.entities.remove(enemy)
            gr.grid[self.rect.x // 45][self.rect.y // 45] = self
        else:
            world.entities.remove(self)
            gr.grid[self.rect.x // 45][self.rect.y // 45] = enemy
            

    def action(self, event_key, gr, world):
        self.oldX = self.rect.x
        self.oldY = self.rect.y
        gr.grid[self.rect.x // 45][self.rect.y // 45] = 0
        if event_key == pygame.K_w and self.rect.y > 0:
            self.rect.y -= 45
        elif event_key == pygame.K_s and self.rect.y < 675:
            self.rect.y += 45
        elif event_key == pygame.K_a and self.rect.x > 0:
            self.rect.x -= 45
        elif event_key == pygame.K_d and self.rect.x < 675:
            self.rect.x += 45

        if gr.grid[self.rect.x // 45][self.rect.y // 45] == 0:
            gr.grid[self.rect.x // 45][self.rect.y // 45] = self
        else:
            gr.grid[self.rect.x // 45][self.rect.y // 45].collision(self, gr, world)

    def specialAbility(self, gr, world): #purification
        if gr.grid[(self.rect.x - 45) // 45][self.rect.y // 45] != 0 and (self.rect.x - 45) > 0:
            world.entities.remove(gr.grid[(self.rect.x - 45) // 45][self.rect.y // 45])
            gr.grid[(self.rect.x - 45) // 45][self.rect.y // 45] = 0
        if gr.grid[(self.rect.x + 45) // 45][self.rect.y // 45] != 0 and (self.rect.x + 45) < 675:
            world.entities.remove(gr.grid[(self.rect.x + 45) // 45][self.rect.y // 45])
            gr.grid[(self.rect.x + 45) // 45][self.rect.y // 45] = 0
        if gr.grid[self.rect.x // 45][(self.rect.y - 45) // 45] != 0 and (self.rect.y - 45) > 0:
            world.entities.remove(gr.grid[self.rect.x // 45][(self.rect.y - 45) // 45])
            gr.grid[self.rect.x // 45][(self.rect.y - 45) // 45] = 0
        if gr.grid[self.rect.x // 45][(self.rect.y + 45) // 45] != 0 and (self.rect.y + 45) < 675:
            world.entities.remove(gr.grid[self.rect.x // 45][(self.rect.y + 45) // 45])
            gr.grid[self.rect.x // 45][(self.rect.y + 45) // 45] = 0
        if gr.grid[(self.rect.x + 45) // 45][(self.rect.y + 45) // 45] != 0 and (self.rect.y + 45) < 675 and (self.rect.x + 45) < 675:
            world.entities.remove(gr.grid[(self.rect.x + 45) // 45][(self.rect.y + 45) // 45])
            gr.grid[(self.rect.x + 45) // 45][(self.rect.y + 45) // 45] = 0
        if gr.grid[(self.rect.x - 45) // 45][(self.rect.y - 45) // 45] != 0 and (self.rect.y - 45) > 0 and (self.rect.x - 45) > 0:
            world.entities.remove(gr.grid[(self.rect.x - 45) // 45][(self.rect.y - 45) // 45])
            gr.grid[(self.rect.x - 45) // 45][(self.rect.y - 45) // 45] = 0
        if gr.grid[(self.rect.x + 45) // 45][(self.rect.y - 45) // 45] != 0 and (self.rect.y - 45) > 0 and (self.rect.x + 45) < 675:
            world.entities.remove(gr.grid[(self.rect.x + 45) // 45][(self.rect.y - 45) // 45])
            gr.grid[(self.rect.x + 45) // 45][(self.rect.y - 45) // 45] = 0
        if gr.grid[(self.rect.x - 45) // 45][(self.rect.y + 45) // 45] != 0 and (self.rect.y + 45) < 675 and (self.rect.x - 45) > 0:
            world.entities.remove(gr.grid[(self.rect.x - 45) // 45][(self.rect.y + 45) // 45])
            gr.grid[(self.rect.x - 45) // 45][(self.rect.y + 45) // 45] = 0

class Wolf(Animal):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'wolf.png'))
        self.game = game
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.strength = 9
        self.initiative = 5
        self.name = "wolf"
        self.oldX = self.rect.x
        self.oldY = self.rect.y

class Sheep(Animal):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'sheep.png'))
        self.game = game
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.strength = 4
        self.initiative = 4
        self.name = "sheep"
        self.oldX = self.rect.x
        self.oldY = self.rect.y

class Fox(Animal):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'fox.png'))
        self.game = game
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.strength = 3
        self.initiative = 7
        self.name = "fox"
        self.oldX = self.rect.x
        self.oldY = self.rect.y

    def action(self, gr, world):
        self.oldX = self.rect.x
        self.oldY = self.rect.y
        gr.grid[self.rect.x // 45][self.rect.y // 45] = 0
        result = random.randint(0, 3)
        if result == 0 and self.rect.y > 0:
            self.rect.y -= 45
        elif result == 1 and self.rect.y < 675:
            self.rect.y += 45
        elif result == 2 and self.rect.x > 0:
            self.rect.x -= 45
        elif result == 3 and self.rect.x < 675:
            self.rect.x += 45

        if gr.grid[self.rect.x // 45][self.rect.y // 45] == 0:
            gr.grid[self.rect.x // 45][self.rect.y // 45] = self
        else:
            if gr.grid[self.rect.x // 45][self.rect.y // 45].strength > self.strength:
                self.rect.x = self.oldX
                self.rect.y = self.oldY
                gr.grid[self.rect.x // 45][self.rect.y // 45] = self
            else:
                gr.grid[self.rect.x // 45][self.rect.y // 45].collision(self, gr, world)

class Turtle(Animal):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'turtle.png'))
        self.game = game
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.strength = 2
        self.initiative = 1
        self.name = "turtle"
        self.oldX = self.rect.x
        self.oldY = self.rect.y
    
    def action(self, gr, world):
        self.oldX = self.rect.x
        self.oldY = self.rect.y
        if random.randint(0, 100) < 75:
            pass
        else:
            gr.grid[self.rect.x // 45][self.rect.y // 45] = 0
            result = random.randint(0, 3)
            if result == 0 and self.rect.y > 0:
                self.rect.y -= 45
            elif result == 1 and self.rect.y < 675:
                self.rect.y += 45
            elif result == 2 and self.rect.x > 0:
                self.rect.x -= 45
            elif result == 3 and self.rect.x < 675:
                self.rect.x += 45

            if gr.grid[self.rect.x // 45][self.rect.y // 45] == 0:
                gr.grid[self.rect.x // 45][self.rect.y // 45] = self
            else:
                gr.grid[self.rect.x // 45][self.rect.y // 45].collision(self, gr, world)

    def collision(self, enemy, gr, world):
        print(self.name + " collides with " + enemy.name)
        if enemy.strength < 5:
            enemy.rect.x = enemy.oldX
            enemy.rect.y = enemy.oldY
            gr.grid[enemy.rect.x // 45][enemy.rect.y // 45] = enemy
        else:
            world.entities.remove(self)
            gr.grid[self.rect.x // 45][self.rect.y // 45] = enemy

class Antelope(Animal):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'antelope.png'))
        self.game = game
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.strength = 4
        self.initiative = 4
        self.name = "antelope"
        self.oldX = self.rect.x
        self.oldY = self.rect.y

    def action(self, gr, world):
        self.oldX = self.rect.x
        self.oldY = self.rect.y
        gr.grid[self.rect.x // 45][self.rect.y // 45] = 0
        result = random.randint(0, 3)
        if result == 0 and self.rect.y > 45:
            self.rect.y -= 90
        elif result == 1 and self.rect.y < 630:
            self.rect.y += 90
        elif result == 2 and self.rect.x > 45:
            self.rect.x -= 90
        elif result == 3 and self.rect.x < 630:
            self.rect.x += 90

        if gr.grid[self.rect.x // 45][self.rect.y // 45] == 0:
            gr.grid[self.rect.x // 45][self.rect.y // 45] = self
        else:
            gr.grid[self.rect.x // 45][self.rect.y // 45].collision(self, gr, world)

    def collision(self, enemy, gr, world):
        print(self.name + " collides with " + enemy.name)
        if enemy.name == self.name:
            new_random_coordinates = gr.find_random_empty(self.rect.x // 45, self.rect.y // 45)
            if new_random_coordinates == 0:
                pass
            else:
                world.create_entity(type(self)(new_random_coordinates[0] * 45, new_random_coordinates[1] * 45, self.game))
        else:
            escape = random.randint(0, 100) < 50
            if escape:
                new_random_coordinates = gr.find_random_empty(self.rect.x // 45, self.rect.y // 45)
                if new_random_coordinates == 0:
                    if self.strength > enemy.strength:
                        world.entities.remove(enemy)
                        gr.grid[self.rect.x // 45][self.rect.y // 45] = self
                    else:
                        world.entities.remove(self)
                        gr.grid[self.rect.x // 45][self.rect.y // 45] = enemy
                else:
                    self.rect.x = new_random_coordinates[0] * 45
                    self.rect.y = new_random_coordinates[1] * 45
                    gr.grid[self.rect.x // 45][self.rect.y // 45] = self
                
            elif self.strength > enemy.strength:
                world.entities.remove(enemy)
                gr.grid[self.rect.x // 45][self.rect.y // 45] = self
            else:
                world.entities.remove(self)
                gr.grid[self.rect.x // 45][self.rect.y // 45] = enemy

class Cybersheep(Animal):
    def __init__(self, xpos, ypos, game):
        super().__init__(xpos, ypos, game)
        self.icon = pygame.image.load(os.path.join('assets', 'cybersheep.png'))
        self.game = game
        self.rect = pygame.Rect(self.xpos, self.ypos, 45, 45)
        self.strength = 11
        self.initiative = 4
        self.name = "cybersheep"
        self.oldX = self.rect.x
        self.oldY = self.rect.y

    def action(self, gr, world):
        self.oldX = self.rect.x
        self.oldY = self.rect.y
        target = "hogweed"
        gr.grid[self.rect.x // 45][self.rect.y // 45] = 0
        targetAlive = False
        targetXpos = cybersheepYpos = 0
        for entity in world.entities:
            if entity.name == target:
                targetAlive = True
                targetXpos = entity.rect.x // 45
                targetYpos = entity.rect.y // 45
        if targetAlive:
            if self.rect.x // 45 > targetXpos and self.rect.x > 0:
                self.rect.x -= 45
            elif self.rect.x // 45 < targetXpos and self.rect.x < 675:
                self.rect.x += 45
            elif self.rect.y // 45 < targetYpos and self.rect.y < 675:
                self.rect.y += 45
            elif self.rect.y // 45 > targetXpos and self.rect.y > 0:
                self.rect.y -= 45

            if gr.grid[self.rect.x // 45][self.rect.y // 45] == 0:
                gr.grid[self.rect.x // 45][self.rect.y // 45] = self
            else:
                gr.grid[self.rect.x // 45][self.rect.y // 45].collision(self, gr, world)
        else:
            super().action(gr, world)