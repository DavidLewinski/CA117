#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def add_time(self, type, time):
        if type == 'swim':
            self.swim = time
        elif type == 'cycle':
            self.cycle = time
        elif type == 'run':
            self.run = time

    def get_time(self, type):
        if type == 'swim':
            return self.swim
        elif type == 'cycle':
            return self.cycle
        elif type == 'run':
            return self.run

    def __eq__(self, num):
        return (self.swim + self.cycle + self.run) == (num.swim + num.cycle + num.run)

    def __gt__(self, num):
        return (self.swim + self.cycle + self.run) > (num.swim + num.cycle + num.run)

    def __lt__(self, num):
        return (self.swim + self.cycle + self.run) < (num.swim + num.cycle + num.run)

    def __str__(self):
        return (f'Name: {self.name}\nID: {self.tid}\nRace time: {self.run + self.cycle + self.swim}')
