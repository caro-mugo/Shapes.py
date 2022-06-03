import math

class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        A=3.14*(self.r**2)
        return A
