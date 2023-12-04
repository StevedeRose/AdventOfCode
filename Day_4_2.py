import numpy as np

input_file_path = './input_4.txt'

with open(input_file_path) as f:
    lines = f.read().splitlines()

nb_copies = np.ones_like(lines, dtype=int)
total = 0

for index, line in enumerate(lines):
    win_cards, my_cards = [list(map(int, cards.split()))
                           for cards in line[line.find(':') + 2:].split(' | ')]
    nb_win = sum(my_card in win_cards for my_card in my_cards)
    if nb_win > 0:
        nb_copies[index + 1: index + nb_win + 1] += nb_copies[index]

print(np.sum(nb_copies))
