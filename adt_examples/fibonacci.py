class Fib:

    def __init__(self):
        self.current = 1
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.next
        self.next += self.current
        self.current = tmp
        return self.current