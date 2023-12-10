"""
Description du module: Advent of Code Day 4
Auteur: Steve de Rose
Date de création: 04.12.2023
"""
import numpy as np


def load_file(file_path):
    """
    Charge le contenu du fichier d'entrée.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        lignes = f.read().splitlines()
    return lignes


def solution_partie_1(lignes):
    """
    Calcule la solution de la partie 1 du problème Advent of Code Day 4.
    """
    total = 0

    for ligne in lignes:
        win_cards, my_cards = [list(map(int, cartes.split()))
                               for cartes in ligne[ligne.find(':') + 2:].split(' | ')]
        nb_win = sum(my_card in win_cards for my_card in my_cards)
        total += 2**(nb_win - 1) if nb_win > 0 else 0

    return total


def solution_partie_2(lignes):
    """
    Calcule la solution de la partie 2 du problème Advent of Code Day 4.
    """
    nb_copies = np.ones_like(lignes, dtype=int)

    for index, ligne in enumerate(lignes):
        win_cards, my_cards = [list(map(int, cartes.split()))
                               for cartes in ligne[ligne.find(':') + 2:].split(' | ')]
        nb_win = sum(my_card in win_cards for my_card in my_cards)
        if nb_win > 0:
            nb_copies[index + 1: index + nb_win + 1] += nb_copies[index]

    return np.sum(nb_copies)


def main():
    """
    Fonction principale.
    """
    file_path = './input_4.txt'
    lignes = load_file(file_path)

    solution_p1 = solution_partie_1(lignes)
    print('Solution Partie 1 :', solution_p1)

    solution_p2 = solution_partie_2(lignes)
    print('Solution Partie 2 :', solution_p2)


if __name__ == "__main__":
    main()
