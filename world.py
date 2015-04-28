from grid import *
from vector import *
from creatures import *

class World:
    def __init__(self,plan,legend):
        self.grid = Grid(len(plan[0]),len(plan))
        self.legend = legend
        self.critters = []
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
                if isinstance(element,BouncingCritter):
                    element.setPosition(Vector(x,y))
                    self.critters.append(element)
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
            if event["action"] == "die":
                self.grid.set(critter.position," ")
        self.critters = critters_after_turn
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


