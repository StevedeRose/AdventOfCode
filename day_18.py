"""
Description du module: Advent of Code Day 18
Auteur: Steve de Rose
Date de création: 18.12.2023
"""
from shapely.geometry import Polygon
import numpy as np

OFFSETS = {
    'U': np.array((-1, 0)), '0': np.array((0, 1)),
    'L': np.array((0, -1)), '1': np.array((1, 0)),
    'D': np.array((1, 0)), '2': np.array((0, -1)),
    'R': np.array((0, 1)), '3': np.array((-1, 0))
}


def read_input(file_path='./input_18.txt'):
    """
    Lit le fichier d'entrée.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        return np.array([line.split() for line in f.read().splitlines() if line])


def get_next_corner(current_corner, direction, distance):
    """
    Cherche le prochain coin en fonction de la direction et la distance.
    """
    return current_corner + OFFSETS[direction] * distance


def compute_solution(lines, part):
    """
    Calcule la soution d'une partie du problème.
    """
    corners = np.zeros((lines.shape[0] + 1, 2), dtype=int)
    perimeter = 0

    if part == 1:
        directions, distances = lines[:, 0], lines[:, 1].astype(int)
    else:
        directions = [line[-2] for line in lines[:, 2]]
        distances = [int(line[2:7], 16) for line in lines[:, 2]]

    for i, (direction, distance) in enumerate(zip(directions, distances)):
        perimeter += distance
        corners[i + 1] = get_next_corner(corners[i], direction, distance)

    polygon = Polygon(corners)
    area = polygon.area

    return int(area + perimeter // 2 + 1)


def main():
    """
    Fonction principale.
    """
    lines = read_input()
    print("Solution Partie 1 :", compute_solution(lines, 1))
    print("Solution Partie 2 :", compute_solution(lines, 2))


if __name__ == '__main__':
    main()
