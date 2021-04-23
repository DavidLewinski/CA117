#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        n = []
        n.append('Name: {:s}'.format(self.name))
        n.append('ID: {:d}'.format(self.tid))
        return '\n'.join(n)

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
        lst = ['{}'.format(n) for n in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(lst)
