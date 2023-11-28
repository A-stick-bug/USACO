# Pattern finding and math
# reading my solution probably won't help for this one

N, K, T = map(int, input().split())
rot = list(map(int, input().split()))
rot.append(N + rot[0])  # add an extra element to handle wrap

res = [-1] * N
for ri, r in enumerate(rot[:K]):
    for i in range(r, rot[ri + 1]):
        div = rot[ri + 1] - r
        delay = i - r  # takes some time for the rotation to get to this cell, there will be a delay
        it = T - 1 - delay  # iterations after dealing with delay
        jumps = it // div  # number of times this cow jumps forwards
        res[(i + jumps * div + div) % N] = i % N

print(*res, sep=" ")

# # brute force to find pattern
# N, K, T = map(int, input().split())
# rot = list(map(int, input().split()))
# assert rot == sorted(rot)
#
# state = list(range(N))
# original = state.copy()
#
# for iteration in range(T):
#     # print(iteration, state)
#     if state == original:
#         print(f"Match: {iteration} {state}")
#
#     new_state = state.copy()
#     for i, r in enumerate(rot):  # do rotations
#         new_state[rot[(i+1)%K]] = state[r]
#
#     state= new_state.copy()
#     rot = list(map(lambda x: (x + 1) % N, rot))  # increase by 1
#
# print(*state)
