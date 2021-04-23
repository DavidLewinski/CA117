#!/usr/bin/env python3

import sys

a = sys.stdin.readlines()
string = "".join(a).rstrip()
complete = string.title()
print(complete)
