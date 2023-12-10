import sys
from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[b].append(a)  # reverse tree


def bfs(start):
    vis = [False] * (n + 1)
    vis[start] = True
    q = deque([start])
    while q:
        cur = q.popleft()
        for adj in graph[cur]:
            vis[adj] = True
            q.append(adj)
    return sum(vis) == n


for i in range(1, n + 1):
    if bfs(i):
        print(i)
        sys.exit()
print(-1)
