#!/usr/bin/env python3

import sys

for inpt in sys.stdin:
    num = inpt.strip().split()
    reverse = num[0]
    number = reverse[::-1]
    base = num[1]
    i = 0
    total = 0
    while i < len(reverse):
        total = (int(number[i]) * int(base) ** i) + total
        i = i + 1
    print(total)
