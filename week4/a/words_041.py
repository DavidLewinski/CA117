#!/usr/bin/env python3

import sys
from string import punctuation

for line in sys.stdin:
    line = line.rstrip()
    lline = line.lower()
    linelist = line.split()
#    print(len(linelist))
    number = 0
    i = 0
    while i < len(linelist):
#        print(linelist[i])
        if "a" in linelist[i]:
            number = number + 1
        i = i + 1
#    print(f"{linelist} : {number}")
