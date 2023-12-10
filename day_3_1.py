"""
Description du module: Advent of Code Day 3 Part 1
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
    nrow, ncol = grid.shape

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < nrow and 0 <= c < ncol and grid[r, c] != '.' and not grid[r, c].isdigit():
            return True

    return False


def compute_total(grid):
    """
    Calcule la somme des nombres valides dans la grille.
    """
    total = 0
    row_num, col_num = grid.shape

    for row in range(row_num):
        col = 0
        while col < col_num:
            nombre = ""
            est_nombre = False

            while col < col_num and grid[row, col].isdigit():
                nombre += grid[row, col]
                est_nombre = est_nombre or is_valid(row, col, grid)
                col += 1

            if est_nombre:
                total += int(nombre)

            col += 1

    return total

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
