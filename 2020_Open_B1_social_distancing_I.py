# try to maximize distance while adding 2 cows
# just do binary search for the maximum d
# corner case (13): the binary searched answer is greater than the smaller distance in the original list

import sys


def works(d):
    total = 0
    if (cows[0] // 2) >= d or (n - 1 - cows[-1]) // 2 >= d:
        return True
    total += cows[0] >= d
    total += (n - 1 - cows[-1]) >= d
    for i in range(len(cows) - 1):
        if (cows[i + 1] - cows[i]) // 3 >= d:
            return True
        if (cows[i + 1] - cows[i]) // 2 >= d:
            total += 1
    return total >= 2


n = int(input())
pos = input()
cows = [i for i in range(n) if pos[i] == "1"]

d = [cows[i + 1] - cows[i] for i in range(len(cows) - 1)]
if not d:
    d = [float('inf')]

if not cows:
    print(n - 1)
    sys.exit()

low = 1
high = n
while low <= high:
    mid = (low + high) // 2
    if not works(mid):
        high = mid - 1
    else:
        low = mid + 1

print(min(min(d), low - 1))
