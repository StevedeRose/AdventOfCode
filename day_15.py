"""
Description du module: Advent of Code Day 15
Auteur: Steve de Rose
Date de création: 15.12.2023
"""
from functools import reduce, cache
from collections import defaultdict

TABLE = {i: (i * 17) % 256 for i in range(256)}
BOXES = defaultdict(dict)


@cache
def apply_hash(word):
    """
    Applique l'algorithme HASH à un mot.
    """
    return reduce(lambda result, c: TABLE[(result + ord(c)) % 256], word, 0)


def read_input(file_path='./input_15.txt'):
    """
    Lit le fichier d'entrée et renvoie une liste de mots.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        return f.read().strip().split(',')


def put_words_in_boxes(words):
    """
    Place les labels et les distances focales dans les boîtes.
    """
    for word in words:
        if word.endswith('-'):
            label = word[:-1]
            BOXES[apply_hash(label)].pop(label, None)
        else:
            label, focal_length = word.split('=')
            BOXES[apply_hash(label)][label] = int(focal_length)


def compute_solution_1(words):
    """
    Calcule la solution de la partie 1.
    """
    return sum(apply_hash(word) for word in words)


def compute_solution_2(words):
    """
    Calcule la solution de la partie 2.
    """
    put_words_in_boxes(words)
    return sum((i + 1) * j * focal_length for i, box in BOXES.items()
               for j, focal_length in enumerate(box.values(), start=1))


def main():
    """
    Fonction principale.
    """
    words = read_input()
    solution_part_1 = compute_solution_1(words)
    print('Solution Partie 1 :', solution_part_1)
    solution_part_2 = compute_solution_2(words)
    print('Solution Partie 2 :', solution_part_2)


if __name__ == '__main__':
    main()
