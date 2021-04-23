#!/usr/bin/env python3

import sys
lines = sys.stdin

def sumFac(line):
    total = 0
    i = 1
    while line >= (i * i):
        if line % i == 0:
            total = total + i
            if (line // i) != i:
                total = total + (line // i)
        i = i + 1
    return total - line

def isPerfect(n):
    n = int(n)
    if sumFac(n) == n:
        return True
    else:
        return False

def main():
    for line in lines:
        line = line.rstrip()
        print(isPerfect(line))

if __name__ == '__main__':
    main()
