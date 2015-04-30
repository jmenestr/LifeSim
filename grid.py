

class Grid:
    def __init__(self,height,width):
        self.space = [None]*(height*width)
        self.width = height
        self.height = width

    def isInside(self,vector):
        return vector.x >=0 and vector.x < self.width and vector.y >= 0 and vector.y <= self.height

    def get(self,vector):
        return self.space[vector.x + self.width*vector.y]

    def set(self,vector,value):
        if self.isInside(vector):
            self.space[vector.x + self.width*vector.y] = value
