# find the smallest n, where all substrings of length n are distinct

with open('whereami.in', 'r') as file_in:
    n = int(file_in.readline().strip())
    houses = file_in.readline().strip()

with open('whereami.out', 'w') as file_out:
    for l in range(1, n+1):
        substrings = set()
        flag = True

        for i in range(n - l + 1):
            sub = tuple(houses[i:i + l])
            if sub in substrings:
                flag = False
                break
            substrings.add(sub)

        if flag:
            file_out.write(str(l) + '\n')
            break
