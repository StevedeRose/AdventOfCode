"""
Description du module: Advent of Code Day 3 Part 2
Auteur: Steve de Rose
Date de création: 03.12.2023
"""
import numpy as np


def load_grid(path):
    """
    Charge une grille à partir d'un fichier texte.
    """
    with open(path, mode='r', encoding='utf-8') as f:
        lignes = f.read().splitlines()

    return np.array([list(ligne) for ligne in lignes])


def is_valid(row, col, grid):
    """
    Vérifie si la position (row, col) dans la grille est valide.
    """
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, -1), (-1, 1), (1, -1)]
    row_num, col_num = grid.shape

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < row_num and 0 <= c < col_num and grid[r, c] == '*':
            return (r, c)

    return None

def compute_total(grid):
    """
    Calcule le résultat final.
    """
    row_num, col_num = grid.shape

    stars = {(row, col): [] for row in range(row_num)
            for col in range(col_num) if grid[row, col] == '*'}

    for row in range(row_num):
        col = 0
        while col < col_num:
            number = ""
            is_number = False
            neighbors = set()

            while col < col_num and grid[row, col].isdigit():
                number += grid[row, col]
                star = is_valid(row, col, grid)
                if star:
                    neighbors.add(star)
                    is_number = True
                col += 1

            if is_number:
                for star in neighbors:
                    stars[star].append(int(number))

            col += 1

    return sum(vec[0] * vec[1] for vec in stars.values() if len(vec) == 2)


def main():
    """
    Fonction principale
    """
    chemin_fichier = './input_3.txt'
    grille = load_grid(chemin_fichier)
    print(compute_total(grille))


if __name__ == "__main__":
    # Utilisation des docstrings pour expliquer l'utilisation du code
    main()
