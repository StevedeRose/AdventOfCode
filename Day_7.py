import argparse
import numpy as np

card_values1 = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5,
                '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

card_values2 = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6,
                '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}


def parse_arguments():
    parser = argparse.ArgumentParser(description='Calculate total bids based on hands and bids from a file.')
    parser.add_argument('--file', type=str, default='./input_7.txt', help='Path to the input file')
    parser.add_argument('--part', type=int, choices=[1, 2], default=1, help='Part value (1 or 2)')
    return parser.parse_args()

def score(hand, part=1):
    card_values = card_values1 if part == 1 else card_values2
    figure = {}
    score = 0

    for card in hand:
        figure[card] = figure.get(card, 0) + 1
        score = score * 13 + card_values[card]

    if part == 2:
        if 'J' in figure.keys() and len(figure) > 1:
            j_count = figure.pop('J')
            figure[max(figure, key=figure.get)] += j_count

    unique_figures = len(figure)

    if unique_figures == 1:
        score += 371293 * 6
    elif unique_figures == 2:
        max_count = max(figure.values())
        score += 371293 * (5 if max_count == 4 else 4)
    elif unique_figures == 3:
        max_count = max(figure.values())
        score += 371293 * (3 if max_count == 3 else 2)
    elif unique_figures == 4:
        score += 371293

    return score


def get_hand_bid(line):
    hand, bid = line.split()
    return list(hand), int(bid)


def calculate_total_bids(bids):
    return sum(bid * (index + 1) for index, bid in enumerate(bids[::-1]))


def main():
    args = parse_arguments()

    with open(args.file) as f:
        lines = [line.split() for line in f.read().splitlines() if line]

    hands, bids = zip(*[(list(hand), int(bid)) for hand, bid in lines])

    scores = np.array([score(hand, args.part) for hand in hands], dtype=int)
    sorted_indices = np.argsort(scores)[::-1]
    sorted_bids = np.array(bids)[sorted_indices]

    total = calculate_total_bids(sorted_bids)
    print('Résultat de la partie', args.part, ':', total)


if __name__ == "__main__":
    main()
