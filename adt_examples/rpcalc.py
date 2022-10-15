"""
This module implements a reverse polish calculator.
"""


import math


class RPCalc:
    """Class to implement reverse polish calculator."""

    def __init__(self):
        """Initialise stack for calculator."""
        self.stack = []
        self.operators = ("+", "-", "*", "/", "sin", "cos")

    def push(self, n):
        """Implement method for pushing to stack."""
        if n not in self.operators:
            self.stack.append(n)
        else:
            if n == "sin":
                num = self.pop()
                self.stack.append(math.sin(num))
            elif n == "cos":
                num = self.pop()
                self.stack.append(math.cos(num))
            elif n == "+":
                num2 = self.pop()
                num1 = self.pop()
                self.stack.append(num1 + num2)
            elif n == "-":
                num2 = self.pop()
                num1 = self.pop()
                self.stack.append(num1 - num2)
            elif n == "*":
                num2 = self.pop()
                num1 = self.pop()
                self.stack.append(num1 * num2)
            elif n == "/":
                num2 = self.pop()
                num1 = self.pop()
                self.stack.append(num1 / num2)

    def pop(self):
        """Implement method to pop stack."""
        return self.stack.pop()

    def peek(self):
        """Implement method to peek at stack."""
        return self.stack[-1]

    def __len__(self):
        """Method for determining number of elements in stack."""
        return len(self.stack)
