import stacks
""" PART 1 """
class Queue:
    def __init__(self):
        """ Constructor """
        self.stackA = stacks.LinkedStack()
        self.stackB = stacks.LinkedStack()
        

    def is_empty(self):
        """Tests if the queue is logically empty"""
        return self.stackA.is_empty()


    def enqueue(self, item):
        """Puts item into the back of the queue"""
        self.stackA.push(item)


    def first(self):
        """Returns the element at the front of the queue, if it exists.
        
        Raises an IndexError if the queue is empty.
        """
        if self.stackA.is_empty() == True:                 # Raise error if stack a is empty
            raise IndexError('Stack A is empty')
        
        else:
            while self.stackA.is_empty() == False:         # While values in stack a
                temp = self.stackA.pop()                   # Pop top value and push to stack b
                self.stackB.push(temp)
            
            b_top = self.stackB.top()                      # Set b_top to the oldest element
        
            while self.stackB.is_empty() == False:         # While values in stack b
                temp = self.stackB.pop()                   # Pop values to return stack a to original
                self.stackA.push(temp)
            
            return b_top


    def dequeue(self):
        """Returns and removes the element at the front of the queue, if it exists.
        
        Raises an IndexError if the queue is empty.
        """
        if self.stackA.is_empty() == True:                 # Raise error if stack a is empty
            raise IndexError('Stack A is empty')
        
        else:
            while self.stackA.is_empty() == False:         # While values in stack a
                temp = self.stackA.pop()                   # Pop top value and push to stack b
                self.stackB.push(temp)
            
            b_top = self.stackB.top()                      # Set b_top to the oldest element
            
            self.stackB.pop()
            while self.stackB.is_empty() == False:         # While values in stack b
                temp = self.stackB.pop()                   # Pop values to return stack a to original
                self.stackA.push(temp)
            
            return b_top
        
        
    def __len__(self):
        """Returns the size of the queue."""
        return self.stackA.__len__()
    
'''
### Function Tests ###
obj = Queue()

obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)

print('Front of queue:', obj.first())
print('Removed:', obj.dequeue())
print('Front of queue:', obj.first())
print('Length is:', obj.__len__())
'''