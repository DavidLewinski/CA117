#!/usr/bin/env python3

import sys

def swap_keys_values(d):
    d = dict([(value, key) for key, value in d.items()])
    return d