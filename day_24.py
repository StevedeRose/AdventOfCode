"""
Description du module: Advent of Code Day 24
Auteur: Steve de Rose
Date de création: 24.12.2023
"""
import numpy as np

MIN_POSITION, MAX_POSITION = 2e14, 4e14


def read_input(file_path='input_24.txt'):
    """
    Lit le contenu du fichier spécifié par le chemin et renvoie les lignes en tant que liste.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        return file.read().splitlines()


def parse_data(data):
    """
    Analyse les données d'entrée et renvoie une liste de chemins représentés par des tuples.
    """
    return [tuple(tuple(map(int, coord.split(', ')))
                  for coord in line.split(' @ ')) for line in data]


def find_intersection_xy(path1, path2):
    """
    Trouve le point d'intersection des chemins dans le plan XY.
    """
    (ix1, iy1, _), (sx1, sy1, _) = path1
    (ix2, iy2, _), (sx2, sy2, _) = path2
    denominator = sx1 * sy2 - sx2 * sy1

    if denominator == 0:
        return (0, 0)

    numerator = (ix2 - ix1) * sy1 * sy2 + sx1 * sy2 * iy1 - sx2 * sy1 * iy2
    y = numerator / denominator
    x = y * sx1 / sy1 + ix1 - sx1 * iy1 / sy1

    return (x, y)


def is_valid_intersection(path1, path2):
    """
    Vérifie si le point d'intersection des chemins est valide dans la plage spécifiée.
    """
    x, y = find_intersection_xy(path1, path2)
    return MIN_POSITION <= x <= MAX_POSITION and MIN_POSITION <= y <= MAX_POSITION and \
           (x - path1[0][0]) * path1[1][0] > 0 and (x - path2[0][0]) * path2[1][0] > 0


def solution_part_one(paths):
    """
    Compte le nombre d'intersections valides entre les chemins.
    """
    return sum(is_valid_intersection(path1, path2)
               for i, path1 in enumerate(paths[:-1])
               for path2 in paths[i + 1:])


def build_jacobian_matrix(x, velocities):
    """
    Construit la matrice jacobienne utilisée dans la méthode de moindres carrés.
    """
    nrows = len(velocities)
    data = np.zeros((nrows * 3, 6 + nrows))
    for i, (xis, velocity) in enumerate(zip(x[6:], velocities)):
        index = 3 * i
        data[index:index + 3, :3] = np.eye(3)
        data[index:index + 3, 3:6] = np.eye(3) * xis
        data[index:index + 3, 6 + i] = x[3:6] - velocity
    return data


def calculate_function_values(x, positions, velocities):
    """
    Calcule les valeurs de la fonction utilisée dans la méthode de moindres carrés.
    """
    data = np.zeros(3 * len(positions))
    for i, (position, velocity) in enumerate(zip(positions, velocities)):
        t = x[6 + i]
        calculated_position = x[:3] + x[3:6] * t
        predicted_position = position + velocity * t
        index = 3 * i
        data[index:index + 3] = calculated_position - predicted_position
    return data


def solution_part_two(paths):
    """
    Trouve la position initale en utilisant la méthode des moindres carrés
    et retourne la somme de ses coordonnées.
    """
    positions = np.array([row[0] for row in paths])
    velocities = np.array([row[1] for row in paths])
    x = np.zeros(len(paths) + 6)
    x[3:6] = 1

    temp = 0
    while True:
        jacobian_matrix = build_jacobian_matrix(x, velocities)
        function_values = calculate_function_values(x, positions, velocities)
        x -= np.linalg.lstsq(jacobian_matrix, function_values, rcond=None)[0]
        result = np.sum(x[:3])
        if result == temp:
            return int(result)
        temp = result


def main():
    """
    Fonction principale pour exécuter le programme.
    """
    paths = parse_data(read_input())

    print('Solution Partie 1 :', solution_part_one(paths))
    print('Solution Partie 2 :', solution_part_two(paths))


if __name__ == '__main__':
    main()
