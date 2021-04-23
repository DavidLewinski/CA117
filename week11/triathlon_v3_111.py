#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}

    def __str__(self):
        n = []
        n.append('Name: {:s}'.format(self.name))
        n.append('ID: {:d}'.format(self.tid))
        n.append('Race time: {:d}'.format(self.total_time()))
        return '\n'.join(n)

    def add_time(self, d, time):
        self.times[d] = time

    def get_time(self, n):
        if n not in self.times:
            return 'N/A'
        else:
            return self.times[n]

    def total_time(self):
        if not self.times:
            return 0
        return sum([t for t in self.times.values()])

    def __gt__(self, other):
        return self.total_time() > other.total_time()

    def __eq__(self, other):
        return self.total_time() == other.total_time()

def sort_on(n):
    return n.name

class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, n):
        self.d[n.tid] = n

    def remove(self, tid):
        del(self.d[tid])

    def lookup(self, tid):
        if tid not in self.d:
            return None
        else:
            return self.d[tid]

    def __str__(self):
        slist = ['{}'.format(t) for t in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(slist)

    def worst(self):
        return max(self.d.values())

    def best(self):
        return min(self.d.values())
