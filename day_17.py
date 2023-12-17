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


def read_input(file_path='input_17.txt') -> np.ndarray:
    """
    Charge le tableau à partir d'un fichier.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        return np.array([[int(c) for c in l.strip()] for l in f.readlines()], dtype=int)


def in_range(pos, goal) -> bool:
    """
    Vérifie si la position donnée est dans les limites du tableau.
    """
    return 0 <= pos[0] <= goal[0] and 0 <= pos[1] <= goal[1]


def find_least_heat_loss(chart, mindist, maxdist, pos = (0, 0)) -> int:
    """
    Trouve le coût minimum pour atteindre le coin en bas à droite de la grille.
    """
    data = [(0, pos, -1)]
    seen = set()
    costs = defaultdict(lambda: np.inf)
    goal = tuple(np.array(chart.shape) - 1)

    while data and pos != goal:
        cost, pos, forbidden_direction = heappop(data)
        if (pos, forbidden_direction) in seen:
            continue
        seen.add((pos, forbidden_direction))
        for direction in DIRECTIONS:
            cost_increase = 0
            if forbidden_direction in (direction, (direction + 2) % 4):
                continue
            for step in range(1, maxdist + 1):
                new_pos = (pos[0] + OFFSETS[direction][0] * step,
                           pos[1] + OFFSETS[direction][1] * step)
                if in_range(new_pos, goal):
                    cost_increase += chart[new_pos]
                    if step < mindist:
                        continue
                    new_cost = cost + cost_increase
                    if costs[new_pos, direction] <= new_cost:
                        continue
                    costs[new_pos, direction] = new_cost
                    heappush(data, (new_cost, new_pos, direction))
    return cost


def main():
    """
    Fonction principale.
    """
    chart = read_input()
    print("Solution Partie 1 :", find_least_heat_loss(chart, 1, 3))
    print("Solution Partie 2 :", find_least_heat_loss(chart, 4, 10))


if __name__ == "__main__":
    main()
