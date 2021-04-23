#!/usr/bin/env python3

import sys
def procfile(filename):
    try:
        with open(filename, "r") as f:
            bestMark = -1
            for line in f:
                try:
                    mark, name = line.strip().split(maxsplit=1)
                    mark = int(mark)
                    if mark > bestMark:
                        bestMark, bestStudent = mark, [name]
                    elif mark == bestMark:
                        bestStudent.append(name)
                except ValueError:
                    print(f"Invalid mark {mark} encountered. Skipping.")
            print(f'Best student(s): {", ".join(bestStudent)}')
            print(f"Best mark: {bestMark}")
    except IndexError:
        print("Index Error")
procfile(sys.argv[1])
