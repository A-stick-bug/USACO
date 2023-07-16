n = int(input())
cows = list(map(int, input().split()))
cows.sort(reverse=True)  # costs are sorted in descending order

max_profit = 1  # placeholder values
optimal_cost = 1

for i, cost in enumerate(cows, start=1):  # 'i' is how many cows are willing to pay on this current iteration
    profit = cost * i
    if profit >= max_profit:  # >= instead of > because "If there are multiple solutions, output the solution with the smallest optimal tuition."
        max_profit = profit
        optimal_cost = cost

print(max_profit, optimal_cost)
