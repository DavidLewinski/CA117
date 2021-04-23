#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, address, sid):
        self.name = name
        self.address = address
        self.sid = sid
        self.d = {}

    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nID: {self.sid}}'

    def add_mark(self, module, mark):
        self.d[module] = mark

    def get_mark(self, module):
        if module in self.d.keys():
            return self.d[module]
        else:
            return "Not registered for module"
