#!/usr/bin/env python3

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def midpoint(self, other):
        x = ((other.x + self.x) / 2)
        y = ((other.y + self.y) / 2)
        return Point(x, y)

class Circle(object):
    def __init__(self, c=None, r=0):
        if c is None:
            c = Point()
        self.centre = c
        self.radius = r

    def __add__(self, other):
        c = (self.centre.midpoint(other.centre))
        r = (self.radius + other.radius)
        return (Circle(c, r))

    def __str__(self):
        return f'Centre: {self.centre}\nRadius: {self.radius}'
