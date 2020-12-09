


class Deque:
    ''' A class representing a Deque '''
    # ----------------------- nested _Node class -------------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_previous', '_element', '_next'     # Streamline memory usage

        def __init__(self, e, n = None, p = None):
            self._element = e         # Reference to item contained
            self._next = n            # Reference to next node
            self._previous = p        # Reference to the previous node

    # ------------------------ linked list methods -----------------------------------
    def __init__(self):
        """Constructor"""
        self.__head = None
        self.__num_items = 0
        
    def __find(self, index):
        if index == 0:
            return self.__head
        i = 1
        current = self.__head._next
        while i < index:
            current = current._next
            i += 1
        return current
        
    def add_to_front(self, x):
        ''' Adds x to beginning of the deque '''
        new_node = self._Node(x, self.__head)                      # Create and point head to new node
        self.__head = new_node
        self.__num_items += 1
        
        
    def add_to_end(self, x):
        ''' Adds x to end of the deque '''
        if self.__num_items == 0:
            new_node = self._Node(x, self.__head)                  # Create and point head to new node
            self.__head = new_node
            self.__num_items += 1
        else:
            current = self.__head                                  
            while current is not None:                             # Traverse to end
                previous = current
                current = current._next
            new_node = self._Node(x, None, previous)               # Create new_node
            previous._next = new_node                              # Point last node to new_node
            self.__num_items += 1
            

    def remove_from_front(self):
        ''' Removes and returns first node of Deque '''
        items = self.__num_items
        
        if items == 0:                              
            raise IndexError('Deque is empty.')
        current = self.__head
        element = current._element
        
        self.__head = current._next                                # Head = original deque's 2nd node
        self.__num_items -= 1
        return element
        

    def remove_from_end(self):
        ''' Removes last node from Deque '''
        items = self.__num_items
        index = items - 1
        
        if items == 0:                                             # If no elements in the deque
            raise IndexError('Deque is empty.')
        elif items == 1:                                           # If only one node, previous set
            previous = self.__find(index)                          # to first and only node
        else:
            previous = self.__find(index - 1)                      # If more than one node, previous set to
        element = previous._next._element                          # correct node
        
        previous._next = None                                      # Set second to last node to point to None
        self.__num_items -= 1
        
        return element
        
    
    def __len__(self):
        ''' Returns num of items of Deque '''
        return self.__num_items
        
    
    def __str__(self):
        ''' Formats printing values '''
        string = '['
        current = self.__head
        while current is not None:
            string += str(current._element)
            current = current._next
            if current is not None:
                string += ', '
        string += ']'
        return string
