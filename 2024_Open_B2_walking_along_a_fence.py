# note that there are only 1 million cells, we can keep track of the time of visit for every cell
# basically brute force simulation, to find length of path, we use (time2 - time1)

import sys

input = sys.stdin.readline
MN = 1001

N, M = map(int, input().split())
posts = [tuple(map(int, input().split())) for _ in range(M)]
posts.append(posts[0])

time = [[-1] * MN for _ in range(MN)]
cw = [0] * M
t = 0

for i in range(1, M + 1):
    x1, y1 = posts[i - 1]
    x2, y2 = posts[i]
    if x1 == x2:
        for y in range(y1, y2, -1 if y1 > y2 else 1):
            time[x1][y] = t
            t += 1
    else:
        for x in range(x1, x2, -1 if x1 > x2 else 1):
            time[x][y1] = t
            t += 1

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    diff = max(time[x1][y1], time[x2][y2]) - min(time[x1][y1], time[x2][y2])
    print(min(diff, t - diff))
