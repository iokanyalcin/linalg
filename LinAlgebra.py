import numpy as np

class LinearAlgebra:
    
    def __init__(self):
        pass
    
    @classmethod
    def linear_combination(cls,c,vectors):
        """
        Computes the linear combination of vectors
        param: c -- constants
        param: vectors, a numpy array includes all vectors, shape (1, Number of Vectors)
        eg. np.array([[1,2],[3,4]])

        """

        assert type(c) == np.ndarray , "constants must be stored in a numpy array"
        assert type(vectors) == np.ndarray, "vectors must be stored in a numpy array"
        
        if len(vectors.shape) == 1:
            #If outter dim of vector not satisfied expand dimension
            vectors = np.expand_dims(vectors,axis = 0)
            

        #Expand dimension
        constraints = [len(c) == len(vectors[0]),vectors.shape[1] == len(c)]
        
        if all(constraints) == True:
            return np.sum(np.multiply(vectors.T,c),axis = 0)
            

        



        
    @classmethod
    def help(cls):
        print("This class designed for linear algebraic operations")

    class vector:
        def __init__(self,array):
            #TODO: Create a vector
            self.array = np.array(array)
            self.shape = self.array.shape


        

            

combination = LinearAlgebra.linear_combination(np.array([[1,2],[3,4],[5,6]]),np.array([2,3,4]))
print(type(combination))