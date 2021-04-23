#!/usr/bin/env python3

import sys
lines = sys.stdin

d = {}
d_reverse = {}
for line in lines:
    line = line.split()
    try:
        if line[0] == "def":
            d[line[1]] = int(line[2])
            d_reverse[int(line[2])] = line[1]
            for (k, v) in (d.items()):
                v = int(v)
            for (kr, vr) in (d_reverse.items()):
                kr = int(kr)
        if line[0] == "calc":
            calc = line[1:]
            i = 0
            total = d[calc[0]]
            while i < len(calc):
                if calc[i] == "-":
                    total = total - d[calc[i + 1]]
                if calc[i] == "+":
                    total = total + d[calc[i + 1]]
                i = i + 1
            print(" ".join(calc), d_reverse[total])
        if "clear" in line:
            d = {}
            d_reverse = {}
    except KeyError:
        print(" ".join(calc), "unknown")
    except IndexError:
        pass
