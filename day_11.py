"""
Description du module: Advent of Code Day 11
Auteur: Steve de Rose
Date de création: 11.12.2023
"""
import numpy as np

def read_input(file_path='./input_11.txt'):
    """
    Lit le fichier d'entrée et l'image des galaxies.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        # Utilisation de np.array pour créer une matrice binaire directement à partir du fichier
        image = np.array([[1 if c == '#' else 0 for c in l] for l in f if l.strip()])
    return image

def find_empty_ranges(array):
    """
    Trouve les plages vides dans un tableau et renvoie leurs indices.
    """
    return [i for i, row in enumerate(array) if sum(row) == 0]

def adjust_galaxy_args(galaxy_args, empty_row_ranges, empty_col_ranges, multiplier):
    """
    Ajuste les coordonnées des positions galactiques en fonction des plages vides.
    """
    adjusted_args = galaxy_args.copy()
    for index, galaxy_arg in enumerate(galaxy_args):
        adjusted_args[index, 0] += sum(empty_row_ranges < galaxy_arg[0]) * multiplier
        adjusted_args[index, 1] += sum(empty_col_ranges < galaxy_arg[1]) * multiplier
    return adjusted_args

def compute_solution_part(image, multiplier):
    """
    Calcule la solution pour une partie du problème.
    """
    empty_row_ranges = find_empty_ranges(image)
    empty_col_ranges = find_empty_ranges(image.T)
    galaxy_args = np.argwhere(image == 1)

    adjusted_args = adjust_galaxy_args(galaxy_args, empty_row_ranges, empty_col_ranges, multiplier)

    solution = 0
    for index, g_1 in enumerate(adjusted_args[:-1]):
        for g_2 in adjusted_args[index + 1:]:
            solution += abs(g_2[0] - g_1[0]) + abs(g_2[1] - g_1[1])

    return solution

def compute_solutions(image):
    """
    Résoud les deux parties du problème.
    """
    solution_part_1 = compute_solution_part(image, 1)
    solution_part_2 = compute_solution_part(image, 999999)

    print('Solution Partie 1 :', solution_part_1)
    print('Solution Partie 2 :', solution_part_2)

def main():
    """
    Fonction principale
    """
    # Lecture de l'image à partir du fichier
    image = read_input()

    compute_solutions(image)

if __name__ == "__main__":
    main()
