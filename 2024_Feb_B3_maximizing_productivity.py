# typical offline query problem
# also use binary search

import sys
from bisect import bisect_right

input = sys.stdin.readline
N, Q = map(int, input().split())
close = list(map(int, input().split()))
vis = list(map(int, input().split()))

queries = [tuple(map(int, input().split())) + (i,) for i in range(Q)]
ans = [None] * Q
queries.sort(key=lambda x: x[0])  # sort by start

diff = [i - j for i, j in zip(close, vis)]
diff.sort()
# print(diff)

for v, s, idx in queries:
    pos = N - bisect_right(diff, s)  # "strictly before", so we need bisect_right
    if pos >= v:
        ans[idx] = "YES"
    else:
        ans[idx] = "NO"

print("\n".join(ans))
