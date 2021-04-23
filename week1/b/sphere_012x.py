#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    args = line.strip().split()
    print(args)
    startR = float(args[0])
    print(startR)
    incrementR = float(args[1])
    print(incrementR)
    endR = float(args[2])
    h1 = "Radius (m)"
    h4 = "-" * len(h1)
    h2 = "Area (m^)"
    h5 = "-" * len(h2)
    h3 = "Volume (m^3)"
    h6 = "-" * len(h3)
    print(f"{h1:>s} {h2:>15s} {h3:>15s}")
    print(f"{h4:>s} {h5:>15s} {h6:>15s}")
