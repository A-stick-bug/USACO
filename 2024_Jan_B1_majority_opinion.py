# observation 1: for any type of hay, H, if there is are 2 hays of type H right next to each other, we
# can just expand by 1 to either side and eventually cover everything
#
# observation 2: the same thing will work if we have anything in the form of (H X H), the sample case was nice enough
# to give this observation to us

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    adj = set()  # adjacent hays of same type that we found

    for i in range(1, n):  # observation 1: adjacent
        if arr[i] == arr[i - 1]:
            adj.add(arr[i])
    for i in range(2, n):  # observation 2: adjacent with 1 thing in between
        if arr[i] == arr[i - 2]:
            adj.add(arr[i])

    if not adj:
        print(-1)
    else:
        print(" ".join(map(str, sorted(adj))))


for _ in range(int(input())):
    solve()
