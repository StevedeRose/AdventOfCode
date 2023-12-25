"""
Description du module: Advent of Code Day 25
Auteur: Steve de Rose
Date de création: 25.12.2023
"""
import random
from collections import defaultdict, deque

NUM_MONTE_CARLO_RUNS = 100


def read_graph_from_file(file_path='input_25.txt'):
    """
    Lit les informations du graphe depuis le fichier d'entrée et retourne un defaultdict de listes.
    Chaque nœud est une clé, et ses voisins sont stockés dans une liste.
    """
    graph = defaultdict(list)
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            node, links = line.strip().split(': ')
            links = links.split()
            graph[node].extend(links)
            for neighbor in links:
                graph[neighbor].append(node)
    return graph


def get_component_size(graph, root, banned_edges):
    """
    Calcule la taille d'une composante connexe après avoir écarté les arêtes interdites.
    Utilise une approche itérative au lieu d'une approche récursive.
    """
    stack = [root]
    seen_nodes = {root}

    while stack:
        node = stack.pop()
        new_nodes = [neighbor for neighbor in graph[node]
                     if neighbor not in seen_nodes and (node, neighbor) not in banned_edges
                     and (neighbor, node) not in banned_edges]
        seen_nodes.update(new_nodes)
        stack.extend(new_nodes)

    return len(seen_nodes)


def get_shortest_path(graph, start, end):
    """
    Trouve le chemin le plus court entre start et end dans le graphe en utilisant BFS.
    Utilise une approche itérative au lieu d'une approche récursive.
    """
    previous_node = {start: start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor in previous_node:
                continue

            previous_node[neighbor] = node
            queue.append(neighbor)

    if previous_node.get(end) is None:
        return None

    path = []
    node = end
    while node != start:
        path.append(node)
        node = previous_node[node]

    path.append(start)
    return path[::-1]


def main():
    """
    Fonction principale pour exécuter le programme.
    """
    graph = read_graph_from_file()

    while True:
        edge_usage_count = defaultdict(int)

        for _ in range(NUM_MONTE_CARLO_RUNS):
            node_a, node_b = random.sample(list(graph.keys()), 2)
            path = get_shortest_path(graph, node_a, node_b)

            for u, v in zip(path, path[1:]):
                edge = tuple(sorted([u, v]))
                edge_usage_count[edge] += 1

        sorted_edge_usage = sorted(
            edge_usage_count.items(), key=lambda x: x[1], reverse=True)
        banned_edges = [edge[0] for edge in sorted_edge_usage[:3]]

        size_component_1 = get_component_size(
            graph, banned_edges[0][0], banned_edges)
        size_component_2 = get_component_size(
            graph, banned_edges[0][1], banned_edges)

        if size_component_1 + size_component_2 == len(graph):
            break

    print('Solution du problème :', size_component_1 * size_component_2)


if __name__ == "__main__":
    main()
