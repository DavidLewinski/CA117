#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, address, sid):
        self.name = name
        self.address = address
        self.sid = sid

    def __str__(self):
        n = []
        n.append('Name: {:s}'.format(self.name))
        n.append('Address: {:s}'.format(self.address))
        n.append('ID: {:d}'.format(self.sid))
        return '\n'.join(n)

def sort_on(n):
    return n.sid

class Classlist(object):
    def __init__(self):
        self.d = {}

    def add(self, s):
        self.d[s.sid] = s

    def remove(self, sid):
        del(self.d[sid])

    def lookup(self, sid):
        if sid in self.d:
            return self.d[sid]
        else:
            return None

    def __str__(self):
        lst = ['{}'.format(t) for t in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(lst)
