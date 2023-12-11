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

    def range_apply(self, intervals):
        """
        Applique la fonction à chaque intervalle de la liste 'intervals'.
        """
        return range_apply(self, intervals)


def parse_input(file_path='./input_05.txt'):
    """
    Lit le fichier d'entrée et retourne les graines et les plans.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        text = file.read().strip().split('\n\n')
        plans = [plan.splitlines()[1:] for plan in text[1:]]
        seeds = [int(x) for x in text[0].split(':')[1].split()]
    return seeds, plans


def range_apply(function, intervals):
    """
    Applique la fonction à chaque intervalle de la liste 'intervals'.
    """
    result = []
    for dest, src, rng in function.tuples:
        src_end = src + rng
        new_intervals = []
        while intervals:
            first, last = intervals.pop()
            before = (first, min(last, src))
            inter = (max(first, src), min(src_end, last))
            after = (max(src_end, first), last)
            if before[1] > before[0]:
                new_intervals.append(before)
            if inter[1] > inter[0]:
                result.append((inter[0] - src + dest, inter[1] - src + dest))
            if after[1] > after[0]:
                new_intervals.append(after)
        intervals = new_intervals
    return result + intervals


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
        intervals = [(seed_start, seed_start + seed_range)]
        for plan in plans:
            intervals = plan.range_apply(intervals)
        result_2.append(min(intervals)[0])
    print("Solution Partie 2:", min(result_2))


if __name__ == "__main__":
    main()
