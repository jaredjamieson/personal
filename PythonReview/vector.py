class Vector:
    """Represent a vector in a multidimensional space"""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other): # Relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    ### V1 and V2 are created in main and populated with values.  
    
    # Multiplication Operator Overloading to work with Type: Vectors
    def __mul__(self, multiplier):
        
        # Starts with a vector of zeros
        # Similar to ziping two list together by adding two identical elements
        result = Vector(len(self))
        # For each element of passed vector, multiply by passed multiplier
        for j in range(len(self)):
            # Element of vector combines multiplier then changes 0's vector into new value
            result[j] = self[j] * multiplier

        return result    

    def __eq__(self, other):
        """Return True if vector has same coordinates as other"""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other"""
        return not self == other # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>' # adapt list representation
