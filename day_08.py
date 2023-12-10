"""
Description du module: Advent of Code Day 8
Auteur: Steve de Rose
Date de création: 08.12.2023
"""
from itertools import cycle
from math import lcm


def calculate_trace_length(start_node, pattern, node_mappings, node_end):
    """
    Calcule la longueur de la trace en utilisant le motif donné et les correspondances de nœuds.
    """
    trace_length = 0
    while not start_node.endswith(node_end):
        start_node = node_mappings[start_node][next(pattern)]
        trace_length += 1
    return trace_length


def part1_solution(pattern, node_mappings):
    """
    Calcule et affiche la solution pour la Partie 1 du problème.
    """
    print("Solution Partie 1 :", calculate_trace_length(
        'AAA', cycle(pattern), node_mappings, 'ZZZ'))


def part2_solution(pattern, node_mappings):
    """
    Calcule et affiche la solution pour la Partie 2 du problème.
    """
    start_nodes = [x for x in node_mappings.keys() if x.endswith('A')]
    trace_lengths = [calculate_trace_length(start_node, cycle(
        pattern), node_mappings, 'Z') for start_node in start_nodes]
    print("Solution Partie 2 :", lcm(*trace_lengths))


def read_input(file_path="./input_8.txt"):
    """
    Lit les données à partir du fichier spécifié et
    renvoie le motif et les correspondances de nœuds.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    pattern = lines[0]
    node_mappings = {line[:3]: {'L': line[7:10],
                                'R': line[12:15]} for line in lines[2:]}
    return pattern, node_mappings


def main():
    """
    Fonction principale.
    """
    pattern, node_mappings = read_input()
    part1_solution(pattern, node_mappings)
    part2_solution(pattern, node_mappings)


if __name__ == "__main__":
    main()
