# ad hoc: observation is hard, implementation is easy
#
# Key observation:
# - in the array [1, 2, 4, 3], 4 is out of place
# - to access 4, we first need to move 1 and 2 to their respective locations
# - in total, we only need to move the first 3 element
#
# therefore, we can conclude that the number of moves is the index of the first element that
# breaks the ascending order

import sys

sys.stdin = open('sleepy.in', 'r')
sys.stdout = open('sleepy.out', 'w')

n = int(input())
arr = list(map(int, input().split()))

for i in reversed(range(n - 1)):
    if arr[i] > arr[i + 1]:
        print(i + 1)
        sys.exit()

print(0)
