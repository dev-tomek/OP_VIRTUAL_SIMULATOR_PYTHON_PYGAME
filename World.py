import pygame
import os

from Grid import Grid
from Organism import Organism
from Animal import Animal, Human, Wolf, Sheep, Fox, Turtle, Antelope, Cybersheep
from Plant import Plant, Grass, Sowthistle, Guarana, Belladonna, Hogweed

class World:
    def __init__(self, game):
        self.world_running = True
        self.g = game
        self.gr = Grid(self.g)
        self.bg_color = (128,128,128)
        self.entities = []
        self.entity_types = ["Wolf", "Sheep", "Fox", "Turtle", "Antelope", "Grass",
        "Sowthistle", "Guarana", "Belladonna", "Hogweed", "Cybersheep"]
        self.entity_selected_index = 0
        self.entity_selected = self.entity_types[self.entity_selected_index]
        self.initialize_entities()

    def create_entity(self, type):
        newEntity = type
        self.entities.append(newEntity)
        self.gr.grid[newEntity.rect.x // 45][newEntity.rect.y // 45] = newEntity

    def initialize_entities(self):
        self.create_entity(Human(135, 270, self.g))
        self.create_entity(Wolf(0, 315, self.g))
        self.create_entity(Wolf(315, 405, self.g))
        self.create_entity(Sheep(450, 0, self.g))
        self.create_entity(Sheep(630, 495, self.g))
        self.create_entity(Fox(675, 90, self.g))
        self.create_entity(Fox(90, 180, self.g))
        self.create_entity(Turtle(540, 540, self.g))
        self.create_entity(Turtle(360, 405, self.g))
        self.create_entity(Antelope(0, 360, self.g))
        self.create_entity(Antelope(0, 675, self.g))
        self.create_entity(Grass(585, 585, self.g))
        self.create_entity(Grass(0, 0, self.g))
        self.create_entity(Sowthistle(585, 675, self.g))
        self.create_entity(Sowthistle(45, 45, self.g))
        self.create_entity(Guarana(270, 585, self.g))
        self.create_entity(Guarana(180, 630, self.g))
        self.create_entity(Belladonna(360, 90, self.g))
        self.create_entity(Belladonna(180, 135, self.g))
        self.create_entity(Hogweed(360, 360, self.g))
        self.create_entity(Cybersheep(45, 630, self.g))

    def find_pos(self, coordinate):
        positions = []
        for i in range(self.gr.rows):
            positions.append(i * 45)

        positions.append(720)
        for i in range(len(positions)):
            if positions[i] <= coordinate < positions[i + 1]:
                return positions[i] 
            

    def spawnEntity(self):
        mouse_pos = pygame.mouse.get_pos()
        new_x_pos = self.find_pos(mouse_pos[0])
        new_y_pos = self.find_pos(mouse_pos[1])
        if self.gr.grid[new_x_pos // 45][new_y_pos // 45] != 0:
            return
        clas = globals()[self.entity_selected]
        self.create_entity(clas(new_x_pos, new_y_pos, self.g))


    def save(self, entities):
        with open("savegame.txt", "w+") as f:
            for entity in entities:
                f.write(f"{entity.name.capitalize()} {entity.rect.x} {entity.rect.y}\n")
        f.close()

    def load(self, gr):
        self.entities.clear()
        gr.grid.clear()
        gr.initialize_grid()
            
        LI = []
        with open("savegame.txt", "r") as f:
            for l in f:
                LI.append(l)
        entities = [i.split(' ') for i in LI]
        for j in entities:
            clas = globals()[j[0]]
            xpos = int(j[1])
            ypos = int(j[2])
            self.create_entity(clas(xpos, ypos, self.g))
        f.close()

    def makeTurn(self, direction):
        for i in self.entities:
            i.age += 1
        #sorting by initiative
        self.entities.sort(key=lambda x: (x.initiative, x.age))
        for i in self.entities:
            if i.name == "human":
                if i.special_ability_rest > 0:
                    i.special_ability_rest -= 1
                if i.special_ability_activated == True:
                    if i.special_ability_turns_left == 0:
                        i.icon = pygame.image.load(os.path.join('assets', 'human.png'))
                        i.special_ability_activated = False
                        i.special_ability_rest = 5
                    else:
                        i.icon = pygame.image.load(os.path.join('assets', 'ability_human.png'))
                        i.specialAbility(self.gr, self)
                        i.special_ability_turns_left -= 1
                i.action(direction, self.gr, self)
            else:
                i.action(self.gr, self)

    def check_world_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.world_running = False
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.makeTurn(pygame.K_w)
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.makeTurn(pygame.K_s)
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.makeTurn(pygame.K_a)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.makeTurn(pygame.K_d)
                if event.key == pygame.K_o:
                    self.save(self.entities)
                if event.key == pygame.K_q:
                    for i in self.entities:
                        if i.name == "human":
                            if i.special_ability_activated == True:
                                pass
                            elif i.special_ability_rest > 0:
                                pass
                            else:
                                i.icon = pygame.image.load(os.path.join('assets', 'ability_human.png'))
                                i.special_ability_activated = True
                                i.special_ability_turns_left = 5
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3: #right click
                    if self.entity_selected_index == (len(self.entity_types) - 1):
                        self.entity_selected_index = 0
                        self.entity_selected = self.entity_types[self.entity_selected_index]
                    else:
                        self.entity_selected_index += 1
                        self.entity_selected = self.entity_types[self.entity_selected_index]
                if event.button == 1: #left click
                    self.spawnEntity()

                
                


    def world_loop(self):
        while self.world_running:
            self.g.WINDOW.fill(self.bg_color)
            self.gr.draw_squares(self.g.WINDOW)
            for i in self.entities:
                i.draw()
            self.check_world_events()
            self.g.update()