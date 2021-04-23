#!/usr/bin/env python3

class Score(object):
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def total(self):
        return (self.points + self.goals * 3)

    def __str__(self):
        return (f'{self.goals} goal(s) and {self.points} point(s)')

    def __le__(self, other):
        return (self.total() < other.total())

    def __gt__(self, other):
        return (self.total() > other.total())

    def __eq__(self, other):
        return (self.total() == other.total())

    def __ne__(self, other):
        return (self.total() != other.total())

    def __ge__(self, other):
        return (self.total() >= other.total())

    def __le__(self, other):
        return (self.total() <= other.total())

    def __sub__(self, other):
        return (Score(self.goals - other.goals, self.points - other.points))

    def __add__(self, other):
        return (Score(self.goals + other.goals, self.points + other.points))

    def __iadd__(self, other):
        self.goals = self.goals + other.goals
        self.points = self.points + other.points
        return (self)

    def __isub__(self, other):
        self.goals = self.goals - other.goals
        self.points = self.points - other.points
        return (self)

    def __mul__(self, other):
        goals = self.goals * other
        points = self.points * other
        return Score(goals, points)

    def __rmul__(self, other):
        goals = self.goals * other
        points = self.points * other
        return Score(goals, points)

    def __imul__(self, other):
        a = self * other
        self.goals, self.points = a.goals, a.points
        return self
