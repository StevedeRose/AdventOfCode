import re

def find_intersection_and_difference(line, src, rng, dst):
    intersections = []
    difference = []

    for i in range(0, len(line), 2):
        a, b = line[i], line[i + 1] + line[i] - 1
        intersection = [max(a, src), min(b, src + rng - 1)]

        if intersection[0] <= intersection[1]:
            intersections.extend([dst + intersection[0] - src, intersection[1] - intersection[0] + 1])

            if a < intersection[0]:
                difference.extend([a, intersection[0] - a + 1])

            if b > intersection[1]:
                a = intersection[1] + 1
        else:
            difference.extend([a, b - a + 1])

    return intersections, difference

def process_line(line, lines, start_index):
    nline = []

    for idx, ligne in enumerate(lines[start_index:], start=start_index):
        if ligne[-1] == ':':
            break
        dst, src, rng = map(int, ligne.split())
        inter, diff = find_intersection_and_difference(line, src, rng, dst)
        line = diff
        nline.extend(inter)

    return idx + 1, line + nline

def main():
    with open('./input_5.txt') as f:
        lines = [line for line in f.read().splitlines() if line]

    start_index = 2
    result_line = [int(seed) for seed in re.findall(r'\d+', lines[0])]

    for _ in range(7):
        start_index, result_line = process_line(result_line, lines, start_index)

    print(min(result_line[::2]))

if __name__ == "__main__":
    main()