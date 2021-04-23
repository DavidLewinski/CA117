#!/usr/bin/env python3

from math import sqrt

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    d = sqrt((x2 - x1) ** 2) + sqrt((y2 - y1) ** 2)
    if d - r1 - r2 < 0:
        return True
    else:
        return False
