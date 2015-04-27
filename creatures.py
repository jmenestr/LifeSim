from vector import *
import random


class Wall:

    def __init__(self,char = "#"):
        self.char = char

    def OriginChar(self):
        return self.char


class BouncingCritter:
    def __init__(self, char, pos=Vector(-1,-1)):
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

    def getDirection(self):
        dir_keys = [key for key in self.directions.keys()]
        return random.choice(dir_keys)

    def move(self,world_grid):
        dir = self.getDirection()
        dir_vec = self.directions[dir]
        if self.critterLook(world_grid,dir_vec) == " ":
            return self.position.plus(dir_vec)
        return self.position

    def critterLook(self,world_grid,direction):
        target_pos = self.position.plus(direction)
        return world_grid.get(target_pos)


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




