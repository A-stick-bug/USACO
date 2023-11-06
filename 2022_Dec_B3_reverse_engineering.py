# heavily inspired by USACO official solution
# iterate column by column (vertical scanning)

get_val = lambda x: bool(int(x))  # "0" --> False, "1" --> True


def solve():
    input()  # blank line
    N, M = map(int, input().split())  # N is the length of each string, M is the number of strings
    inputs = []
    outputs = []

    for _ in range(M):
        i, o = input().split()
        inputs.append(i)
        outputs.append(o)

    uncertain = [i for i in range(M)]
    while True:
        updated = False
        for pos in range(N):
            if updated:
                break
            table = {True: [], False: []}
            out = {True: set(), False: set()}
            for seq in uncertain:
                val = get_val(inputs[seq][pos])
                table[val].append(seq)
                out[val].add(outputs[seq])

            lf = len(out[False])
            lt = len(out[True])
            if lf < 2 and lt < 2:  # both have been determined
                print("OK")
                return

            elif lf == 1:  # false has been determined for this index, reduce search space
                updated = True
                uncertain = table[True]

            elif lt == 1:  # true has been determined for this index, reduce search space
                updated = True
                uncertain = table[False]

        if not updated:  # updated nothing, can't deduce any more information due to inconsistency
            print("LIE")
            return


# for each test case
for _ in range(int(input())):
    solve()
