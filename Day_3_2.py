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
        if 0 <= r < row_num and 0 <= c < col_num and tab[r, c] == '*':
            return (r, c)
    return None


stars = {(row, col): [] for row in range(row_num) for col in range(col_num) if tab[row, col] == '*'}

for row in range(row_num):
    col = 0
    while col < col_num:
        number = ""
        is_number = False
        neighbors = set()

        while col < col_num and tab[row, col].isdigit():
            number += tab[row, col]
            star = is_valid(row, col)
            if star:
                neighbors.add(star)
                is_number = True
            col += 1

        if is_number:
            for star in neighbors:
                stars[star].append(int(number))

        col += 1

total = sum(vec[0] * vec[1] for vec in stars.values() if len(vec) == 2)

print(total)
