"""
Description du module: Advent of Code Day 16
Auteur: Steve de Rose
Date de création: 16.12.2023
"""
from collections import deque
import numpy as np


NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3


class Square:
    """
    Représente une case.
    """

    def __init__(self):
        self.exits = {NORTH, EAST, SOUTH, WEST}
        self.energized = False

    def lock(self, direction):
        """
        Ferme une direction de sortie.
        """
        self.exits.discard(direction)

    def next_directions(self, direction, value):
        """
        Détermine la/les direction(s) du rayon après son passage dans la case.
        """
        self.energized = True
        if value == '.':
            result = [direction] if direction in self.exits else []
        elif value == '-':
            result = [direction] if direction in (WEST, EAST) and direction in self.exits else [
                cardinal for cardinal in (EAST, WEST) if cardinal in self.exits]
        elif value == '\\':
            result = [cardinal for cardinal in (WEST, NORTH, EAST, SOUTH)
                      if direction == 3 - cardinal and cardinal in self.exits]
        elif value == '|':
            result = [direction] if direction in (NORTH, SOUTH) and direction in self.exits else [
                cardinal for cardinal in (NORTH, SOUTH) if cardinal in self.exits]
        else:
            result = [cardinal for cardinal in (WEST, NORTH, EAST, SOUTH)
                      if direction == (1 - cardinal) % 4 and cardinal in self.exits]
        for cardinal in result:
            self.lock(cardinal)
        return result


class Layout:
    """
    Représente l'agencement.
    """

    def __init__(self):
        self.data = self._parse_input_file()
        self.grid = np.full(self.data.shape, None, dtype=Square)
        self.reset()

    def reset(self):
        """
        Réinitalise l'agencement.
        """
        for i, j in np.ndindex(self.data.shape):
            self.grid[i, j] = Square()
            if i == 0 or i == self.data.shape[0] - 1:
                self.grid[i, j].lock(NORTH if i == 0 else SOUTH)
            if j == 0 or j == self.data.shape[1] - 1:
                self.grid[i, j].lock(WEST if j == 0 else EAST)

    def beam(self, i=0, j=0, direction=EAST):
        """
        Envoie un rayon dans la case (i, j) et vers 'direction'.
        """
        stack = deque([(i, j, direction)])
        while stack:
            i, j, direction = stack.pop()
            next_directions = self.grid[i, j].next_directions(
                direction, self.data[i, j])
            stack.extend((i + di, j + dj, next_direction) for di, dj, next_direction in
                         [(0, 1, EAST), (0, -1, WEST),
                          (-1, 0, NORTH), (1, 0, SOUTH)]
                         if next_direction in next_directions)

    def total(self):
        """
        Calcule le nombre de cases activées.
        """
        return np.count_nonzero([square.energized for square in self.grid.flat])

    @staticmethod
    def _parse_input_file():
        """
        Lit le fichier d'entrée et renvoie un tableau des données.
        """
        with open('./input_16.txt', mode='r', encoding='utf-8') as f:
            return np.array([list(l) for l in f.read().splitlines() if l])


def main():
    """
    Fonction principale.
    """
    layout = Layout()
    layout.beam()
    print(f'Solution Partie 1: {layout.total()}')

    maximum = 0
    height, width = layout.grid.shape
    for i, direction in enumerate([SOUTH, NORTH]):
        for j in range(width):
            layout.reset()
            layout.beam(-i, j, direction)
            maximum = max(maximum, layout.total())
    for j, direction in enumerate([EAST, WEST]):
        for i in range(height):
            layout.reset()
            layout.beam(i, -j, direction)
            maximum = max(maximum, layout.total())
    print(f'Solution Partie 2: {maximum}')


if __name__ == '__main__':
    main()
