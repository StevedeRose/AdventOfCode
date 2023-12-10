"""
Description du module: Advent of Code Day 5
Auteur: Steve de Rose
Date de création: 05.12.2023
"""
import re
import numpy as np


def update_map(matrix, index, lines, start_index, max_index):
    """
    Met à jour la matrice en fonction des règles définies dans la liste de lignes.
    """
    while start_index < max_index and lines[start_index][-1:] != ':':
        dst, src, rng = map(int, lines[start_index].split())

        mask = (src <= matrix[index]) & (matrix[index] < src + rng)
        matrix[index + 1:, mask] = dst + matrix[index, mask] - src

        start_index += 1
    return start_index + 1


def find_intersection_and_difference(line, src, rng, dst):
    """
    Trouve les intersections et les différences entre la ligne actuelle et une règle donnée.
    """
    intersections = []
    difference = []

    for i in range(0, len(line), 2):
        a, b = line[i], line[i + 1] + line[i] - 1
        inter = [max(a, src), min(b, src + rng - 1)]

        if inter[0] <= inter[1]:
            intersections.extend(
                [dst + inter[0] - src, inter[1] - inter[0] + 1])

            if a < inter[0]:
                difference.extend([a, inter[0] - a + 1])

            if b > inter[1]:
                a = inter[1] + 1
        else:
            difference.extend([a, b - a + 1])

    return intersections, difference


def process_line(line, lines, start_index):
    """
    Traite une ligne en appliquant les règles définies dans la liste de lignes.
    """
    nline = []
    idx = start_index

    for idx, ligne in enumerate(lines[start_index:], start=start_index):
        if ligne[-1] == ':':
            break
        dst, src, rng = map(int, ligne.split())
        inter, diff = find_intersection_and_difference(line, src, rng, dst)
        line = diff
        nline.extend(inter)

    return idx + 1, line + nline


def read_input(file_path='./input_5.txt'):
    """
    Lit le fichier d'entrée et retourne les lignes non vides.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        lines = [line for line in f.read().splitlines() if line]
    return lines


def main():
    """
    Fonction principale.
    """
    lines = read_input()

    result_line = [int(seed) for seed in re.findall(r'\d+', lines[0])]
    matrix = np.tile(result_line, (8, 1)).astype(np.uint64)

    index_1 = index_2 = 2
    max_index = len(lines)

    for index in range(7):
        index_1 = update_map(matrix, index, lines, index_1, max_index)
        index_2, result_line = process_line(result_line, lines, index_2)

    print('Solution Partie 1 :', min(matrix[-1]))
    print('Solution Partie 2 :', min(result_line[::2]))


if __name__ == "__main__":
    main()
