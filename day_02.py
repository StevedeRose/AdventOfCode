"""
Description du module: Advent of Code Day 2
Auteur: Steve de Rose
Date de création: 03.12.2023
"""


def process_line(line):
    """
    Fonction pour traiter une ligne du fichier et extraire les informations nécessaires.
    """
    line = line[line.find(':') + 2:]

    sets = line.split('; ')

    numbers = {'red': 0, 'green': 0, 'blue': 0}
    for set_str in sets:
        nums_cols = set_str.split(', ')
        for couple in nums_cols:
            num_col = couple.split()
            numbers[num_col[1]] = max(numbers[num_col[1]], int(num_col[0]))

    return numbers


def main():
    """
    Fonction principale.
    """
    with open('./input_02.txt', mode='r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    total_part_1 = total_part_2 = 0

    for index, line in enumerate(lines):
        numbers = process_line(line)

        # Vérification pour la Partie 1
        if numbers['red'] < 13 and numbers['green'] < 14 and numbers['blue'] < 15:
            total_part_1 += index + 1

        # Calcul pour la Partie 2
        total_part_2 += numbers['red'] * numbers['green'] * numbers['blue']

    # Affichage des solutions
    print('Solution Partie 1 :', total_part_1)
    print('Solution Partie 2 :', total_part_2)


if __name__ == "__main__":
    main()
