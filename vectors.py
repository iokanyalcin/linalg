import numpy as np
class Vector:
    def __init__(self,x,y):
        #Unit vectors  i an j
        self.i = np.array([1,0])
        self.j = np.array([0,1])
        self.x = self.i * x
        self.y = self.j * y
        self.vector = self.x+self.y

    def __repr__(self):
        return "{}".format(self.vector)

    

vec = Vector(5,6)
print(vec)