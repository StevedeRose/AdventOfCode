"""
Description du module: Advent of Code Day 5
Auteur: Steve de Rose
Date de création: 05.12.2023
"""


class Plan:
    """
    Classe de traitement d'un plan de l'almanach.
    """

    def __init__(self, plan):
        self.tuples = [list(map(int, line.split())) for line in plan]

    def apply_once(self, seed):
        """
        Applique la fonction à une seule valeur.
        """
        for (dst, src, rng) in self.tuples:
            if src <= seed < src + rng:
                return seed + dst - src
        return seed

    def range_apply(self, ranges):
        """
        Applique la fonction à chaque intervalle de la liste 'ranges'.
        """
        return range_apply(self, ranges)


def parse_input(file_path='./input_05.txt'):
    """
    Lit le fichier d'entrée et retourne les graines et les plans.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        text = file.read().strip().split('\n\n')
        plans = [plan.splitlines()[1:] for plan in text[1:]]
        seeds = [int(x) for x in text[0].split(':')[1].split()]
    return seeds, plans


def range_apply(function, ranges):
    """
    Applique la fonction à chaque intervalle de la liste 'ranges'.
    """
    result = []
    for dest, src, rng in function.tuples:
        src_end = src + rng
        new_ranges = []
        while ranges:
            first, last = ranges.pop()
            before = (first, min(last, src))
            inter = (max(first, src), min(src_end, last))
            after = (max(src_end, first), last)
            if before[1] > before[0]:
                new_ranges.append(before)
            if inter[1] > inter[0]:
                result.append((inter[0] - src + dest, inter[1] - src + dest))
            if after[1] > after[0]:
                new_ranges.append(after)
        ranges = new_ranges
    return result + ranges


def main():
    """
    Fonction principale.
    """
    seeds, others = parse_input()
    plans = [Plan(plan) for plan in others]

    result_1 = seeds.copy()
    for plan in plans:
        result_1 = [plan.apply_once(seed) for seed in result_1]
    print("Solution Partie 1:", min(result_1))

    result_2 = []
    for seed_start, seed_range in zip(seeds[::2], seeds[1::2]):
        ranges = [(seed_start, seed_start + seed_range)]
        for plan in plans:
            ranges = plan.range_apply(ranges)
        result_2.append(min(ranges)[0])
    print("Solution Partie 2:", min(result_2))


if __name__ == "__main__":
    main()
