#!/usr/bin/env python3

import sys

for temp in sys.stdin:
    lines = temp.strip().split()

    i = 0
    while i < len(lines):
        words = lines[i]
        last = words[len(words) - 1].upper()
        body = words[0:len(words) - 1]
        lines[i] = body + last
        i = i + 1
    print(" ".join(lines))
