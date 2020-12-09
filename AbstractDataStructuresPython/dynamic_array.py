# Largely taken from Goodrich et al., Code Fragment 5.3 (p. 196)
# Intended to serve as a simplified version of a python list, to explain how they work

import ctypes                                       # Provides low-level arrays

class DynamicArray:
    """A dynamic array class similar to a simplified Python list."""

    def __init__(self):
        """Create an empty array"""
        self._n = 0                                 # Count actual elements
        self._capacity = 1                          # Default array capacity
        self._A = self._make_array(self._capacity)  # Low-level array


    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n


    def __getitem__(self, k):
        """Return element at index k."""
        if k >= self._n or abs(k) >= self._n:       # Checks if k is in array
            raise IndexError('Invalid index')
        elif k < 0:
            k = self._n + k                         # Counts backwards from last non-empty position
        
        return self._A[k]                           # Retrieve from array


    def __setitem__(self, k, val):
        """Set item to an array"""
        if k >= self._n or abs(k) >= self._n:       # Checks if k is in array
            raise IndexError('Invalid index') 
        else:
            self._A[k] = val                        # Replaces val at element k, assume k >= 0
        
        
    def pop(self):
        """Removes and returns last element of the array"""
        
        last = self[-1]                             # Saves the last item
        self._n -= 1                                # Updates n to new list size
        
        if self._capacity == (self._n * 4):         # Too much room, halve capacity
            self._resize(2 / self._capacity)
            
        return last
    
    
    def __eq__(self, other):
        """Bool if two DynamicArrays are identical"""
        isTrue = True
        
        for i in range(self._n):
            if self[i] == other[i]:
                pass
            else:
                isTrue = False
        return isTrue


    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:               # Not enough room, double capacity
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1


    # Code Fragment 5.5 (p. 204)
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # For simplicity, assumes that 0 <= k <= n
        if self._n == self._capacity:               # Not enough room, double capacity
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):             # Shift rightmost first, then move left
            self._A[j] = self._A[j-1]
        self._A[k] = value                          # Store newest element
        self._n += 1


    # Code Fragment 5.6 (p. 206)
    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        # Does not consider shrinking the array in this version
        for k in range(self._n):
            if self._A[k] == value:                 # Found a match!
                for j in range(k, self._n - 1):     # Shift other elements to fill the gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None         # Fill the old last spot with None
                self._n -= 1                        # Reduce size
                return                              # Exit the function immediately, since we were successful
        raise ValueError('Value not found')


    def _resize(self, c):                           # Non-public utility function
        """Resize internal array to capacity c."""
        B = self._make_array(c)                     # New, bigger array
        for k in range(self._n):                    # For each existing value
            B[k] = self._A[k]
        self._A = B                                 # B is now the array
        self._capacity = c


    def _make_array(self, c):                       # Non-public utility function
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()


    def __str__(self):
        """Return a string represntation of the array."""
        s = '['
        for i in range(self._n):
            if i != 0:
                s += ', '
            s += str(self._A[i])
        s += ']'
        return s


    def lab3_v1(self):
        import random
        for x in range(self._n):                    # loops through nums in array
            for y in range(x + 1, self._n):         # loops through x and nums in array
                z = random.randint(0, y - x)        # Rand int
                temp = self._A[x]                   # Var = xth element of array
                self._A[x] = self._A[x + z]         
                self._A[x + z] = temp               # Assigns self._A[x] to self._A[x + z]
            
            
    def lab3_v2(self):
        import random
        for i in range(10):                         # 0 - 9
            for j in range(self._n):                # loops through nums in array
                k = random.randint(0,self._n - 1)   # sets k between 0 and (nums - 1)
                temp = self._A[j]                   
                self._A[j] = self._A[k]            
                self._A[k] = temp                   # Assigns self._A[j] to self._A[k]
                
                
def main():
    
    c = DynamicArray()                               # Class Object
    c2 = DynamicArray()
    
    c.append('a')
    c.append('b')
    c.append('c')
    
    c2.append('a')
    c2.append('b')
    c2.append('c')
    
    
    k = -1
    
    #print(c[k])
    #c[k] = 'y' 
    #print(c.pop())
    #print(c == c2)
    
    
main()