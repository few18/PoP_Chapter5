class Fib:
    """Class to compute fibonacci sequence."""

    def __init__(self):
        """Initialise the fibonacci class."""
        self.current = 1
        self.next = 1

    def __iter__(self):
        """Method for iteration protocol."""
        return self

    def __next__(self):
        """Mehtod to determine next element of iteration."""
        tmp = self.next
        self.next += self.current
        self.current = tmp
        return self.current
