import sys

# uncomment this when submitting, comment when running in regular coding environment (IDE)
sys.stdin = open('div7.in', 'r')
sys.stdout = open('div7.out', 'w')

n = int(input())

arr = [int(input())]
for i in range(1, n):
    num = int(input())
    arr.append((num + arr[-1]) % 7)

res = 0
for i in range(7):
    if i not in arr:
        continue

    start = arr.index(i)
    end = n - arr[::-1].index(i) - 1  # find right index
    res = max(res, end - start)

print(res)
