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
            return None
        element = self.legend[char]()
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
        if element == None:
            return " "
        return element.char

    def worldToString(self):
        output = ""
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                element = self.grid.get(Vector(x,y))
                output += self.charFromElement(element)
            output += "\n"
        return output

    def turn(self):
        for critter in self.critters:
            critter.act(self.grid)


