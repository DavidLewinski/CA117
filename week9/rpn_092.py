#!/usr/bin/env python3

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

def calculator(line):
    s = Stack()
    line = line.rstrip().split()
    rn = ["r", "n"]
    sym = ["+", "-", "*", "/"]
    for each in line:
        if (each not in rn) and (each not in sym):
            s.push(each)
        elif each in rn:
            num = float(s.pop())
            s.push(calc1(each, num))
        elif each in sym:
            num1 = float(s.pop())
            num2 = float(s.pop())
            s.push(calc2(each, num1, num2))
    return float(s.top())

def calc1(sym, num):
    if sym == "r":
        return (num ** (1 / 2))
    elif sym == "n":
        return -num

def calc2(sym, num1, num2):
    if sym == "+":
        return num1 + num2
    elif sym == "/":
        return num2 / num1
    elif sym == "*":
        return num1 * num2
    elif sym == "-":
        return num2 - num1
