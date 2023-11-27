# binary search for the maximum distance by checking if it is possible to have a minimum distance of x between cows

def works(d):
    """check if having a min dist of d between cows is possible, we try to place a cow in the earliest available
    position as it is always optimal"""
    prev = grass[0][0]  # first cow always goes at the start
    cow = 1
    i = 0
    while cow < N and i < M:
        if prev + d <= grass[i][1]:  # can fit cow in segment
            prev = max(prev + d, grass[i][0])  # cow is at least on the start of the next segment
            cow += 1
        else:
            i += 1
    return cow == N


N, M = map(int, input().split())  # N cows, M segments
grass = [list(map(int, input().split())) for _ in range(M)]
grass.sort()  # sort by staring point

low = 0
high = 10 ** 18
while low <= high:  # template binary search
    mid = low + (high - low) // 2
    if works(mid):
        low = mid + 1
    else:
        high = mid - 1

print(low - 1)  # low contains the first distance that doesn't work, so minus one for the last one that works
