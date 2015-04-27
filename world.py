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
        return element.char

    def turn(self):
        for critter in self.critters:
            new_pos = critter.move(self.grid)
            self.grid.set(critter.position," ")
            self.grid.set(new_pos,critter)
            critter.setPosition(new_pos)

    def worldToString(self):
        output = ""
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                element = self.grid.get(Vector(x,y))
                output += self.charFromElement(element)
            output += "\n"
        return output


