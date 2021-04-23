#!/usr/bin/env python3

import math
import sys
lines = sys.stdin

def Volume(radius):
    return (4 / 3 * math.pi * radius ** 3)

def Area(radius):
    return (4 * math.pi * radius ** 2)

def main():
    for line in lines:
        numbers = line.strip().split()
        startR = float(numbers[0])
        incR = float(numbers[1])
        endR = float(numbers[2])
        h1 = ("Radius (m)")
        h2 = ("Area (m^2)")
        h3 = ("Volume (m^3)")
        h4 = ("-" * len(h1))
        h5 = ("-" * len(h2))
        h6 = ("-" * len(h3))
        print(f'{h1:>s} {h2:>15s} {h3:>15s}')
        print(f'{h4:>s} {h5:>15s} {h6:>15s}')
        while startR <= endR:
            print(f"{startR:10.1f} {Area(startR):15.2f} {Volume(startR):15.2f}")
            startR = startR + incR

if __name__ == '__main__':
    main()
