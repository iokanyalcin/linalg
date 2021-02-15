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
        """
        Perfrom elementwise sum of two vectors
        param other -- Vector object
        """
        if isinstance(other,Vector):
            return Vector(self.x+other.x,self.y+other.y)
        else: 
            raise "Given object is not Vector instance"
    
    def __mul__(self,other):
        return self.vector*other
    
    def __rmul__(self,other):
        return self.__mul__(other)
    def __repr__(self):
        return "vector({})".format(self.vector)



print(5*Vector(1,2))



