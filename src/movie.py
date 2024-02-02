class Movie:
    """A simple wrapper class around a Movie object. Stores its name and the vectorized embedding."""
    def __init__(self, name="default", vector=[]):
        # We would like to keep all fields insulated and accessible only through defined methods.
        self.name = name
        self.vector = []
        for val in vector:
            self.vector.append(float(val))