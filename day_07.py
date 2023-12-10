"""
Description du module: Advent of Code Day 7
Auteur: Steve de Rose
Date de création: 07.12.2023
"""
import numpy as np

card_values1 = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5,
                '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

card_values2 = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5,
                '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}


def compute_score(hand, part=1):
    """
    Calcule le score d'une main de cartes.
    """
    card_values = card_values1 if part == 1 else card_values2
    figure = {}
    score = 0

    for card in hand:
        figure[card] = figure.get(card, 0) + 1
        score = score * 13 + card_values[card]

    if part == 2 and 'J' in figure and len(figure) > 1:
        j_count = figure.pop('J')
        figure[max(figure, key=figure.get)] += j_count

    unique_figures = len(figure)

    if unique_figures == 1:
        score += 371293 * 6
    elif unique_figures == 2:
        score += 371293 * (5 if max(figure.values()) == 4 else 4)
    elif unique_figures == 3:
        score += 371293 * (3 if max(figure.values()) == 3 else 2)
    elif unique_figures == 4:
        score += 371293

    return score


def get_hand_bid(line):
    """
    Extrait la main et l'enchère à partir d'une ligne de texte.
    """
    hand, bid = line.split()
    return list(hand), int(bid)


def calculate_total_bids(bids):
    """
    Calcule le total des enchères en utilisant une liste d'enchères.
    """
    return sum(bid * (index + 1) for index, bid in enumerate(bids[::-1]))


def read_input(file_path='./input_7.txt'):
    """
    Lit le fichier d'entrée et retourne les lignes non vides.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        lines = [line.split() for line in f.read().splitlines() if line]
    return lines


def get_solution(hands, bids, part):
    """
    Calcule la solution pour chaque partie.
    """
    scores = np.array([compute_score(hand, part) for hand in hands], dtype=int)
    sorted_indices = np.argsort(scores)[::-1]
    sorted_bids = np.array(bids)[sorted_indices]

    return calculate_total_bids(sorted_bids)


def main():
    """
    Fonction principale.
    """
    lines = read_input()

    hands, bids = zip(*[(list(hand), int(bid)) for hand, bid in lines])

    print('Solution Partie 1', ':', get_solution(hands, bids, 1))
    print('Solution Partie 2', ':', get_solution(hands, bids, 2))


if __name__ == "__main__":
    main()
