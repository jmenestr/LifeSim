from vector import *
import random


class Wall:

    def __init__(self,char = "#"):
        self.char = char

    def OriginChar(self):
        return self.char

class LifeForm:
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
        self.energy = 3

    def setPosition(self,vector):
        self.position = vector

    def loseEnergy(self,value = 0.2):
        self.energy -= value

    def gainEnergy(self,value):
        self.energy += value

    def returnEnergy(self):
        return self.energy

    def eat(self):
        pass

    def act(self,world_grid):
        pass

    def getDirection(self):
        dir_keys = [key for key in self.directions.keys()]
        return random.choice(dir_keys)

    def critterLook(self,world_grid,direction):
        target_pos = self.position.plus(direction)
        return world_grid.get(target_pos)

    def findFreeSquares(self,world_grid):
        direction_keys = [key for key in self.directions.keys()]
        free_direction_vectors = []
        for direction in direction_keys:
            direction_vector = self.directions[direction]
            if self.critterLook(world_grid,direction_vector) == " ":
                free_direction_vectors.append(direction_vector)
        return free_direction_vectors

    def OriginChar(self):
        return self.char

class Plant(LifeForm):
    def __init__(self,char,pos=Vector(-1,-1)):
        super(Plant,self).__init__(char,pos)
        self.energy = random.randint(1,5)+3
        self.dead = False

    def act(self,world_grid):
        if self.energy >= 20:
            self.energy /= 2
            return self.reproduce(world_grid)
        else:
            return self.grow()

    def grow(self,value = .1):
        event ={"action":"grow"}
        self.energy += value
        return event,self.position

    def reproduce(self,world_grid):
        event = {"action":"reproduce"}
        free_spaces = self.findFreeSquares(world_grid)
        if len(free_spaces) > 0:
            dest = random.choice(free_spaces)
            return event,self.position.plus(dest)
        else:
            return self.grow()

    def kill(self):
        self.dead = True

    def plantDead(self):
        return self.dead

class BouncingCritter(LifeForm):

    def __init__(self, char, pos=Vector(-1,-1)):
        super(BouncingCritter,self).__init__(char,pos)
        self.dead = False

    def findPlantSquares(self,world_grid):
        direction_keys = [key for key in self.directions.keys()]
        surrounding_plants = []
        for direction in direction_keys:
            dir_to_look=self.directions[direction]
            element = self.critterLook(world_grid,dir_to_look)
            if isinstance(element,Plant):
                surrounding_plants.append(dir_to_look)
        return surrounding_plants

    def act(self,world_grid):
        if self.energy <= 0:
            return self.die(world_grid)
        elif self.energy >= 12:
            self.energy -= 6
            return self.reproduce(world_grid)
        elif self.energy <= 5:
            return self.eat(world_grid)
        else:
            return self.move(world_grid)

    def move(self,world_grid):
        event = {"action": "move"}
        self.energy -= .2
        free_spaces = self.findFreeSquares(world_grid)
        if len(free_spaces) > 0:
            dest = random.choice(free_spaces)
            return event,self.position.plus(dest)
        return event,self.position

    def eat(self,word_grid):
        event = {"action":"eat"}
        plant_spaces = self.findPlantSquares(word_grid)
        if len(plant_spaces) > 0:
            destination = random.choice(plant_spaces)
            return event,self.position.plus(destination)
        return self.move(word_grid)


    def reproduce(self,world_grid):
        event = {"action":"reproduce"}
        free_spaces = self.findFreeSquares(world_grid)
        if len(free_spaces) > 0:
            dest = random.choice(free_spaces)
            return event,self.position.plus(dest)
        else:
            return self.move(world_grid)
    def isDead(self):
        return self.dead

    def kill(self):
        self.dead = True

    def die(self,world_grid):
        event = {"action":"die"}
        return event,self.position

class Predator(LifeForm):
    def __init__(self, char, pos=Vector(-1,-1)):
        super(Predator,self).__init__(char,pos)
        self.energy = 30

    def findAnimalSquares(self,world_grid):
        direction_keys = [key for key in self.directions.keys()]
        surrounding_targets = []
        for direction in direction_keys:
            dir_to_look=self.directions[direction]
            element = self.critterLook(world_grid,dir_to_look)
            if isinstance(element,BouncingCritter):
                surrounding_targets.append(dir_to_look)
        return surrounding_targets

    def act(self,world_grid):
        if self.energy <= 0:
            return self.die(world_grid)
        elif self.energy >= 40:
            self.energy -= 20
            return self.reproduce(world_grid)
        elif self.energy <= 20:
            return self.eat(world_grid)
        else:
            return self.move(world_grid)

    def move(self,world_grid):
        event = {"action": "move"}
        self.energy -= 1
        free_spaces = self.findFreeSquares(world_grid)
        if len(free_spaces) > 0:
            dest = random.choice(free_spaces)
            return event,self.position.plus(dest)
        return event,self.position

    def eat(self,word_grid):
        event = {"action":"eat"}
        plant_spaces = self.findAnimalSquares(word_grid)
        if len(plant_spaces) > 0:
            destination = random.choice(plant_spaces)
            return event,self.position.plus(destination)
        return self.move(word_grid)


    def reproduce(self,world_grid):
        event = {"action":"reproduce"}
        free_spaces = self.findFreeSquares(world_grid)
        if len(free_spaces) > 0:
            dest = random.choice(free_spaces)
            return event,self.position.plus(dest)
        else:
            return self.move(world_grid)

    def die(self,world_grid):
        event = {"action":"die"}
        return event,self.position


class WallFollower(LifeForm):
    def __init__(self, char, pos=Vector(-1,-1)):
        super(WallFollower,self).__init__(char,pos)
        self.current_dir = "w"
        self.dead = False

    def kill(self):
        self.dead = True

    def isDead(self):
        return self.dead


    def dirPlus(self,value):
        compass = ["e","ne","n","nw","w","sw","s","se"]
        current_index = compass.index(self.current_dir)
        return compass[((current_index+value) % 8)]

    def getDirection(self,world_grid):
        behind = self.directions[self.dirPlus(-3)]
        if self.critterLook(world_grid,behind) != " ":
            self.current_dir = self.dirPlus(-2)
            dir = self.directions[self.current_dir ]
        else:
            start = self.current_dir
            dir = self.directions[start]
        turn = 0
        while self.critterLook(world_grid,dir) != " ":
            turn += 1
            dir = self.directions[self.dirPlus(turn)]
        self.current_dir = self.dirPlus(turn)
        return dir

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
        dir_vec = self.getDirection(world_grid)
        return event,self.position.plus(dir_vec)

    def reproduce(self,world_grid):
        event = {"action":"reproduce"}
        free_spaces = self.findFreeSquares(world_grid)
        dest = random.choice(free_spaces)
        return event,self.position.plus(dest)

    def die(self,world_grid):
        event = {"action":"die"}
        return event,self.position
