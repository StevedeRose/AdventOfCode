"""
Description du module: Advent of Code Day 13
Auteur: Steve de Rose
Date de création: 13.12.2023
"""
import numpy as np


def read_input(file_path='./input_13.txt'):
    """
    Lit le fichier d'entrée et retourne les motifs.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        patterns = [block.strip() for block in f.read().split('\n\n')]
    return patterns


def find_mirror(record, part):
    """
    Cherche un mirroir dans un tableau et retourne sa position.
    """
    length = len(record)
    for i in range(1, length):
        # Vérification de la symétrie
        if np.sum(record[max(0, 2*i-length):i]
                  != record[i:min(2*i, length)][::-1]) == part - 1:
            return i
    return 0


def compute_solution(patterns, part=1):
    """
    Résoud la partie 1 ou 2 du problème.
    """
    total_answer = 0
    for pattern in patterns:
        pattern_array = np.array([list(row) for row in pattern.split()])
        mirror = find_mirror(pattern_array, part) * 100
        if mirror == 0:
            mirror = find_mirror(pattern_array.T, part)
        total_answer += mirror
    print(f'Solution Partie {part}: {total_answer}')


def main():
    """
    Fonction principale.
    """
    patterns = read_input()

    if patterns:
        compute_solution(patterns)
        compute_solution(patterns, 2)


if __name__ == "__main__":
    main()
