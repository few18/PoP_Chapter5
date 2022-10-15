import math


class RPCalc:

    def __init__(self):
        self.stack = []
        self.operators = ("+", "-", "*", "/", "sin", "cos")

    def push(self, n):
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
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)