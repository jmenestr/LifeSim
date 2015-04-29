class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self, other_vector):
        return Vector(self.x+other_vector.x, self.y+other_vector.y)

    def minus(self,other_vector):
        return Vector(self.x-other_vector.x, self.y - other_vector.y)

    def multiply(self, factor):
        x = factor*self.x
        y = factor*self.y
        return Vector(x,y)



