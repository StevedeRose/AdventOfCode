"""
Description du module: Advent of Code Day 1
Auteur: Steve de Rose
Date de création: 03.12.2023
"""
import numpy as np


def get_digit(indices, part, forward=True):
    """Retourne le chiffre correspondant à la partie spécifiée des indices."""
    return (np.argmin(indices) if forward else np.argmax(indices)) // part


def find_word(line, word, forward=True):
    """Retourne l'indice de la première occurrence du mot dans la ligne."""
    return line.find(word) if forward else line.rfind(word)


def process_lines(lines, words, part):
    """Calcule la solution pour une partie spécifique."""
    total = 0

    for line in lines:
        indices = np.array([find_word(line, word) for word in words])
        indices[indices == -1] = len(line)
        total += 10 * get_digit(indices, part)

        indices = np.array([find_word(line, word, False) for word in words])
        total += get_digit(indices, part, False)

    return total


def main():
    """Fonction principale"""
    # Charger les lignes à partir du fichier
    with open('./input_1.txt', mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    # Partie 1
    words_part1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    total_part1 = process_lines(lines, words_part1, 1)
    print("Solution Partie 1 :", total_part1)

    # Partie 2
    words_part2 = ['zero', '0', 'one', '1', 'two', '2', 'three', '3', 'four', '4',
                   'five', '5', 'six', '6', 'seven', '7', 'eight', '8', 'nine', '9']
    total_part2 = process_lines(lines, words_part2, 2)
    print("Solution Partie 2 :", total_part2)


if __name__ == "__main__":
    # Appeler la fonction principale
    main()
