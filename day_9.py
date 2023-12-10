"""
Description du module: Advent of Code Day 9
Auteur: Steve de Rose
Date de création: 09.12.2023
"""
from numpy import array


def compute_values(history):
    """
    Calcule les valeurs précédente et prochaine à partir de l'historique des nombres.
    """
    previous_value = next_value = 0
    sign = 1

    # Continue à calculer les valeurs jusqu'à ce que l'historique soit entièrement nul
    while not (history == 0).all():
        next_value += history[-1]
        previous_value += sign * history[0]
        history = history[1:] - history[:-1]
        sign *= -1

    return array([previous_value, next_value])


def read_input(file_path='./input_9.txt'):
    """
    Lit le fichier d'entrée et retourne les lignes non vides sous forme de listes d'entiers.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        lines = [list(map(int, line.split()))
                 for line in f.read().splitlines() if line]
    return lines


def main():
    """
    Fonction principale.
    """
    solutions = array([0, 0])
    lines = read_input()

    # Calcule les valeurs pour chaque ligne et agrège les solutions
    for line in lines:
        solutions += compute_values(array(line))

    print('Solution Partie 1 :', solutions[1])
    print('Solution Partie 2 :', solutions[0])


if __name__ == "__main__":
    main()
