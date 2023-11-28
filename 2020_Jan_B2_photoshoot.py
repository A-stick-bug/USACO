# the entire sequence depends on the first number, so we just try every possible number for the first one
# and take the lexicographically least one (after making sure it is valid)

def build(start):
    """try to build valid array from the first number"""
    arr = [0] * n
    arr[0] = start
    for i in range(1, n):
        arr[i] = adj[i - 1] - arr[i - 1]
    if sorted(arr) == match:
        return arr
    else:  # if it's not valid, we can just return a lexicographically big array, doesn't really matter
        return match[::-1]


n = int(input())
adj = list(map(int, input().split()))

match = list(range(1, n + 1))  # the sorted sequence has to match this to be a permutation

res = min(build(first) for first in range(1, adj[0]))
print(*res)
