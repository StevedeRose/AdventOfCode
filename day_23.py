"""
Description du module: Advent of Code Day 23
Auteur: Steve de Rose
Date de création: 23.12.2023
"""
from collections import defaultdict


OFFSETS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}


def read_hiking_map(file_path='input_23.txt'):
    """
    Lit la carte des sentiers de randonnée depuis un fichier texte.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        return file.read().splitlines()


def valid_neighbors(position, hiking_map):
    """
    Renvoie les voisins valides d'une position sur la carte.
    """
    i, j = position
    dim = len(hiking_map)
    neighbors = set()

    for di, dj in OFFSETS.values():
        ni, nj = i + di, j + dj
        if 0 <= ni < dim and 0 <= nj < dim and hiking_map[ni][nj] != '#':
            neighbors.add((ni, nj))

    return neighbors


def get_slope_neighbors(position, hiking_map):
    """
    Renvoie les voisins valides d'une position sur la carte en tenant compte des pentes.
    """
    i, j = position
    direction = hiking_map[i][j]

    if direction in OFFSETS:
        di, dj = OFFSETS[direction]
        return {(i + di, j + dj)}
    return valid_neighbors(position, hiking_map)


def dfs(hiking_map):
    """
    Effectue une recherche en profondeur (DFS) pour trouver 
    le chemin le plus long entre deux points sur la carte.
    """
    start = (0, 1)
    end = (len(hiking_map) - 1, len(hiking_map) - 2)
    stack = [(start, 0, {start})]
    max_distance = 0

    while stack:
        current, distance, visited = stack.pop()

        if current == end:
            max_distance = distance if distance > max_distance else max_distance

        for neighbor in get_slope_neighbors(current, hiking_map):
            if neighbor not in visited:
                stack.append((neighbor, distance + 1, visited | {neighbor}))

    return max_distance


def build_graph(start, end, hiking_map):
    """
    Construit un graphe des pentes entre les bifurcations.
    """
    dim = len(hiking_map)
    junctions = {start}
    junctions.update((i, j) for i in range(dim) for j in range(
        dim) if len(valid_neighbors((i, j), hiking_map)) > 2)
    junctions.add(end)
    graph = defaultdict(list)

    for junction in junctions:
        for current in valid_neighbors(junction, hiking_map):
            previous, distance = junction, 1

            while current not in junctions:
                previous, current = current, next(neighbor for neighbor in valid_neighbors(
                    current, hiking_map) if neighbor != previous)
                distance += 1

            graph[junction].append((current, distance))

    return graph


def dfs_longest_hike(hiking_map):
    """
    Trouve la randonnée la plus longue en utilisant un graphe précalculé.
    """
    start = (0, 1)
    end = (len(hiking_map) - 1, len(hiking_map) - 2)
    stack = [(start, 0, {start})]
    longest_hike = 0
    graph = build_graph(start, end, hiking_map)

    while stack:
        current, distance, visited = stack.pop()

        if current == end:
            longest_hike = distance if distance > longest_hike else longest_hike

        for neighbor, plus in graph[current]:
            if neighbor not in visited:
                stack.append((neighbor, distance + plus, visited | {neighbor}))

    return longest_hike


def main():
    """
    Fonction principale pour exécuter le programme.
    """
    hiking_map = read_hiking_map()

    print('Solution Partie 1 :', dfs(hiking_map))
    print('Solution Partie 2 :', dfs_longest_hike(hiking_map))


if __name__ == '__main__':
    main()
