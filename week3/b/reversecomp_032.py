#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
reverse = []
def reversed(line):
    i = 0
    j = len(reverse)
    while i < j:
        a = (i + j) // 2
        if reverse[a].lower() < line:
            i = a + 1
        else:
            j = a
    return reverse[i].lower() == line

for line in lines:
    line = line.strip()
    lline = line.lower()
    if len(line) >= 5:
        reverse.append(line)
    else:
        continue

print(f"{[n for n in reverse if reversed(n[::-1].lower())]}")