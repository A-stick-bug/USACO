# 2 pointers solution

import sys

# uncomment this when submitting, comment when running in regular coding environment (IDE)
sys.stdin = open('rental.in', 'r')
sys.stdout = open('rental.out', 'w')


n_cows, n_stores, n_rent = map(int, input().split())

milks = [int(input()) for _ in range(n_cows)]
stores = [list(map(int, input().split())) for _ in range(n_stores)]
rent = [int(input()) for _ in range(n_rent)]

milks.sort()  # production of each cow low to high
stores.sort(reverse=True, key=lambda s: s[1])  # stores with highest profit first
rent.sort(reverse=True)  # rent with highest gain first

rent_cow, right_cow = 0, n_cows - 1
i_stores = 0  # store still willing to buy
res = 0

while right_cow >= rent_cow:  # when left > right, it means we already used all the cows
    right_milk = milks[right_cow]
    right_total = 0  # money gained from selling the milk for right_cow
    to_buy = i_stores

    while to_buy < n_stores:
        amt = stores[to_buy][0]
        if amt > right_milk:
            amt -= right_milk
            right_total += right_milk*stores[to_buy][1]
            break
        else:
            right_milk -= amt
            right_total += amt*stores[to_buy][1]
            to_buy += 1

    if rent_cow < len(rent) and rent[rent_cow] > right_total:  # check is renting left_cow gives more money
        res += rent[rent_cow]
        rent_cow += 1

    else:  # selling gives more money so we update the values in stores (and the stores that is still willing to buy)
        i_stores = to_buy
        if i_stores < n_stores:
            stores[i_stores][0] = amt
        res += right_total
        right_cow -= 1

print(res)


# similar approach (not my code, credit goes to USACO Guide), --this doesn't use 2 pointers--
#
# import sys
#
# # uncomment this when submitting, comment when running in regular coding environment (IDE)
# sys.stdin = open('rental.in', 'r')
# sys.stdout = open('rental.out', 'w')
#
#
# n_cows, n_stores, n_rent = map(int, input().split())
#
# milks = [int(input()) for _ in range(n_cows)]
# stores = [list(map(int, input().split())) for _ in range(n_stores)]
# rent = [int(input()) for _ in range(n_rent)]
#
# milks.sort(reverse=True)  # production of each cow low to high
# stores.sort(reverse=True, key=lambda s: s[1])  # stores with highest profit first
# rent.sort(reverse=True)  # rent with highest profit first
#
# i_store = 0  # the index of the shop which we've bought up to
# i_rent = 0  # the index of the farmer we've rented up to
# i_cow = 0
#
# total = 0
# while i_cow < n_cows:
#     milk = milks[i_cow]
#     sold_money = 0  # how much we can make from selling the milk
#     curr_shop = i_store
#     last = 0
#
#     # calculate how much money this cow can make if we sell its milk
#     while curr_shop < n_stores:
#         sold = min(milk, stores[curr_shop][0])
#         sold_money += stores[curr_shop][1] * sold
#         milk -= sold
#
#         if milk == 0:
#             last = sold
#             break
#         else:
#             curr_shop += 1
#
#     # decide rent or sell milk
#     if i_rent >= n_rent or sold_money > rent[i_rent]:
#         total += sold_money
#         i_store = curr_shop
#         if i_store < n_stores:
#             stores[i_store][0] -= last
#         i_cow += 1
#     else:
#         total += rent[i_rent]
#         n_cows -= 1
#         i_rent += 1
#
# print(total)
