import re
import numpy as np

def update_map(matrix, index, lines, start_index, max_index):
    while start_index < max_index and lines[start_index][-1:] != ':':
        dst, src, rng = map(int, lines[start_index].split())

        mask = (src <= matrix[index]) & (matrix[index] < src + rng)
        matrix[index + 1:, mask] = dst + matrix[index, mask] - src

        start_index += 1
    return start_index + 1

def main():
    with open('./input_5.txt') as f:
        lines = [line for line in f.read().splitlines() if line]

    initial_seed = [int(seed) for seed in re.findall(r'\d+', lines[0])]
    matrix = np.tile(initial_seed, (8, 1)).astype(np.uint64)

    start_index = 2
    max_index = len(lines)

    for index in range(7):
        start_index = update_map(matrix, index, lines, start_index, max_index)

    print(min(matrix[-1]))

if __name__ == "__main__":
    main()