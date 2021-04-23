#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    list = line.casefold().split(" ")
    a = list[0].rstrip()
    for s in list[1]:
        a = a.replace(s, "", 1)
    if len(a) > 0:
        print("False")
    else:
        print("True")
