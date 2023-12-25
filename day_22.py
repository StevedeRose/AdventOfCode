"""
Description du module: Advent of Code Day 22
Auteur: Steve de Rose
Date de création: 22.12.2023
"""
from collections import defaultdict


def read_bricks_from_files(file_path='input_22.txt'):
    """
    Lit le fichier d'entrée et renvoie les informations sur les briques.
    """
    bricks = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            left, right = line.strip().split('~')
            start = tuple(map(int, left.split(',')))
            end = tuple(map(int, right.split(',')))
            bricks.append((start, end))
    return bricks


def generate_blocks(brick):
    """
    Génère les blocs (cubes) occupés par une brique.
    """
    (start_x, start_y, start_z), (end_x, end_y, end_z) = brick
    ranges = [(start_x, end_x + 1), (start_y, end_y + 1), (start_z, end_z + 1)]
    return [(x, y, z) for x in range(*ranges[0]) for y
            in range(*ranges[1]) for z in range(*ranges[2])]


def update_bricks_positions(bricks):
    """
    Met à jour les positions des briques en fonction de leur stabilité.
    """
    bricks.sort(key=lambda brick: brick[0][2])
    occupied_blocks = set()
    updated_bricks = []

    for (start_x, start_y, start_z), (end_x, end_y, end_z) in bricks:
        while is_valid_position(((start_x, start_y, start_z - 1),
                                 (end_x, end_y, end_z - 1)), occupied_blocks) and start_z - 1 >= 1:
            start_z -= 1
            end_z -= 1

        updated_brick = ((start_x, start_y, start_z), (end_x, end_y, end_z))
        updated_bricks.append(updated_brick)
        occupied_blocks.update(generate_blocks(updated_brick))

    return sorted(updated_bricks, key=lambda brick: brick[0][2])


def is_valid_position(brick, occupied_blocks):
    """
    Vérifie si la position d'une brique est valide par rapport aux blocs occupés.
    """
    return all((x, y, z) not in occupied_blocks for (x, y, z) in generate_blocks(brick))


def supports(brick1, brick2):
    """
    Définit si la brique brick1 supporte la brique brick2.
    """
    return any((x, y, z + 1) in generate_blocks(brick2) for x, y, z in generate_blocks(brick1))


def get_parents_children(bricks):
    """
    Identifie les parents et les enfants des briques dans l'ordre de chute.
    """
    parents = defaultdict(list)
    children = defaultdict(list)

    for i, brick1 in enumerate(bricks):
        for j, brick2 in enumerate(bricks):
            if brick2[0][2] > brick1[1][2] + 1:
                break

            if j > i and supports(brick1, brick2):
                parents[j].append(i)
                children[i].append(j)

    return parents, children, len(bricks)


def solution_part_one(parents, length):
    """
    Compte le nombre de briques pouvant être désintégrées en toute sécurité.
    """
    disintegration_graph = defaultdict(list)
    for i in range(length):
        for j in range(length):
            if parents[j] == [i]:
                disintegration_graph[i].append(j)
    return sum(not disintegration_graph[i] for i in range(length))


def solution_part_two(bricks, children, length):
    """
    Calcule la somme des briques qui tomberaient en désintégrant chaque brique.
    """
    total = 0
    heights = [brick[0][2] for brick in bricks]

    for index in range(length):
        viewed = {i for i in range(length) if heights[i] == 1}
        stack = [i for i in range(length) if heights[i] == 1 and i != index]

        while stack:
            x = stack.pop()
            if x != index:
                stack.extend(v for v in children[x] if v not in viewed)
                viewed.update(children[x])

        total += length - len(viewed)

    return total


def main():
    """
    Fonction principale pour résoudre le problème.
    """
    bricks = update_bricks_positions(read_bricks_from_files())
    parents, children, length = get_parents_children(bricks)

    print('Solution Partie 1 :', solution_part_one(parents, length))
    print('Solution Partie 2 :', solution_part_two(bricks, children, length))


if __name__ == '__main__':
    main()
