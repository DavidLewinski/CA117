#!/usr/bin/env python3

import sys
from math import sqrt
lines = sys.stdin

def roots(lines):
    for line in lines:
        try:
            line = line.rstrip().split()
            # print(line)
            a = int(line[0])
            b = int(line[1])
            c = int(line[2])
            # print(a, b, c)
            r1 = -b + sqrt((b ** 2) - ((4 * a) * c))
            r1 = r1 / (2 * a)
            # print(r1)
            r2 = -b - sqrt((b ** 2) - ((4 * a) * c))
            r2 = r2 / (2 * a)
            print(f'r1 = {r1}, r2 = {r2}')
        except ValueError:
            print('None')

roots(lines)
