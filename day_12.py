"""
Description du module: Advent of Code Day 11
Auteur: Steve de Rose
Date de création: 11.12.2023
"""
import re
from functools import cache


def possible_placements(row: str, group: int) -> str:
    """
    Génère toutes les positions possibles pour placer
    un groupe de longueur donnée dans une ligne.
    """
    for m in re.finditer(rf'(?=([^\.]{{{group}}}[^#]))', row):
        i = m.span(1)[0]
        if '#' in row[:i]:
            break
        yield row[i + group + 1:]


@cache
def count_arrangements(row: str, groups: tuple) -> int:
    """
    Calcule le nombre de placements possibles pour un ensemble de groupes dans une ligne.
    """
    return '#' not in row if not groups else sum(
        count_arrangements(rest_row, rest_groups)
        for rest_row in possible_placements(row, groups[0])
        for rest_groups in [groups[1:]]
    )


def total_arrangements() -> (int, int):
    """
    Fonction résolvant les deux parties du problème du jour 12 et retourne leurs résultats.
    """
    input_lines = [read_input(), read_input(5)]
    return (sum(count_arrangements(row, groups) for row, groups in lines) for lines in input_lines)


def read_input(multiplier: int = 1, file_path: str = './input_12.txt') -> list:
    """
    Lit le fichier d'entrée et renvoie une liste de tuples.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        lines = [
            (
                f'.{"?".join([row] * multiplier)}.',
                tuple(map(int, groups.split(','))) * multiplier
            )
            for row, groups in (line.strip().split() for line in f)
        ]
    return lines


def main():
    """
    Fonction principale.
    """
    solution_part_1, solution_part_2 = total_arrangements()
    print('Solution Partie 1 :', solution_part_1)
    print('Solution Partie 2 :', solution_part_2)


if __name__ == "__main__":
    main()
