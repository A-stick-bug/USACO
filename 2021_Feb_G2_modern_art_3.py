# https://dmoj.ca/problem/usaco21febg2
# interval DP
# Pretty much just trial and error until you get a transition that works

n = int(input())
arr = list(map(int, input().split()))

inf = 301
dp = [[inf] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1  # base case: 1 stroke to paint a cell

for length in range(1, n):
    for i in range(n - length):
        j = i + length
        # try all ways of making an interval with 2 smaller intervals
        for mid in range(i, j):  # try all splits [i,m] + [m+1,r]
            ans = dp[i][mid] + dp[mid + 1][j]
            # if the start and end are equal, we can fill [start,end] to save a move
            # everything in the middle will get override later on anyway
            if arr[i] == arr[j]:
                ans -= 1
            dp[i][j] = min(dp[i][j], ans)

print(dp[0][n - 1])
