# Q: Given a set of bitmasks states, for each state, find the maximum distance to another state
# Note: maximum distance is just (C minus the minimum distance of the state's inverse)
# We can use DP-like transitions to get the min distance to existing states

C, N = map(int, input().split())

dist = [100] * (1 << C)  # minimum distance from i to a valid state
queries = []
for _ in range(N):
    s = input()
    state = 0  # store as bitmask
    for i in range(C):
        if s[i] == "H":
            state |= 1 << i
    dist[state] = 0
    queries.append(state)

for i in range(C):
    for state in range(1 << C):  # not sure why this transition works
        dist[state] = min(dist[state], dist[state ^ (1 << i)] + 1)

for state in queries:
    inv = 0
    for i in range(C):  # get state's inverse
        if not (state & (1 << i)):
            inv += 1 << i
    print(C - dist[inv])
