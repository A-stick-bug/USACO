# TLE on test case 8, optimized as much as possible

import sys
from collections import defaultdict, deque

# uncomment this when submitting, comment when running in regular coding environment (IDE)
sys.stdin = open('where.in', 'r')
sys.stdout = open('where.out', 'w')


def is_plc(sub):  # given a matrix, check if it is a PLC
    def flood_fill(color, r, c):
        stack = deque()
        stack.append((r, c))
        while stack:
            row, col = stack.popleft()

            if sub[row][col] != color:
                continue
            sub[row][col] = "."  # marked as visited

            for dr, dc in dir:
                new_r, new_c = row + dr, col + dc
                if ROWS > new_r >= 0 and COLS > new_c >= 0 and sub[new_r][new_c] == color:
                    stack.append((new_r, new_c))

    ROWS, COLS = len(sub), len(sub[0])
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    colors = defaultdict(int)
    for i in range(ROWS):
        for j in range(COLS):
            color = sub[i][j]
            if sub[i][j] != ".":
                colors[color] += 1
                flood_fill(color, i, j)

    a, b = colors.values()
    return (a == 1 and b > 1) or (b == 1 and a > 1)


def get_sub(matrix, row_start, row_end, col_start, col_end):
    submatrix = []
    for row in range(row_start, row_end + 1):
        submatrix.append(matrix[row][col_start:col_end + 1])
    return submatrix


def count_letters(sub):  # count how many of each letter there are
    count = defaultdict(int)
    for i in range(len(sub)):
        for j in range(len(sub[0])):
            count[sub[i][j]] += 1
    return count


# get every subarray and check if it works
n = int(input())
grid = [list(input()) for _ in range(n)]
plcs = []

for i1 in range(n):
    for j1 in range(n):
        for i2 in range(n - 1, i1 - 1, -1):  # reverse order to get the bigger PLCs first
            for j2 in range(n - 1, j1 - 1, -1):
                sub = get_sub(grid, i1, i2, j1, j2)
                letters = count_letters(sub)
                if len(letters) != 2:
                    continue

                # check if it's in another PLC
                in_plc = False
                for pl1, pl2, pl3, pl4 in plcs:
                    if pl1 <= i1 <= i2 <= pl2 and pl3 <= j1 <= j2 <= pl4:
                        in_plc = True
                        break
                if in_plc:
                    continue

                if is_plc(sub):
                    plcs.append((i1, i2, j1, j2))

print(len(plcs))
