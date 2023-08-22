# using a 2D difference array, then prefix sum

import sys

# # uncomment this when submitting, comment when running in regular coding environment (IDE)
# sys.stdin = open('paintbarn.in', 'r')
# sys.stdout = open('paintbarn.out', 'w')

N, K = map(int, input().split())

diff = [[0] * 1001 for _ in range(1001)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    diff[x1][y1] += 1
    diff[x2][y2] += 1
    diff[x2][y1] -= 1
    diff[x1][y2] -= 1

arr = [[0] * 1001 for _ in range(1001)]
for i in range(1000):
    for j in range(1000):
        # turn into actual array using a PSA
        arr[i+1][j+1] = arr[i+1][j] + arr[i][j+1] + diff[i][j] - arr[i][j]

# for i in arr[:10]:
#     print(i[:10])
print(sum([row.count(K) for row in arr]))
