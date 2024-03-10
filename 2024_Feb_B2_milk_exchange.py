# if there is a RL, no milk is lost here
# if there is a chain (RRR or LLL) that ends up at a RL, min(sum of chain, M) is lost in this chain
# use disjoint set to keep track of chains

import sys


class DisjointSet:
    def __init__(self, N):
        self.parent = [i for i in range(N + 1)]  # disjoint set stuff
        self.size = [1] * (N + 1)

    def find(self, node):
        if self.parent[node] != node:  # go up until we reach the root
            # attach everything on our way to the root (path compression)
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        if self.size[root_b] > self.size[root_a]:  # join the smaller to the larger
            root_a, root_b = root_b, root_a  # swap
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]


N, M = map(int, input().split())
dir = input()
arr = list(map(int, input().split()))

if len(set(list(dir))) == 1:  # corner case: everything is in 1 cycle
    print(sum(arr))
    sys.exit()

pair = [False] * N  # RL pairs
for i in range(N - 1):
    if dir[i] == "R" and dir[i + 1] == "L":
        pair[i] = pair[i + 1] = True
if dir[-1] == "R" and dir[0] == "L":
    pair[0] = pair[-1] = True

chains = [0] * N
ds = DisjointSet(N)
for i in range(N):
    if pair[i]:
        continue
    if dir[i] == "R" and dir[(i + 1) % N] == "R":
        ds.union(i, (i + 1) % N)
    elif dir[i] == "L" and dir[(i - 1) % N] == "L":
        ds.union(i, (i - 1) % N)

for i in range(N):
    if pair[i]:
        continue
    chains[ds.find(i)] += arr[i]
print(sum(arr) - sum(min(M, i) for i in chains))
