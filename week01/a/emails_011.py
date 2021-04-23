#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    line1 = line.split("@")
    line2 = line1[0]
    line3 = line2.split(".")
    firstname = line3[0]
    secondname = line3[1]

    i = 0
    while i < len(secondname):
        if secondname[i].isdigit():
            secondname = str(secondname[0:i])
        i = i + 1
    print(firstname.title(), secondname.title())
