#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def load_loadcontacts(filename):
    d = {}
    with open(filename, 'r') as fin:
       for line in fin:
            name, number, email = line.strip().split()
            d[name] = number
            d[email] = email
    return d

d = load_loadcontacts(sys.argv[1])

for line in lines:
    name = line.strip()
    print(f"Name: {name}")
    if name in d:
        print(f"Phone: {d[name]}")
    if email in d:
        print(f"Email: {d[email]}")
    else:
        print("No such contact")
