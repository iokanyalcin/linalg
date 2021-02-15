import numpy as np
class Vector:
    def __init__(self,x,y):
        #Unit vectors  i an j
        self.i = np.array([1,0])
        self.j = np.array([0,1])
        self.x = self.i * x
        self.y = self.j * y
        self.vector = self.x+self.y

    def vec_sum(self,other):
        """Perfrom elementwise sum of two vectors"""
        return Vector(self.x+other.x,self.y+other.y)
    def __repr__(self):
        return "vector({})".format(self.vector)

    

vec1 = Vector(5,6)
vec2 = Vector(10,4)
print(vec1.vec_sum(vec2))