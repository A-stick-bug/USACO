n = int(input())
flowers = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(i, n):
        sub = flowers[i: j + 1]
        avg = sum(sub) / (j - i + 1)
        res += avg in sub

print(res)
