import numpy as np
class Algebra:
    
    #TODO: Fix linear combination
    
    @classmethod
    def linear_combination(cls,constants,vectors):
        """
        params: constants -- numpy object np.array([1,2,3])
        params: vectors --- array of Vector.vector objects np.array([Vector.vector,Vector.vector])
        """
        return np.sum(np.multiply(vectors.T,c),axis = 0)

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



x = np.array([Vector(1,2).vector,Vector(5,6).vector])
c = np.array([1,2])
print(Algebra.linear_combination(c,x))


