"""
http://usaco.org/index.php?page=viewproblem2&cpid=1252
Greedy Algorithm: put grass at furthest possible right position if the current cow needs grass

Works because (no overlap):
- the max distance that both type of cows are willing to walk is the same
- no 2 cows are at the same location

Edge Case: further position is last point and last point is already occupied
- for this edge case to happen, N > 0 must be true
- therefore, we can just put it at N-1 because if N > 0, the last cow will be able to get the grass anyway

"""

# for all test cases
for _ in range(int(input())):
    N, K = map(int, input().split())
    cows = input()
    arr = ["."] * N

    g = h = 0
    while g < N or h < N:
        if g < N and cows[g] == "G":
            i = min(g + K, N - 1)  # put in the furthest possible position
            if arr[i] != ".":  # edge case: already occupied (only happens when i == N-1)
                arr[i - 1] = "G"
            else:
                arr[i] = "G"

            g += K * 2  # all cows before this can eat the grass at i

        if h < N and cows[h] == "H":
            i = min(h + K, N - 1)
            if arr[i] != ".":
                arr[i - 1] = "H"
            else:
                arr[i] = "H"

            h += K * 2

        g += 1
        h += 1

    print(arr.count("G") + arr.count("H"))
    print(*arr, sep="")
