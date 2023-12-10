from collections import deque
import sys

n = 10
arr = [list(input()) for _ in range(10)]

goal = None
for i in range(n):
    for j in range(n):
        if arr[i][j] == "B":
            goal = i, j
        elif arr[i][j] == "L":
            q = deque([(0, i, j)])

while q:
    cur, i, j = q.popleft()

    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ni, nj = i + dr, j + dc
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != "R":
            if arr[ni][nj] == "B":
                print(cur)
                sys.exit()
            arr[ni][nj] = "R"  # visited
            q.append((cur + 1, ni, nj))
