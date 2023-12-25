"""
Description du module: Advent of Code Day 20
Auteur: Steve de Rose
Date de création: 20.12.2023
"""
from collections import deque
from itertools import count
from math import lcm
import dataclasses


@dataclasses.dataclass
class PulseData:
    """
    Données d'une impulsion.
    """
    sender: str
    receiver: str
    pulse: bool


def propagate_pulse(graph, flipflops, conjunctions, pulse_data):
    """
    Propage un impulsion.
    """
    receiver = pulse_data.receiver

    if receiver in flipflops:
        if pulse_data.pulse:
            return
        next_pulse = flipflops[receiver] = not flipflops[receiver]
    elif receiver in conjunctions:
        conjunctions[receiver][pulse_data.sender] = pulse_data.pulse
        next_pulse = not all(conjunctions[receiver].values())
    elif receiver in graph:
        next_pulse = pulse_data.pulse
    else:
        return

    for new_receiver in graph[receiver]:
        yield PulseData(receiver, new_receiver, next_pulse)


def press_button(graph, flipflops, conjunctions):
    """
    Appuie sur le bouton.
    """
    queue = deque([PulseData('button', 'broadcaster', False)])
    high_num = low_num = 0

    while queue:
        pulse_data = queue.popleft()
        high_num += pulse_data.pulse
        low_num += not pulse_data.pulse
        queue.extend(propagate_pulse(graph, flipflops, conjunctions, pulse_data))

    return high_num, low_num


def find_periods(graph, flipflops, conjunctions):
    """
    Recherche les périodes pour pouvoir calculer leurr PPCM et répondre à la partie 2.
    """
    periodic = set()
    rx_source = next(
        (rx_src for rx_src, destinations in graph.items() if destinations == ['rx']), None)

    for source, destinations in graph.items():
        if rx_source in destinations:
            assert source in conjunctions
            periodic.add(source)

    for iteration in count(1):
        queue = deque([PulseData('button', 'broadcaster', False)])

        while queue:
            pulse_data = queue.popleft()

            if not pulse_data.pulse and pulse_data.receiver in periodic:
                yield iteration
                periodic.discard(pulse_data.receiver)

                if not periodic:
                    return

            queue.extend(propagate_pulse(
                graph, flipflops, conjunctions, pulse_data))


def parse_input(file_path='input_20.txt'):
    """
    Lit les données du problème et les classe dans des dictionnaires.
    """
    flipflops = {}
    conjunctions = {}
    graph = {}

    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            source, destinations = map(str.strip, line.split('->'))
            destinations = destinations.split(', ')

            if source.startswith('%'):
                source = source[1:]
                flipflops[source] = False
            elif source.startswith('&'):
                source = source[1:]
                conjunctions[source] = {}

            graph[source] = destinations

    return graph, conjunctions, flipflops


def main():
    """
    Fonction principale.
    """
    graph, conjunctions, flipflops = parse_input()
    high_count = low_count = 0

    for source, destinations in graph.items():
        for dest in filter(conjunctions.__contains__, destinations):
            conjunctions[dest][source] = False

    for _ in range(1000):
        high_num, low_num = press_button(graph, flipflops, conjunctions)
        high_count += high_num
        low_count += low_num

    print('Solution Partie 1 :', low_count * high_count)

    for key in flipflops:
        flipflops[key] = False

    for inputs in conjunctions.values():
        for key in inputs:
            inputs[key] = False

    print('Solution Partie 2 :', lcm(
        *find_periods(graph, flipflops, conjunctions)))


if __name__ == "__main__":
    main()
