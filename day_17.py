"""
Description du module: Advent of Code Day 17
Auteur: Steve de Rose
Date de création: 17.12.2023
"""
from heapq import heappop, heappush
from collections import defaultdict
import numpy as np

OFFSETS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIRECTIONS = range(4)


def read_input(file_path: str = 'input_17.txt') -> np.ndarray:
    """
    Charge le tableau à partir d'un fichier.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        return np.array([[int(c) for c in l.strip()] for l in f.readlines()], dtype=int)


def in_range(pos: (int, int), goal: (int, int)) -> bool:
    """
    Vérifie si la position donnée est dans les limites du tableau.
    """
    return 0 <= pos[0] <= goal[0] and 0 <= pos[1] <= goal[1]


def get_new_position(pos: (int, int), offset: (int, int), distance: int) -> (int, int):
    """
    Calcule la nouvelle position en fonction de la position actuelle, du décalage et de la distance.
    """
    return pos[0] + offset[0] * distance, pos[1] + offset[1] * distance


def find_least_heat_loss(chart: np.ndarray, bounds: (int, int)) -> int:
    """
    Trouve le coût minimum pour atteindre le coin en bas à droite de la grille.
    """
    data = [(0, (0, 0), -1)]
    seen = set()
    costs = defaultdict(lambda: np.inf)
    goal = (chart.shape[0] - 1, chart.shape[1] - 1)

    while data:
        cost, pos, stop = heappop(data)
        if pos == goal:
            break
        if (pos, stop) in seen:
            continue
        seen.add((pos, stop))
        for way in DIRECTIONS:
            if stop in {way, (way + 2) % 4}:
                continue
            offset = OFFSETS[way]
            cost_increase = 0
            for distance in range(1, bounds[1]):
                new_pos = get_new_position(pos, offset, distance)
                if in_range(new_pos, goal):
                    cost_increase += chart[new_pos]
                    if distance > bounds[0] and costs[new_pos, way] > cost + cost_increase:
                        costs[new_pos, way] = cost + cost_increase
                        heappush(data, (costs[new_pos, way], new_pos, way))
    return cost


def main() -> None:
    """
    Fonction principale.
    """
    chart = read_input()
    bounds_1, bounds_2 = (0, 4), (3, 11)
    print(f'Solution Partie 1 : {find_least_heat_loss(chart, bounds_1)}')
    print(f'Solution Partie 2 : {find_least_heat_loss(chart, bounds_2)}')


if __name__ == "__main__":
    main()
