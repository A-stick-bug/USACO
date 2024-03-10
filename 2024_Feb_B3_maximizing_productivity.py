# just binary search

import sys
from bisect import bisect_right

input = sys.stdin.readline
N, Q = map(int, input().split())
close = list(map(int, input().split()))
vis = list(map(int, input().split()))

diff = [i - j for i, j in zip(close, vis)]
diff.sort()
# print(diff)

for _ in range(Q):
    v,s = map(int, input().split())
    pos = N - bisect_right(diff, s)  # "strictly before", so we need bisect_right
    if pos >= v:
        print("YES")
    else:
        print("NO")

