"""
Description du module: Advent of Code Day 10
Auteur: Steve de Rose
Date de création: 10.12.2023
"""
import numpy as np


def read_input(file_path: str = './input_10.txt'):
    """
    Lit le fichier d'entrée et retourne les lignes non vides.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        field = np.array([list(l) for l in f.read().splitlines() if l])
    return field


def get_first_position(field: np.ndarray, sheep: tuple):
    """
    Retourne la première position à explorer dans le champ.
    """
    row, col = sheep
    if field[row + 1, col] in ['|', 'L', 'J']:
        return row + 1, col
    if field[row, col + 1] in ['-', '7', 'J']:
        return row, col + 1
    return row - 1, col


def update_path_matrix(matrix: np.ndarray, current_pos: tuple, val: int,
                       pos_1: tuple, pos_2: tuple, turn: bool = True):
    """
    Met à jour la matrice représentant le chemin suivi.
    """
    matrix[current_pos] = 2
    if 0 <= pos_1[0] < matrix.shape[0] and 0 <= pos_1[1] < matrix.shape[1] and matrix[pos_1] == 0:
        matrix[pos_1] = val
    if 0 <= pos_2[0] < matrix.shape[0] and 0 <= pos_2[1] < matrix.shape[1] and matrix[pos_2] == 0:
        matrix[pos_2] = val if turn else -val


def get_next_position(current_pos: tuple, previous_pos: tuple,
                      field: np.ndarray, path_matrix: np.ndarray):
    """
    Retourne la position suivante à explorer dans le champ.
    """
    current_val = field[current_pos]
    row, col = result = current_pos

    if current_val == '|':
        value = previous_pos[0] - row
        update_path_matrix(path_matrix, current_pos, value,
                           (row, col - 1), (row, col + 1), False)
        result = (2 * row - previous_pos[0], col)
    elif current_val == '-':
        value = col - previous_pos[1]
        update_path_matrix(path_matrix, current_pos, value,
                           (row - 1, col), (row + 1, col), False)
        result = (row, 2 * col - previous_pos[1])
    elif current_val == 'L':
        value = previous_pos[0] + previous_pos[1] - row - col
        update_path_matrix(path_matrix, current_pos, value,
                           (row + 1, col), (row, col - 1))
        result = (2 * row - previous_pos[0] - 1, 2 * col - previous_pos[1] + 1)
    elif current_val == 'J':
        value = row + previous_pos[1] - previous_pos[0] - col
        update_path_matrix(path_matrix, current_pos, value,
                           (row + 1, col), (row, col + 1))
        result = (2 * row - previous_pos[0] - 1, 2 * col - previous_pos[1] - 1)
    elif current_val == '7':
        value = row + col - previous_pos[0] - previous_pos[1]
        update_path_matrix(path_matrix, current_pos, value,
                           (row - 1, col), (row, col + 1))
        result = (2 * row - previous_pos[0] + 1, 2 * col - previous_pos[1] - 1)
    elif current_val == 'F':
        value = previous_pos[0] + col - row - previous_pos[1]
        update_path_matrix(path_matrix, current_pos, value,
                           (row - 1, col), (row, col - 1))
        result = (2 * row - previous_pos[0] + 1, 2 * col - previous_pos[1] + 1)

    return current_pos, result


def complete_path_matrix(path_matrix: np.ndarray, val: int = 0) -> int:
    """
    Complète la matrice représentant le chemin suivi.
    """
    zero_positions = [tuple(pos) for pos in np.argwhere(path_matrix == 0)]
    while zero_positions:
        for pos in zero_positions:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_pos = (pos[0] + dx, pos[1] + dy)
                if (0 <= new_pos[0] < path_matrix.shape[0] and
                    0 <= new_pos[1] < path_matrix.shape[1] and
                        abs(path_matrix[new_pos]) == 1):
                    path_matrix[pos] = path_matrix[new_pos]
                    if val == 0 and (pos[0] == 0 or pos[0] == path_matrix.shape[0] - 1 or
                                    pos[1] == 0 or pos[1] == path_matrix.shape[1] - 1):
                        val = -path_matrix[pos]
        zero_positions = [tuple(pos) for pos in np.argwhere(path_matrix == 0)]
    return val


def main():
    """
    Fonction principale.
    """
    field = read_input()
    previous_pos = tuple(np.argwhere(field == 'S')[0])
    path_matrix = np.zeros_like(field, dtype=np.byte)
    path_matrix[previous_pos] = 2
    current_pos = get_first_position(field, previous_pos)
    steps = 0

    while current_pos != previous_pos:
        previous_pos, current_pos = get_next_position(current_pos, previous_pos, field, path_matrix)
        steps += 1

    enclosed = complete_path_matrix(path_matrix)

    print('Solution Partie 1 :', steps // 2)
    print('Solution Partie 2 :', np.sum(path_matrix == enclosed))


if __name__ == "__main__":
    main()
