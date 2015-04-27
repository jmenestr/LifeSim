from vector import *
import random

class Wall:

    def __init__(self,char = "#"):
        self.char = char

    def OriginChar(self):
        return self.char


class BouncingCritter:
    def __init__(self, pos=Vector(-1,-1), char="o"):
        self.char = char
        self.position = pos
        self.directions = {
            "n": Vector(0,1),
            "ne": Vector(1,1),
            "e": Vector(1,0),
            "se": Vector(1,-1),
            "s": Vector(0,-1),
            "sw": Vector(-1,-1),
            "w": Vector(-1,0),
            "nw": Vector(-1,1)
        }

    def setPosition(self,vector):
        self.position = vector

    def act(self,world):
        self.move(world)

    def move(self,world):
        dir_keys = [key for key in self.directions]
        dir = random.choice(dir_keys)
        dir_vector = self.directions[dir]

        crit_view = View(world,self.position)
        if crit_view.look(dir_vector) == " ":
            print("asdf")
            world.world.set(self.position.plus(dir_vector),"o")
            world.world.set(self.position," ")
            self.setPosition(self.position.plus(dir_vector))

    def OriginChar(self):
        return self.char


class View:
    def __init__(self,world,vector): # world is an instance of class World and position is a vector class
        self.world = world
        self.vector = vector

    def look(self,direction):
        target = self.vector.plus(direction)
        if self.world.isInside(target):
            return self.world.charFromElement(self.world.grid.get(target))




