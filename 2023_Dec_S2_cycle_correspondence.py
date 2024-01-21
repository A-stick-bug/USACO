# given 2 lists of equal length, check how many element we can match after rotating and reversing

n, k = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))


def match(a, b):
    cnt = [0] * k  # if we rotate i times, cnt[i] will match
    loc_in_a = [-1] * (n + 1)
    for i, v in enumerate(a):  # reverse map that gets the location of a value in a
        loc_in_a[v] = i

    for i, val in enumerate(b):
        if loc_in_a[val] != -1:
            cnt[(i - loc_in_a[val]) % k] += 1  # mod since it is circular

    return max(cnt)


excluded = set(range(1, n + 1)) - set(a1) - set(a2)
print(len(excluded) + max(match(a1, a2), match(a1, a2[::-1])))
