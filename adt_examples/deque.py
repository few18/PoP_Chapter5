"""
This module implements a deque type data structure.
"""


class Deque:
    """Implementation of Deque type struct."""

    def __init__(self, n):
        """Initialise the deque."""
        self.ring = [None] * n
        self.right = 0
        self.left = 0
        self.n = n
        self.length = 0

    def append(self, x):
        """Implement method to right append value to deque."""
        if not self.length:
            self.ring[self.right] = x
        else:
            self.right = (self.right + 1) % self.n
            self.ring[self.right] = x
        self.length += 1

    def appendleft(self, x):
        """Implement method to left append value to deque."""
        if not self.length:
            self.ring[self.left] = x
        else:
            self.left = (self.left - 1) % self.n
            self.ring[self.left] = x
        self.length += 1

    def pop(self):
        """Implement method to pop element from the right."""
        self.length -= 1
        val = self.ring[self.right]
        self.ring[self.right] = None
        self.right = (self.right - 1) % self.n
        return val

    def popleft(self):
        """Implement method to pop element from the left."""
        self.length -= 1
        val = self.ring[self.left]
        self.ring[self.left] = None
        self.left = (self.left + 1) % self.n
        return val

    def peek(self):
        """Implement method to peek at rightmost element."""
        return self.ring[self.right]

    def peekleft(self):
        """Implement method to peek at leftmost element."""
        return self.ring[self.left]

    def __len__(self):
        """Method to determine length of deque."""
        return self.length

    def __iter__(self):
        """Method for Iter protocol."""
        return DequeIter(self)


class DequeIter:
    """Iteration object for protocol."""

    def __init__(self, deque):
        """Initialise the iter object."""
        self.here = deque.left
        self._ring = deque.ring
        self.stop = deque.right
        self._n = deque.n
        self.passed_stop = 0

    def __next__(self):
        """Method to determine next element of iteration."""
        if not self.passed_stop:
            if self.here == self.stop:
                self.passed_stop = 1
            val = self._ring[self.here]
            self.here = (self.here + 1) % self._n
            return val
        else:
            raise StopIteration
