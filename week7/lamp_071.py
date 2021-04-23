#!/usr/bin/env python3

class Lamp:
    def __init__(self, on=False):
        self.on = on

    def turn_off(self):
        self.on = False

    def turn_on(self):
        self.on = True

    def toggle(self):
        self.on = not self.on
