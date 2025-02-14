"""
TLE, THIS IS A BRUTE FORCE SOLUTION

USACO 2025 January Silver P3 - Table Recovery
https://dmoj.ca/problem/usaco25jans3

find best isomorphic match that satisfies:
- achievable by swapping rows and columns from a N by N addition grid
   - frequencies are identical to the sorted ver
- lex min

TC: O(2^n * n^3)
"""

from collections import Counter, defaultdict


def sort_by_col(grid):
    cop = [row.copy() for row in grid]
    cop = list(zip(*cop))
    cop.sort()
    cop = list(zip(*cop))
    return [list(row) for row in cop]


def works(res):
    c = [i.copy() for i in res]
    for _ in range(3 * n):
        c = sorted(c)
        c = sort_by_col(c)
    return c == target


def is_smaller(a, b):
    for i in range(n):
        for j in range(n):
            if a[i][j] < b[i][j]:
                return 1
            if a[i][j] > b[i][j]:
                return -1
    return 0


def get_freqs(a):
    freq = Counter()
    for row in a:
        for i in row:
            freq[i] += 1
    freq = list(freq.items())
    f2 = defaultdict(list)
    for k, v in freq:
        f2[v].append(k)
    return f2


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

if n <= 8:  # just bitmask for small cases
    t_freq = Counter()
    target = []
    for row in range(n):
        target.append([i + row for i in range(2, n + 2)])
        for i in target[row]:
            t_freq[i] += 1

    tf = get_freqs(target)
    gf = get_freqs(grid)

    pairs = [(gf[i], tf[i]) for i in range(1, n + 1)]

    # print(tf)
    # print(gf)
    # print(pairs)

    # END PRECOMPUTATION
    # BEGIN BITMASK

    inf = 1 << 30
    best = [[inf] * n for _ in range(n)]
    for mask in range(1 << len(pairs)):
        state = [[-1] * n for _ in range(n)]
        table = {}

        for bit in range(len(pairs)):
            val = bool(mask & (1 << bit))
            if len(pairs[bit][0]) == 1:  # diagonal
                table[pairs[bit][0][0]] = pairs[bit][1][0]
            else:
                table[pairs[bit][0][0]] = pairs[bit][1][val]
                table[pairs[bit][0][1]] = pairs[bit][1][val ^ 1]

        for i in range(n):
            for j in range(n):
                state[i][j] = table[grid[i][j]]

        # if works(state):
        #     print(state)

        if works(state) and is_smaller(state, best) == 1:
            best = state

    for row in best:
        print(" ".join(map(str, row)))

else:  # do whatever
    print("test")


"""
[2 - 5]
[3 - 6]
[4 - 7]
[5 - 8]
"""