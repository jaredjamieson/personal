# Slightly modified version of LinkedStack from Goodrich et al.
# Code Fragment 7.5-7.6 (p. 262-263)


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""
    # ----------------------- nested _Node class -------------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'     # Streamline memory usage

        def __init__(self, e, n):
            self._element = e         # Reference to item contained
            self._next = n               # Reference to next node

    # ------------------------ stack methods -----------------------------------
    def __init__(self):
        self._head = None  # Reference to head node
        self._size = 0     # Number of stack elements

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack

        :param e: New item
        :return: None
        """
        self._head = self._Node(e, self._head)  # Create and link a new node
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise IndexError if the stack is empty.

        :return: The element at the top of the stack.
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._head._element

    def pop(self):
        """Remove and return the element at the top of the stack.

        Raise IndexError if the stack is empty.

        :return: The element that was at the top of the stack before removal
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
