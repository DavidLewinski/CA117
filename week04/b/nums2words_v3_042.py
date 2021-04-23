#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
irishd = {word.split()[0]: word.split()[1] for word in open(sys.argv[1]).readlines()}

for line in lines:
    line = line.strip().split()
    translated = []
    d = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}
    for num in line:
        if num in d:
            translated.append(irishd[d[num]])
        if num not in d:
            translated.append("unknown")
    print(' '.join(translated))