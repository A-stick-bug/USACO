from itertools import combinations_with_replacement


def wins(d1, d2):
    """check is dice 1 wins against dice 2 by trying all roll possibilities (they have equal chance)"""
    w1 = 0
    w2 = 0
    for i in range(4):
        for j in range(4):
            if d1[i] > d2[j]:
                w1 += 1
            elif d1[i] < d2[j]:
                w2 += 1
    return w1 > w2

for _ in range(int(input())):
    inp = list(map(int, input().split()))
    a = inp[:4]
    b = inp[4:]
    if a == b:
        print('no')  # edge case breaks simulation
        continue

    d = [i for i in range(1,11)]
    all_c = list(combinations_with_replacement(d, 4))

    # check if any combination of numbers on c will work
    if any((wins(a,b) and wins(b,c) and wins(c,a)) or (wins(b,a) and wins(c,b) and wins(a,c)) for c in all_c):
        print('yes')
    else:
        print('no')
