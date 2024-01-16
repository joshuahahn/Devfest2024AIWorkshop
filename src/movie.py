class Movie:
    """A simple wrapper class around a Movie object. Stores its name and the vectorized embedding."""
    def __init__(self, name="default", vector=[]):
        # We would like to keep all fields insulated and accessible only through defined methods.
        self.__name = name
        self.__vector = vector

    def getName(self):
        return self.__name
    
    def getVector(self):
        return self.__vector
    
    def setName(self, newName):
        self.__name = newName
    
    def setVetor(self, newVector):
        self.__vector = newVector