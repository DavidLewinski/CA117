#!/usr/bin/env python3

import sys

def l2d(file):
    lines = file.readlines()
    d = {}
    key = lines[0].split()
    value = lines[1].split()

    j = 0
    for i in key:
        d[i] = value[j]
        j = j + 1
    return d