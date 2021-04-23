#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
total = 0

for line in lines:
    tokens = line.strip().split()
    total = total + len(tokens)

print(total)
