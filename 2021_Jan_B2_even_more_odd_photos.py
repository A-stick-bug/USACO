"""
http://www.usaco.org/index.php?page=viewproblem2&cpid=1084
You can make more even numbers from odd numbers, but you can't create more odd numbers

Because all cows must be put into groups, there is an edge case (FOR SECOND SOLUTION):
1 1 1 1 (there is 1 odd number left over)

In this case, we must minus one from the answer
Reason: even, odd, extra odd --> even (by combining the last 2 odd numbers and adding it to the even)
"""

# Simpler solution by just turning the extra odd cows into even ones
# this also takes care of the corner case

n = int(input())
nums = list(map(int, input().split()))

# count the number of even and odd numbers
even = odd = 0
for i in nums:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

# turn extra odd cows into even ones
while odd > even:
    odd -= 2
    even += 1

# can have odd+1 even cows at most, remove extra ones by putting into same groups (doesn't affect parity)
# (handles corner case)
even = min(even, odd + 1)

print(even + odd)

# n = int(input())
# nums = list(map(int, input().split()))
#
# # count the number of even and odd numbers
# even = odd = 0
# for i in nums:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# groups = 0
# parity = 0  # the parity of the current group (0 = even, 1 = odd)
#
# while odd > 0 or even > 0:
#     if parity == 0 and (even == 0 and odd == 1):  # edge case: need even, have extra odd
#         groups -= 1
#         break
#
#     # extra evens is fine because we can add it to any number without changing its parity
#     if parity == 1 and odd == 0:
#         break
#
#     # regular cases begin here
#     if parity == 0:  # need even
#         if even > 0:
#             even -= 1
#         else:
#             odd -= 2
#
#     else:  # need odd
#         odd -= 1
#
#     groups += 1
#     parity = not parity
#
# print(groups)

