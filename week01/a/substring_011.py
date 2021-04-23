#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for a in lines:
    s = a.rstrip().lower().split()
    character = s[0]
    word = s[1]
    if character in word:
        print("True")
    else:
        print("False")
