# brute force, since n < 10
# probably faster with combinations but whatever

from itertools import permutations

words = int(input())
blocks = [input() for _ in range(4)]
all_perm = [list(permutations(blocks, i)) for i in range(5)]

for _ in range(words):
    word = input()
    perm = all_perm[len(word)]  # all permutation of n blocks, where n is the length of the word

    found = False
    for group in perm:  # as long as one permutation works, we can create the word
        if all(word[i] in block for i, block in enumerate(group)):
            found = True

    if found:
        print("YES")
    else:
        print("NO")
