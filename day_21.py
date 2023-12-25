"""
Description du module: Advent of Code Day 21
Auteur: Steve de Rose
Date de création: 21.12.2023
"""
from collections import defaultdict, deque

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def read_input(file_path='input_21.txt'):
    """
    Lit le fichier d'entrée et retourne la position initiale et la carte du jardin.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        garden_map = [list(line.strip()) for line in file.readlines()]

    start = next((i, j) for i, row in enumerate(garden_map)
                 for j, cell in enumerate(row) if cell == 'S')

    return start, garden_map


def get_possible_neighbors(position, garden_map):
    """
    Retourne les voisins possibles d'une position dans la carte du jardin.
    """
    heigth, width = len(garden_map), len(garden_map[0])

    return [(position[0] + dx, position[1] + dy) for dx, dy in DIRECTIONS
            if garden_map[(position[0] + dx) % heigth][(position[1] + dy) % width] != '#']


def explore_tiles(position, garden_map, max_steps):
    """
    Explore les tuiles du jardin à partir d'une position avec une limite de pas.
    """
    tiles = defaultdict(int)
    visited = set()
    queue = deque([(position, 0)])

    while queue:
        current_position, steps = queue.popleft()

        if steps == (max_steps + 1) or current_position in visited:
            continue

        tiles[steps] += 1
        visited.add(current_position)

        for next_position in get_possible_neighbors(current_position, garden_map):
            queue.append((next_position, (steps + 1)))

    return tiles


def compute_candidates(start, garden_map, max_steps):
    """
    Calcule le nombre de tuiles explorées à partir de la position initiale avec une limite de pas.
    """
    tiles = explore_tiles(start, garden_map, max_steps)
    return sum(amount for distance, amount in tiles.items() if distance % 2 == max_steps % 2)


def quadratic_formula(distances, width):
    """
    Calcule la formule quadratique à partir des distances et de la largeur.
    """
    a = (distances[2] + distances[0]) // 2 - distances[1]
    b = distances[1] - distances[0] - a
    c = distances[0]
    return a * width**2 + b * width + c


def solution_part_one(data):
    """
    Calcule la solution de la première partie du problème.
    """
    return compute_candidates(*data, 64)


def solution_part_two(data):
    """
    Calcule la solution de la deuxième partie du problème.
    """
    size = len(data[1])
    edge = size // 2

    distances = [compute_candidates(*data, edge + i * size) for i in range(3)]

    width = (26501365 - edge) // size
    return quadratic_formula(distances, width)


def main():
    """
    Fonction principale pour exécuter le programme.
    """
    data = read_input()

    print('Solution Partie 1 :', solution_part_one(data))
    print('Solution Partie 2 :', solution_part_two(data))


if __name__ == "__main__":
    main()
