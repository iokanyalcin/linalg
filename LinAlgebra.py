import numpy as np

class LinearAlgebra:
    
    def __init__(self):
        pass
    
    @classmethod
    def linear_combination(cls,c,vectors):
        """
        Computes the linear combination of vectors
        param: c -- constants
        param: vectors, a numpy array includes all vectors
        """

        assert type(c) == list, "constants must be stored in a list"
        assert type(vectors) == list, "vectors must be stored in a list" 

        

        
    @classmethod
    def help(cls):
        print("This class designed for linear algebraic operations")

    class vector:
        def __init__(self,array):
            #TODO: Create a vector
            self.array = np.array(array)
            self.shape = self.array.shape


        

            
LinearAlgebra.help()
LinearAlgebra.linear_combination([1],[2])
