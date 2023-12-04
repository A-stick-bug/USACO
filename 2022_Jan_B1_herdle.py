# simple implementation

guess = [list(input()) for _ in range(3)]
answer = [list(input()) for _ in range(3)]

right = 0
partial = 0

for i in range(3):
    for j in range(3):
        if guess[i][j] == answer[i][j]:
            right += 1
            answer[i][j] = "."  # mark as found
            guess[i][j] = "."  # mark as found


def find(i, j):
    global partial
    for ii in range(3):
        for jj in range(3):
            if answer[ii][jj] == guess[i][j]:
                partial += 1
                answer[ii][jj] = "."
                return


for i in range(3):
    for j in range(3):
        if guess[i][j] == ".":  # skip
            continue
        find(i, j)

print(right)
print(partial)
