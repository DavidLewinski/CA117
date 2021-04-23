#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.rstrip()
    if line.isnumeric() == 0:
        print(f"{line} is not a number")
    else:
        print(f"Thank you for {line}")
        break
