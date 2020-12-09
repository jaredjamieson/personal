# Author: Brian O'Neill
# Combined module for priority queue implementations for the Goodrich et. al
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


class PriorityQueueBase:
    """Abstract base class for a priority queue"""

    class _Item:
        """Lightweight composite to store priority queue items"""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    # Concrete method assuming abstract len()
    def is_empty(self):
        """Return True if the priority queue is empty"""
        return len(self) == 0

    def __len__(self):
        raise NotImplementedError('Must be implemented by subclass')

    def add(self, key, value):
        raise NotImplementedError('Must be implemented by subclass')

    def min(self):
        raise NotImplementedError('Must be implemented by subclass')

    def remove_min(self):
        raise NotImplementedError('Must be implemented by subclass')


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap"""
    # non-public behaviors

    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)      # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)     # index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)                    # recurse at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)         # recurse at position of small_child

    def _heapify(self):
        start = self._parent(len(self)-1)       # start at PARENT of last leaf
        for j in range(start, -1, -1):          # going up to and including the root
            self._downheap(j)

    # public behaviors
    def __init__(self, contents=()):
        """Create a new empty Priority Queue.

        By default, the queue will be empty. If contents is given, it should be as an
        iterable sequence of (k,v) tuples specifying the initial contents.
        """
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()

    def __len__(self):
        """Return the number of items in the priority queue"""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data)-1)             # upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key

        Raise exception if empty
        """
        if self.is_empty():
            raise Exception('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key

        Raise exception if empty.
        """
        if self.is_empty():
            raise Exception('Priority queue is empty')
        self._swap(0, len(self._data)-1)    # Put minimum item at the end
        item = self._data.pop()             # And remove it from the list
        self._downheap(0)                   # Then fix the new root
        return (item._key, item._value)
