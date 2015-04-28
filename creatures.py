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
        self.energy = random.randint(10,20)

    def setPosition(self,vector):
        self.position = vector

    def getDirection(self):
        dir_keys = [key for key in self.directions.keys()]
        return random.choice(dir_keys)

    def act(self,world_grid):
        if self.energy >= 15:
            self.energy -= 14
            return self.reproduce(world_grid)
        elif self.energy <= 0:
            return self.die(world_grid)
        else:
            self.energy -= .2
            return self.move(world_grid)

    def move(self,world_grid):
        event = {"action": "move"}
        dir = self.getDirection()
        dir_vec = self.directions[dir]
        if self.critterLook(world_grid,dir_vec) == " ":
            return event,self.position.plus(dir_vec)
        return event,self.position

    def reproduce(self,world_grid):
        event = {"action":"reproduce"}
        dir = self.getDirection()
        dest = self.directions[dir]
        while self.critterLook(world_grid,dest) != " ":
            dir = self.getDirection()
            dest = self.directions[dir]
        return event,self.position.plus(dest)

    def die(self,world_grid):
        event = {"action":"die"}
        return event,self.position

    def eat(self,world_grid):
        event = {"action": "eat"}


    def critterLook(self,world_grid,direction):
        target_pos = self.position.plus(direction)
        return world_grid.get(target_pos)


    def OriginChar(self):
        return self.char

class Plant:
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
        self.energy = 10

    def setPosition(self,vector):
        self.position = vector

    def getDirection(self):
        dir_keys = [key for key in self.directions.keys()]
        return random.choice(dir_keys)

    def act(self,world_grid):
        pass

    def grow(self,value=0.5):
        self.energy += value

    def reproduce(self,world_grid): #returns to world position vector to grow into
        pass
    def critterLook(self,world_grid,direction):
        target_pos = self.position.plus(direction)
        return world_grid.get(target_pos)

    def findEmptySquares(self,world_grid,direction,space = " "):
        dir_keys = [key for key in self.directions.keys()]
        for direction in dir_keys:
            pass


    def OriginChar(self):
        return self.char