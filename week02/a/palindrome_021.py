#!/usr/bin/env python3

import sys
from string import punctuation
lines = sys.stdin.readlines()

for line in lines:
    s = line.lower().strip()
    for char in s:
        if char in punctuation or char == " ":
            s = s.replace(char, "", 1)
    print(s == s[::-1])
