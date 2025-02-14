# USACO 2025 January Silver P1 - Cow Checkups
# https://dmoj.ca/problem/usaco25jans1
# Line sweep with basic combinatorics

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

loc_a = defaultdict(list)
for i in range(n):
    loc_a[a[i]].append(i)

loc_b = defaultdict(list)
for i in range(n):
    loc_b[b[i]].append(i)

total = 0
for i in range(n):  # handle equal elements
    if a[i] == b[i]:  # all subarrays excluding this element
        left = i * (i + 1) // 2
        rt = n - i - 1
        right = rt * (rt + 1) // 2
        total += left + right

for t in range(1, n + 1):
    # line sweep
    events = []
    for c in loc_b[t]:
        a, b = min(c, n - c - 1), max(c, n - c - 1)
        events.append((a, 1))
        events.append((b + 1, -1))
    events.sort()

    inner_add = 0
    outer_add = len(loc_b[t])
    idx = 0
    for cur in loc_a[t]:
        while idx < len(events) and events[idx][0] <= cur:  # process events
            i, t = events[idx]
            idx += 1

            outer_add -= t
            if t == 1:
                inner_add += i + 1
            else:
                inner_add -= n - i + 1

        total += outer_add * (min(cur, n - cur - 1) + 1)
        total += inner_add

print(total)
