"""
USACO 2025 January Silver P2 - Farmer John's Favorite Operation
https://dmoj.ca/problem/usaco25jans2

Observations:
- only care about numbers mod m
- optimal always involves shifting to make a number 0

Keep track of numbers < m/2 and > m/2 separately
- Use deques to shift elements from one to the other efficiently
"""

from collections import deque


def solve():
    n, m = map(int, input().split())
    arr = list(map(lambda x: int(x) % m, input().split()))
    arr.sort()

    best = sum(min(i, m - i) for i in arr)  # no change

    deltas = [0] + arr + [m - i for i in arr]
    deltas.sort()

    # all values represented by arr[i] + lazy
    lazy = 0
    hf = m / 2

    less = deque([i for i in arr if i <= m - i])
    more = deque([i for i in arr if i > m - i])

    total = best
    for i in range(1, len(deltas)):
        change = deltas[i] - deltas[i - 1]
        if change == 0:
            continue

        while less and less[-1] + lazy + change > hf:  # transfer less to more
            total -= less[-1] + lazy
            total += m - (less[-1] + lazy)
            more.appendleft(less.pop())

        lazy += change
        total += len(less) * change

        total -= len(more) * change
        while more and more[-1] + lazy >= m:  # transfer more to less
            less.appendleft(more.pop() - m)

        best = min(best, total)

    print(best)


t = int(input())
for _ in range(t):
    solve()

"""
2
5 9
15 12 18 3 8

1
3 69
1 988244353 998244853
"""
