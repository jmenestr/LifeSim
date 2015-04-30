from grid import *
from creatures import *

class World:
    def __init__(self,plan,legend):
        self.grid = Grid(len(plan[0]),len(plan))
        self.legend = legend
        self.critters = []
        self.plants = []
        self.setUpWorld(plan)

    def createElement(self,char):
        if char == " ":
            return " "
        element = self.legend[char](char)
        return element

    def setUpWorld(self,plan):
        for y, line in enumerate(plan):
            for x, char in enumerate(line):
                element = self.createElement(char)
                if isinstance(element,BouncingCritter) or isinstance(element,WallFollower):
                    element.setPosition(Vector(x,y))
                    self.critters.append(element)
                if isinstance(element,Plant):
                    element.setPosition(Vector(x,y))
                    self.plants.append(element)
                self.grid.set(Vector(x,y),element)

    def charFromElement(self,element):
        if element == " ":
            return " "
        return element.OriginChar()

    def isempty(self):
        if len(self.critters) <= 0:
            return True

    def turn(self):
        critters_after_turn = []
        for critter in self.critters:
            (event,dest) = critter.act(self.grid)
            if event["action"] == "move":
                self.grid.set(critter.position," ")
                self.grid.set(dest,critter)
                critter.setPosition(dest)
                critters_after_turn.append(critter)
            if event["action"] == "reproduce":
                baby_crit = BouncingCritter(critter.OriginChar(),dest)
                self.grid.set(dest,baby_crit)
                critters_after_turn.append(critter)
                critters_after_turn.append(baby_crit)
            if event["action"] == "eat":
                target_plant = self.grid.get(dest)
                target_plant_energy = target_plant.returnEnergy()
                critter.gainEnergy(target_plant_energy)
                target_plant.kill()
                self.grid.set(critter.position," ")
                self.grid.set(dest,critter)
                critter.setPosition(dest)
                critters_after_turn.append(critter)
            if event["action"] == "die":
                self.grid.set(critter.position," ")
        self.critters = critters_after_turn

        plants_after_turn= []
        for plant in self.plants:
            if plant.plantDead():
                continue
            (event,dest) = plant.act(self.grid)
            if event["action"] == "grow":
                plants_after_turn.append(plant)
            elif event["action"] == "reproduce":
                new_plant = Plant(plant.OriginChar(),dest)
                self.grid.set(dest,new_plant)
                plants_after_turn.append(new_plant)
                plants_after_turn.append(plant)
        self.plants = plants_after_turn
        '''
            new_pos = critter.move(self.grid)
            self.grid.set(critter.position," ")
            self.grid.set(new_pos,critter)
            critter.setPosition(new_pos)'''

    def worldToString(self):
        output = ""
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                element = self.grid.get(Vector(x,y))
                char = self.charFromElement(element)
                output += char
            output += "\n"
        return output


