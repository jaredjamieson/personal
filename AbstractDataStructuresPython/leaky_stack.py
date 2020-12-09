# Modified version of array_stack.py for Goodrich, et al. textbook
# Modified by Brian O'Neill
# Changes largely reflect removal of sample use code and different package structure
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""


    def __init__(self, size):
        """ Constructor """
        self._data = [None] * size                  # Init storage
        if size < 1:
            raise ValueError('Stack size is invalid.')
        else:
            self._capacity = size                   # Capacity
        self._size = 0                              # Init size of 0
        self._position = -1                          # Store index of list
        
        
    def __len__(self):
        """Return number of elements in the stack"""
        return self._size


    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size != 0


    def push(self, e):
        """Add element e to the top of the stack"""
        #self._data(self._capacity - 1) # Store the new item at the end of the list
        # Shift all elements over one, set last element to new one
        self._position = (self._position + 1) % self._capacity           # Position is current spot in list
        self._data[self._position] = e
        if self._size < self._capacity:
            self._size += 1
        

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._data[-1]                                     # Last element of stack is top


    def pop(self):
        """Remove and return the element at the top of the stack.

        Raise IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        self._size -= 1
        pop = self._data[self._position]
        self._data[self._position] = None
        self._position = (self._position - 1) % self._capacity
        
        return pop
    
    
    def __str__(self):
        """Return a string represntation of the array."""
        s = '['
        for i in range(self._size):
            if i != 0:
                s += ', '
            s += str(self._data[(self._position - self._size + 1 + i) % self._capacity])
        s += ']'
        return s
        


def main():
    """ Main function """
    #size = int(input('Enter array stack size: '))
    
    #obj = ArrayStack(size)
    
    #print(obj)     # String Func
    #print(obj.__len__()) # Len funct
    #print(obj.is_empty()) # Is_Empty
    
    #obj.push(1)    # Push funct
    #obj.push(2)
    #obj.push(3)
    
    #print(obj.pop())    # Pop function
    #print(obj.top())     # Top function
    
#main()