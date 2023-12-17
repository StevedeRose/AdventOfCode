"""
Description du module: Advent of Code Day 14
Auteur: Steve de Rose
Date de création: 14.12.2023
"""
import numpy as np


FIRST, REST, ALL = 1, 2, 3


def tilt_line(line: np.char.array) -> None:
    """
    Penche une ligne.
    """
    free_spot = 0
    for index, spot in enumerate(line):
        if index == free_spot:
            free_spot += spot != '.'
        elif spot == '#':
            free_spot = index + 1
        elif spot == 'O':
            line[free_spot], line[index] = 'O', '.'
            free_spot += 1


def tilt_field(field, part):
    """
    Fait faire la partie 'part' d'un cycle à un champ.
    """
    if part in (ALL, FIRST):
        np.apply_along_axis(tilt_line, 0, field)
    if part in (ALL, REST):
        np.apply_along_axis(tilt_line, 1, field)
        np.apply_along_axis(tilt_line, 0, field[::-1])
        np.apply_along_axis(tilt_line, 1, field[:, ::-1])


def compute_total(field):
    """
    Calcule la charge totale d'un champ.
    """
    return np.sum(np.arange(1, field.shape[0] + 1)[:, None] * (field[::-1] == 'O'), axis=0).sum()


def compute_solutions(field):
    """
    Calcule les solutions du problème.
    """
    tilt_field(field, FIRST)
    solution_part_1 = compute_total(field)
    tilt_field(field, REST)
    cycle_totals = np.zeros(999999999, dtype=np.uintc)
    for i in range(999999999):
        tilt_field(field, ALL)
        cycle_totals[i] = compute_total(field)
        same_args = np.argwhere(cycle_totals[:i] == cycle_totals[i]).flatten()
        if len(same_args) > 2:
            x, y = same_args[-2:]
            if y - x > 3 and np.array_equal(cycle_totals[x:y], cycle_totals[y:i]):
                return solution_part_1, cycle_totals[(999999999 - x) % (y - x) + x - 1]
    return solution_part_1, cycle_totals[-1]


def read_input(file_path='./input_14.txt'):
    """
    Lit le fichier d'entrée et renvoie une liste de tuples.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        field = np.array([list(l) for l in f.read().splitlines() if l])
    return field


def main():
    """
    Fonction principale.
    """
    field = read_input()
    solutions = compute_solutions(field)
    print('Solution Partie 1 :', solutions[0])
    print('Solution Partie 2 :', solutions[1])


if __name__ == '__main__':
    main()
