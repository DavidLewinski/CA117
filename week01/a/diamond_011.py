#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    num = int(line.strip())
    character = "* "
    whitespace = " "

    i = num
    while i != 0:
        print((i - 1) * whitespace + character * (((num - i + 1)) - 1) + "*")
        i = i - 1

    num = num - 1
    i = 0
    while num != 0:
        i = i + 1
        print((whitespace * (i)) + (((num) - 1) * character) + "*")
        num = num - 1
