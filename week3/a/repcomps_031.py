#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def removethree(nums):
    line = range(1, nums + 1)
    line = list(line)
    multiof3 = ["X" if (n % 3 == 0) else n for n in line]
    print("Multiples of 3 replaced:", str(multiof3))

for nums in lines:
    nums = nums.rstrip()
    removethree(int(nums))