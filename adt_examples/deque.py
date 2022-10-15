class Deque:

    def __init__(self, n):
        self.ring = [None] * n
        self.right = 0
        self.left = 0
        self.n = n
        self.length = 0

    def append(self, x):
        if not self.length:
            self.ring[self.right] = x
        else:
            self.right = (self.right + 1) % self.n
            self.ring[self.right] = x
        self.length += 1

    def appendleft(self, x):
        if not self.length:
            self.ring[self.left] = x
        else:
            self.left = (self.left - 1) % self.n
            self.ring[self.left] = x
        self.length += 1

    def pop(self):
        self.length -= 1
        val = self.ring[self.right]
        self.ring[self.right] = None
        self.right = (self.right - 1) % self.n
        return val

    def popleft(self):
        self.length -= 1
        val = self.ring[self.left]
        self.ring[self.left] = None
        self.left = (self.left + 1) % self.n
        return val

    def peek(self):
        return self.ring[self.right]

    def peekleft(self):
        return self.ring[self.left]

    def __len__(self):
        return self.length

    def __iter__(self):
        return Deque_Iter(self)


class Deque_Iter:

    def __init__(self, deque):
        self.here = deque.left
        self._ring = deque.ring
        self.stop = deque.right
        self._n = deque.n
        self.passed_stop = 0

    def __next__(self):
        if not self.passed_stop:
            if self.here == self.stop:
                self.passed_stop = 1
            val = self._ring[self.here]
            self.here = (self.here + 1) % self._n
            return val
        else:
            raise StopIteration
