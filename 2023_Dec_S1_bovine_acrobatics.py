# using greedy algorithm
# sort by weight, then stack as many as possible on the lowest weights

import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
cows = [list(map(int, input().split())) for _ in range(n)]  # weight, amount
cows.sort(key=lambda x: x[0])  # sort by weight

inf = 1 << 60
q = deque([(-inf, m)])
ans = 0
for w, amt in cows:
    cnt = 0
    while q and w - q[0][0] >= k and amt > 0:  # while this forms a stable tower, stack more
        prev_w, prev_a = q.popleft()
        if prev_a > amt:  # more than we need
            cnt += amt
            q.appendleft((prev_w, prev_a - amt))  # add remaining back
            break
        else:  # use all
            cnt += prev_a
            amt -= prev_a

    if cnt:
        q.append((w, cnt))
        ans += cnt

print(ans)
