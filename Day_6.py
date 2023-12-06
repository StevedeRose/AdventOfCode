import re
import math


def nb_ways(time, dist):
    discriminant = math.sqrt(time**2 - 4 * dist)
    min_t = math.ceil((time - discriminant) / 2 + 1e-4)
    max_t = math.floor((time + discriminant) / 2 - 1e-4)

    return max_t - min_t + 1


def main():
    with open('./input_6.txt') as f:
        lines = [line for line in f.read().splitlines() if line]

    times = [int(seed) for seed in re.findall(r'\d+', lines[0])]
    dists = [int(seed) for seed in re.findall(r'\d+', lines[1])]

    answer_part_1 = 1
    for time, dist in zip(times, dists):
        answer_part_1 *= nb_ways(time, dist)

    print('Answer Part 1:', answer_part_1)

    time = int(lines[0].replace(' ', '').split(':')[1])
    dist = int(lines[1].replace(' ', '').split(':')[1])

    print('Answer Part 2:', nb_ways(time, dist))


if __name__ == "__main__":
    main()
