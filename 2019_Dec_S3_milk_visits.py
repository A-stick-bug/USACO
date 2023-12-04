# I overcomplicated this way too much...
# unless you really like tree LCA, you should probably go find a better solution
# turn the entire question into 0-indexing
# the question is like weighted graph with weights 0 and 1, but the weights are on the nodes, not the edges

from math import log2
import sys
sys.setrecursionlimit(100000)

class LCA:
    def __init__(self):
        self.depth = [0] * N
        self.first = [0] * N
        self.euler = []
        self.st = [[(0, 0)] * 18 for _ in range(2 * N)]

        self.dfs(0, -1)
        M = len(self.euler)
        LOG = int(log2(M))
        for i in range(M):
            self.st[i][0] = (self.depth[self.euler[i]], self.euler[i])
        for k in range(1, LOG + 1):
            for i in range(M - (1 << k) + 1):
                self.st[i][k] = min(self.st[i][k - 1], self.st[i + (1 << k - 1)][k - 1])

    def dfs(self, u, prev):
        self.first[u] = len(self.euler)
        self.euler.append(u)
        for v in graph[u]:
            if v != prev:
                self.depth[v] = self.depth[u] + 1
                self.dfs(v, u)
                self.euler.append(u)

    def lca(self, u, v):
        left = min(self.first[u], self.first[v])
        right = max(self.first[u], self.first[v])
        k = int(log2(right - left + 1))
        return min(self.st[left][k], self.st[right - (1 << k) + 1][k])[1]


input = sys.stdin.readline
N, Q = map(int, input().split())  # N nodes, Q queries
cows = list(map(lambda x: 1 if x == "H" else 0, list(input().strip())))  # 0: G, 1: H

graph = [[] for _ in range(N)]  # create graph from input
for i in range(1, N):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

h_cow = [0] * N
h_cow[0] = cows[0]


def h_cows(cur, prev):
    for adj in graph[cur]:
        if adj == prev:
            continue
        h_cow[adj] = h_cow[cur] + cows[adj]
        h_cows(adj, cur)


h_cows(0, -1)
tree = LCA()

for _ in range(Q):
    q = input().split()
    u, v = map(int, q[:2])
    u -= 1
    v -= 1
    ancestor = tree.lca(u, v)
    h_nodes = h_cow[u] + h_cow[v] - 2 * h_cow[ancestor] + cows[ancestor]
    total_nodes = tree.depth[u] + tree.depth[v] - 2 * tree.depth[ancestor] + 1
    if (q[2] == "H" and h_nodes) or (q[2] == "G" and total_nodes != h_nodes):
        print(1, end="")
    else:
        print(0, end="")

print()  # newline
