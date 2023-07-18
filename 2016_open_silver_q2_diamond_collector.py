import sys

sys.stdin = open('diamond.in', 'r')
sys.stdout = open('diamond.out', 'w')


n, k = map(int, input().split())
diamonds = [int(input()) for _ in range(n)]
diamonds.sort()

# let max_d be 'maximum number of diamonds'
# get the max_d if 'i' is the smallest diamond chosen
max_length = [0] * (n + 1)
right = 0
for left in range(n):  # 2 pointers
    while right < n and diamonds[right] - diamonds[left] <= k:  # move right until the difference is more than k
        right += 1
    max_length[left] = right - left

# suffix maximum: the max_d using only diamonds larger than d
larger_d = [0 for d in range(n + 1)]
larger_d[-1] = max_length[-1]
for i in range(n - 2, -1, -1):  # loop from end to start
    larger_d[i] = max(max_length[i], larger_d[i + 1])

# find maximum pair using diamonds less than i and more than i
ans = 0
for i in range(n):  # ensure there is no overlap in diamonds
    ans = max(ans, max_length[i] + larger_d[i + max_length[i]])
print(ans)
