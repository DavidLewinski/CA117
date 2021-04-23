#!/usr/bin/env python3

import sys

for a in sys.stdin:
    a = a.rstrip()
    removed = a[1:len(a) - 1]
    if len(removed) > 0:
        print(removed)
