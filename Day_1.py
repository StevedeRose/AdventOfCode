import numpy as np

with open('./input_1.txt') as f:
    lines = f.readlines()

part = 1

# Part 1
if part == 1:
    words = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Part 2
if part == 2:
    words = ['zero', '0', 'one', '1', 'two', '2', 'three', '3', 'four', '4',
             'five', '5', 'six', '6', 'seven', '7', 'eight', '8', 'nine', '9']


def get_digit(indices, forward=True):
    return (np.argmin(indices) if forward else np.argmax(indices)) // part


def find_word(line, word, forward=True):
    return line.find(word) if forward else line.rfind(word)


total = 0

for line in lines:
    indices = np.array([find_word(line, word) for word in words])
    indices[indices == -1] = len(line)
    total += 10 * get_digit(indices)

    indices = np.array([find_word(line, word, False) for word in words])
    total += get_digit(indices, False)

print(total)
