class Circle:
    def __init__(self, r):
        self.r = r
    def __add__(a, b):
        from math import pi, sqrt
        return sqrt((pi*a.r**2 + pi*b.r**2)/pi)
    def __sub__(a, b):
        from math import pi, sqrt
        return sqrt((pi*a.r**2 - pi*b.r**2)/pi)
