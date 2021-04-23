#!/usr/bin/env python3

from math import pi
import sys

nums = sys.stdin.readlines()

for num in nums:
    position = int(num)
    print(f'{pi:.{position}f}')
