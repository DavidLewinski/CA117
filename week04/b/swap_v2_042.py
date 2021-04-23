#!/usr/bin/env python3

import sys

def swap_unique_keys_values(d):
    value = list(d.values())
    check = {val: 1 for val in value if value.count(val) == 1}
    swapped = {v: k for (k, v) in d.items() if v in check}
    return swapped