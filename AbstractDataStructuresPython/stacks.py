# Author: Brian O'Neill
# Combined module for array-based and linked stacks for the Goodrich et. al
# data structures textbook. Created for CS/IT 200 class.
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

    def __init__(self):
        """Constructor"""
        self._data = []

    def __len__(self):
        """Return number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e) # Store the new item at the end of the list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the element at the top of the stack.

        Raise IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._data.pop()

    def __str__(self):
        return str(self._data)


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

    def __str__(self):
        current = self._head
        listform = [None] * self._size
        for i in range(self._size-1, -1, -1):
            listform[i] = current._element
            current = current._next
        return str(listform)
