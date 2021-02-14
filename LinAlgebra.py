import numpy as np


class LinearAlgebra:
    
    def __init__(self):
        pass
    
    @classmethod
    def linear_combination(cls,c,vectors):
        """
        Computes the linear combination of vectors
        param: c -- constants -- numpy array -- eg. np.array([c1,c2,c3])
        param: vectors, a numpy array includes all vectors, shape (1, Number of Vectors)
        eg. np.array([[1,2],[3,4]])
        """
        #TODO: Add more constraints, if neccessary... 
        assert type(c) == np.ndarray , "constants must be stored in a numpy array"
        assert type(vectors) == np.ndarray, "vectors must be stored in a numpy array"
        
        if len(vectors.shape) == 1:
            #If outter dim of vector not satisfied expand dimension
            vectors = np.expand_dims(vectors,axis = 0)
            
        constraints = [len(c) == len(vectors[0]),vectors.shape[1] == len(c)]
        
        if all(constraints) == True:
            return np.sum(np.multiply(vectors.T,c),axis = 0)
            