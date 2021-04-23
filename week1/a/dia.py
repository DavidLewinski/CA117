#!/usr/bin/env python3

import sys

x = sys.stdin.readline()

i = 0
while i < len(x):
    number = int(x[i].rstrip())

    j = 1
    while j <= number:
        print((" " * (number - j) + (("*" + " ") * j)).rstrip())
        j = j + 1

    j = 1
    while j < number:
        print((" " * (j) + (("*" + " ") * (number - j))).rstrip())
        j = j + 1

    i = i + 1
