# 10/10 test cases, BFS solution

from collections import deque, defaultdict

n = int(input())

years = {"Ox": 1, "Tiger": 2, "Rabbit": 3, "Dragon": 4, "Snake": 5, "Horse": 6, "Goat": 7, "Monkey": 8, "Rooster": 9,
         "Dog": 10, "Pig": 11, "Rat": 12}
cows = {"Bessie": "Ox"}
graph = defaultdict(list)  # is a DAG

for _ in range(n):
    line = input().split()  # extract relevant information
    cow1, direction, cow1_year, cow2 = line[0], line[3], line[4], line[7]
    cows[cow1] = cow1_year  # store for later use

    cow2_year = cows[cow2]
    y1, y2 = years[cow1_year], years[cow2_year]

    # get the difference in years between the 2 cows
    if direction == "previous":
        d = ((12 - y1) + y2) % 12 * -1
        if y1 == y2:  # edge case where same year
            d = -12
    else:
        d = ((12 - y2) + y1) % 12
        if y1 == y2:
            d = 12

    graph[cow1].append((cow2, d))
    # print(cow1, d, cow2)

# BFS to find the year difference
# note that any path to the end will give the same result and there are no cycles
q = deque([("Elsie", 0)])
while q:
    cow, dist = q.popleft()
    if cow == "Bessie":
        print(abs(dist))
        break

    for adj, c in graph[cow]:
        q.append((adj, c+dist))
