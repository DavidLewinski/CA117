#!/usr/bin/env python3

class Queue(object):
    def __init__(self):
        self.l = []

    def dequeue(self):
        return self.l.pop(0)

    def enqueue(self, e):
        self.l.append(e)

    def first(self):
        return self.l[0]

    def __len__(self):
        return len(self.l)

    def is_empty(self):
        return len(self.l) == 0
