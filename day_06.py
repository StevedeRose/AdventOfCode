"""
Description du module: Advent of Code Day 6
Auteur: Steve de Rose
Date de création: 06.12.2023
"""
import re
import math


def best_distances_number(temps, distance):
    """
    Calcule le nombre de chemins possibles en fonction du temps et de la distance.
    """
    discriminant = math.sqrt(temps ** 2 - 4 * distance)
    min_temps = math.ceil((temps - discriminant) / 2 + 1e-4)
    max_temps = math.floor((temps + discriminant) / 2 - 1e-4)

    return max_temps - min_temps + 1


def read_input(file_path='./input_06.txt'):
    """
    Lit le fichier d'entrée et retourne les lignes non vides.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        lines = [line for line in f.read().splitlines() if line]
    return lines


def main():
    """
    Fonction principale.
    """
    lines = read_input()

    temps_liste = [int(temps) for temps in re.findall(r'\d+', lines[0])]
    distances_liste = [int(distance)
                       for distance in re.findall(r'\d+', lines[1])]

    answer_1 = 1
    for temps, distance in zip(temps_liste, distances_liste):
        answer_1 *= best_distances_number(temps, distance)

    temps = int(lines[0].replace(' ', '').split(':')[1])
    distance = int(lines[1].replace(' ', '').split(':')[1])

    print('Solution Partie 1 :', answer_1)
    print('Solution Partie 2 :', best_distances_number(temps, distance))


if __name__ == "__main__":
    main()
