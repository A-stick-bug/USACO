# find the smallest n, where all substrings of length n are distinct

import sys

# uncomment this when submitting, comment when running in regular coding environment (IDE)
sys.stdin = open('whereami.in', 'r')
sys.stdout = open('whereami.out', 'w')

n = int(input())
houses = input()

for length in range(1, n + 1):  # test every length
    substrings = set()
    found = True

    for i in range(n - length + 1):  # go through every substring of that length
        sub = houses[i:i + length]
        if sub in substrings:  # repeated substring, means that this length won't work
            found = False
            break
        substrings.add(sub)

    if found:
        print(length)
        break
