#!/usr/bin/env python3

import sys

class Stack(object):
    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

def matcher(line):
    d = {
        '}': '{', ']': '[', ')': '('
    }
    s = Stack()
    try:
        for each in line:
            if each in d.values():
                s.push(each)
            if each in d.keys():
                if d[each] != s.pop():
                    return False
    except IndexError:
        return False
    return s.is_empty()
