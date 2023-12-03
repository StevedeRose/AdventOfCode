import numpy as np

with open('./input_3.txt') as f:
    lines = f.read().splitlines()

tab = np.array([list(line) for line in lines])
row_num, col_num = tab.shape


def is_valid(row, col):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, -1), (-1, 1), (1, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < row_num and 0 <= c < col_num and tab[r, c] != '.' and not tab[r, c].isdigit():
            return True
    return False

total = 0

for row in range(row_num):
    col = 0
    while col < col_num:
        number = ""
        is_number = False

        while col < col_num and tab[row, col].isdigit():
            number += tab[row, col]
            is_number = is_number or is_valid(row, col)
            col += 1

        if is_number:
            total += int(number)

        col += 1

print(total)
