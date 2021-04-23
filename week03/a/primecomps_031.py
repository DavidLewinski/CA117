#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    nums = line.strip()
    nums = int(nums)
    primes = []
    for num in range(0, nums + 1):
        if num > 1:
            r = range(2, num)
            for i in r:
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    print("Primes:", primes)