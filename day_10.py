"""
Description du module: Advent of Code Day 1
Auteur: Steve de Rose
Date de création: 03.12.2023
"""
import numpy as np


def read_input(file_path='./input_10.txt'):
    """
    Lit le fichier d'entrée et retourne les lignes non vides.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        field = np.array([list(line)
                         for line in f.read().splitlines() if line])
    return field


def get_sheep(field):
    """
    Retourne la position du mouton dans le champ.
    """
    return tuple(np.argwhere(field == 'S')[0])


def get_first(field, sheep):
    """
    Retourne la première position à explorer dans le champ.
    """
    if field[sheep[0] + 1, sheep[1]] in ['|', 'L', 'J']:
        return sheep[0] + 1, sheep[1]
    if field[sheep[0], sheep[1] + 1] in ['-', '7', 'J']:
        return sheep[0], sheep[1] + 1
    return (sheep[0] - 1, sheep[1])


def update_path_matrix(matrix, curr, val, pos_1, pos_2, turn=True):
    """
    Met à jour la matrice représentant le chemin suivi.
    """
    matrix[curr] = 2
    if 0 < pos_1[0] < matrix.shape[0] and 0 < pos_1[1] < matrix.shape[1] and matrix[pos_1] == 0:
        matrix[pos_1] = val
    if 0 < pos_2[0] < matrix.shape[0] and 0 < pos_2[1] < matrix.shape[1] and matrix[pos_2] == 0:
        matrix[pos_2] = val if turn else -val


def get_next_position(curr, prev, field, path_matrix):
    """
    Retourne la position suivante à explorer dans le champ.
    """
    curr_val = field[curr]
    result = curr

    if curr_val == '|':
        val = prev[0] - curr[0]
        update_path_matrix(path_matrix, curr, val,
                           (curr[0], curr[1] - 1), (curr[0], curr[1] + 1), False)
        result = (2 * curr[0] - prev[0], curr[1])
    elif curr_val == '-':
        val = curr[1] - prev[1]
        update_path_matrix(path_matrix, curr, val,
                           (curr[0] - 1, curr[1]), (curr[0] + 1, curr[1]), False)
        result = (curr[0], 2 * curr[1] - prev[1])
    elif curr_val == 'L':
        val = prev[0] + prev[1] - curr[0] - curr[1]
        update_path_matrix(path_matrix, curr, val,
                           (curr[0] + 1, curr[1]), (curr[0], curr[1] - 1))
        result = (2 * curr[0] - prev[0] - 1, 2 * curr[1] - prev[1] + 1)
    elif curr_val == 'J':
        val = curr[0] + prev[1] - prev[0] - curr[1]
        update_path_matrix(path_matrix, curr, val,
                           (curr[0] + 1, curr[1]), (curr[0], curr[1] + 1))
        result = (2 * curr[0] - prev[0] - 1, 2 * curr[1] - prev[1] - 1)
    elif curr_val == '7':
        val = curr[0] + curr[1] - prev[0] - prev[1]
        update_path_matrix(path_matrix, curr, val,
                           (curr[0] - 1, curr[1]), (curr[0], curr[1] + 1))
        result = (2 * curr[0] - prev[0] + 1, 2 * curr[1] - prev[1] - 1)
    elif curr_val == 'F':
        val = prev[0] + curr[1] - curr[0] - prev[1]
        update_path_matrix(path_matrix, curr, val,
                           (curr[0] - 1, curr[1]), (curr[0], curr[1] - 1))
        result = (2 * curr[0] - prev[0] + 1, 2 * curr[1] - prev[1] + 1)
    return curr, result


def complete_path_matrix(matrix, val):
    """
    Complète la matrice représentant le chemin suivi.
    """
    zero_positions = [tuple(pos) for pos in np.argwhere(matrix == 0)]

    if not zero_positions:
        return val

    for pos in zero_positions:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            if (0 <= new_pos[0] < matrix.shape[0] and
                0 <= new_pos[1] < matrix.shape[1] and
                    abs(matrix[new_pos]) == 1):
                matrix[pos] = matrix[new_pos]
                if val == 0 and (pos[0] == 0 or pos[0] == matrix.shape[0] - 1 or
                                 pos[1] == 0 or pos[1] == matrix.shape[1] - 1):
                    val = -matrix[pos]

    return complete_path_matrix(matrix, val)


def main():
    """
    Fonction principale.
    """
    field = read_input()
    path_matrix = np.zeros_like(field, dtype=np.byte)

    prev = get_sheep(field)
    path_matrix[prev] = 2
    curr = get_first(field, prev)

    steps = 0
    while curr != prev:
        prev, curr = get_next_position(curr, prev, field, path_matrix)
        steps += 1

    print('Solution Partie 1 :', steps // 2)

    ext_val = complete_path_matrix(path_matrix, 0)

    print('Solution Partie 2 :', np.sum(path_matrix == ext_val))


if __name__ == "__main__":
    main()
