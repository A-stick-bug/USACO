# tricky operations on arrays
# optimize with binary search and PSA
#
# - Basically realise that when you move something, the products become a*i -> a*(i+1) or a*(i-1) so add/minus
#   the sum in the range that was shifted
# - Also remember to minus the old value that was removed and add the new one

import sys
from itertools import accumulate
from bisect import bisect_left

input = sys.stdin.readline
N = int(input())
old = list(map(int, input().split()))
arr = sorted(old)  # optimal order to milk cows

psa = [0] + list(accumulate(arr))
query = lambda l, r: psa[r + 1] - psa[l]
total = sum(i * v for i, v in enumerate(arr, start=1))

Q = int(input())
for _ in range(Q):
    i, added = map(int, input().split())
    removed = old[i - 1]
    old_pos = bisect_left(arr, removed)
    new_pos = bisect_left(arr, added)

    if new_pos < old_pos:  # moved left
        print(total - (old_pos + 1) * removed + (new_pos + 1) * added + query(new_pos, old_pos - 1))

    elif new_pos == old_pos:  # didn't move
        print(total - (old_pos + 1) * removed + (new_pos + 1) * added)

    else:  # moved right
        print(total - (old_pos + 1) * removed + (new_pos) * added - query(old_pos + 1, new_pos - 1))
