with open('./input_4.txt') as f:
    lines = f.read().splitlines()


total = 0

for line in lines:
    win_cards, my_cards = [list(map(int, cards.split()))
                           for cards in line[line.find(':') + 2:].split(' | ')]
    nb_win = sum(my_card in win_cards for my_card in my_cards)
    total += 2**(nb_win - 1) if nb_win > 0 else 0

print(total)
