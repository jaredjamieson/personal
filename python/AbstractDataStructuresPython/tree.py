class Tree:
    """Abstract base class representing a tree structure"""

    #-------------------- nested Position class ---------------------
    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            raise NotImplementedError('Must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not(self == other)

    #--- abstract methods that concrete subclass must support -----------

    def root(self):
        """Return Position representing the tree's root (or None if empty)"""
        raise NotImplementedError('Must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)"""
        raise NotImplementedError('Must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that p has"""
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError('Must be implemented by subclass')

    #--- concrete methods implemented in this class --------------------

    def is_root(self, p):
        """Return True if Position p represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self) == 0

    # -------------- traversal methods ---------------------------------
    def preorder(self):
        """Generate a preorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):   # Start recursion
                yield p

    def _subtree_preorder(self, p):
        yield p                                         # Visit p before its subtrees
        for c in self.children(p):                      # For each child c
            for other in self._subtree_preorder(c):     # Do preorder of c's subtree
                yield other                             # Yielding each

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):                      # For each child c
            for other in self._subtree_postorder(c):    # Do postorder of c's subtree
                yield other                             # Yielding each
        yield p                                         # Visit p after its subtrees
