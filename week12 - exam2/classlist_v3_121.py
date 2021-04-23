#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, address, sid):
        self.name = name
        self.address = address
        self.sid = sid
        self.scores = {}

    def __str__(self):
        n = []
        n.append('Name: {:s}'.format(self.name))
        n.append('Address: {:s}'.format(self.address))
        n.append('ID: {:d}'.format(self.sid))
        return '\n'.join(n)

    def add_mark(self, module, mark):
        self.scores[module] = mark

    def get_mark(self, module):
        if module in self.scores.keys():
            return self.scores[module]
        else:
            return "Not registered for module"

def sort_on(n):
    return n.sid

class Classlist(object):
    def __init__(self):
        self.list = {}

    def add(self, student):
        self.list[student.sid] = student

    def lookup(self, sid):
        if sid in self.list.keys():
            return self.list[sid]
        else:
            return None

    def remove(self, sid):
        if sid in self.list.keys():
            return self.list.pop(sid)
        else:
            return None

    def least_popular_module(self):
        modules = []
        for (sid, other) in self.list.items():
            # modules = [module for module in other.scores.keys()]
            for module in other.scores.keys():
                modules.append(module)
        leastpop = len(modules)
        for module in modules:
            if modules.count(module) < leastpop:
                leastpop, name = modules.count(module), module
        return name
