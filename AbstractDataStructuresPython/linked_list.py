# Author: Brian O'Neill
# Simple Linked List class to go with Goodrich et al. text for CS/IT 200


class LinkedList:
    """A class representing a linked list."""
    # ----------------------- nested _Node class -------------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'     # Streamline memory usage

        def __init__(self, e, n=None):
            self._element = e         # Reference to item contained
            self._next = n            # Reference to next node

    # ------------------------ linked list methods -----------------------------------
    def __init__(self):
        """Constructor"""
        self.__head = None
        self.__num_items = 0

    def insert(self, index, item):
        """Adds an item to the list at the given index

        :param item: Item to add to the list
        :param index: Location to add the item. Should be between 0 and size() (inclusive)
        :return: None
        """
        if index < 0 or index > self.__num_items:
            raise IndexError('Invalid index ' + str(index))
        elif index == 0:
            new_node = self._Node(item, self.__head)
            self.__head = new_node
            self.__num_items += 1
        else:
            previous = self.__find(index - 1)
            current = previous._next
            new_node = self._Node(item, current)
            previous._next = new_node
            self.__num_items += 1

    def get(self, index):
        """Gets the item at the given index.

        :param index: Location to retrieve from. Should be between 0 and size()-1 (inclusive)
        :return: The item at index.
        """
        if index < 0 or index >= self.__num_items:
            raise IndexError('Invalid index ' + str(index))
        else:
            node = self.__find(index)
            return node._element

    def delete(self, index):
        """Removes the item at index from the list.

        :param index: Location to remove from. Should be between 0 and size()-1 (inclusive)
        :return: None
        """
        if index < 0 or index >= self.__num_items:
            raise IndexError('Invalid index ' + str(index))
        elif index == 0:
            self.__head = self.__head._next
            self.__num_items -= 1
        else:
            previous = self.__find(index - 1)
            current = previous._next
            previous._next = current._next
            current._next = None
            self.__num_items -= 1

    def is_empty(self):
        """Returns True if the list is empty, False otherwise."""
        return self.__num_items == 0

    def size(self):
        """Returns the number of items in the list."""
        return self.__num_items

    def remove_all(self):
        """Removes all items from the list."""
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

    def __str__(self):
        string = '['
        current = self.__head
        while current is not None:
            string += str(current._element)
            current = current._next
            if current is not None:
                string += ', '
        string += ']'
        return string

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('Invalid index')
        return self.get(index)

    def __delitem__(self, index):
        # This block checks to see if index is an instance of the int type.
        # If it is not, the method raises a TypeError because indices must be integers.
        if not isinstance(index, int):
            raise TypeError('Invalid index')
        self.delete(index)

    def __len__(self):
        return self.size()
    
    def append(self, x):
        """ Adds x to end of list """
        if self.__num_items == 0:                               # If LL is empty, create first node
            new_node = self._Node(x, self.__head)               # No IndexError because index is not a user parameter
            self.__head = new_node
            self.__num_items += 1
        else:                                                   # If nodes in LL, append to end
            previous = self.__find(self.__num_items - 1)
            current = previous._next
            new_node = self._Node(x, current)
            previous._next = new_node
            self.__num_items += 1
            
    def remove(self, item):
        """ Removes first instance of item in LL """
        if self.__num_items == 0:                                # Checks if LL is empty
            print('Linked List is Empty. ')
            
        element = 1                                              # Count through elements of LL
        current = self.__head                                    # Start at the head, first data = None
        previous = None                                          
        
        while current is not None:                               # While not on the last node
            if current._element == item:                         # If values match
                if previous is not None:                         # Node is not Head
                    previous._next = current._next               #
                else:
                    self.__head = current._next                  # If node is Head, set new head
                    return
            previous = current                                   # Traverse to next node
            current = current._next                              
            element += 1                                         # Increase depth in LL
            
    def contains(self, item):
        """ Returns True if item is in LL, False otherwise """
        
        isTrue = False                                        
        
        current = self.__head                                    # Start at the Head
        
        while current is not None:                               # While not at the end of the LL
            if current._element == item:                         # If vals match, reset Bool
                isTrue = True                                    
            else:
                pass                                             # If val not found, keep looping
            
            current = current._next                              # Traverse to next node
        
        return isTrue
        
    def extend(self, other_list):
        """ Extends self LL by other_list """
        
        current = self.__head                                    # Start at the Head of first LL
        previous = None
        counter = 0
        other_current = other_list.__head
        
        while current is not None:                               # Travers to end of first LL
            previous = current
            current = current._next
        
        while other_current is not None:                         # While not at the end of second list
            temp_element = other_list.__getitem__(counter)
            counter += 1
            
            self.append(temp_element)
            
            other_current = other_current._next
        
        
    def reverse(self):
        """ Reverses the elements of a LL """
        counter = 1                                              # Variables for function
        current = self.__head 
        original_length = self.__num_items
        
        for length in range(self.__num_items):
            current = self.__find(original_length - counter)     # Appends list in reversed order to first list
            self.append(current._element)
            counter += 1
            
        self.__head = self.__find(original_length)
