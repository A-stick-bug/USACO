# brute force with optimization

N, M = map(int, input().split())
cows = list(map(int, input().split()))
candies = list(map(int, input().split()))

for candy in candies:
    lowest = 0
    for i, cow in enumerate(cows):
        if candy <= 0:  # this optimization reduces time complexity
            break
        if cow > lowest:
            eat = min(candy, cow - lowest)  # leftovers or as much as we can
            lowest += eat
            cows[i] += eat
            candy -= eat

for i in cows:
    print(i)
