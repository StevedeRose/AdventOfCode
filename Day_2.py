with open('./input_2.txt') as f:
    lines = f.read().splitlines()

part = 1

total = 0

for index, line in enumerate(lines):
    line = line[line.find(':')+2:]

    sets = line.split('; ')

    numbers = {'red': 0, 'green': 0, 'blue': 0}
    for set in sets:
        nums_cols = set.split(', ')
        for couple in nums_cols:
            num_col = couple.split(' ')
            numbers[num_col[1]] = max(numbers[num_col[1]], int(num_col[0]))
    
    if part == 1 and numbers['red'] < 13 and numbers['green'] < 14 and numbers['blue'] < 15:
        total += index + 1
    elif part == 2:
        total += numbers['red'] * numbers['green'] * numbers['blue']

print(total)