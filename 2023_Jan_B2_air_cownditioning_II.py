# brute force
# you can use bitmask to iterate over states

def satisfied(arr):
    for s, e, req in cows:
        if not all(i >= req for i in arr[s:e + 1]):
            return False
    return True


n, m = map(int, input().split())
cows = [tuple(map(int, input().split())) for _ in range(n)]  # (start, end, req)
cool = [tuple(map(int, input().split())) for _ in range(m)]  # (start, end, cool, cost)

best = 1 << 30
for state in range(1 << m):
    cooling = [0] * 100
    total_cost = 0
    for i, (s, e, c, cost) in enumerate(cool):
        if state & (1 << i):
            total_cost += cost
            for loc in range(s, e + 1):
                cooling[loc] += c

    if satisfied(cooling):
        best = min(best, total_cost)

print(best)
