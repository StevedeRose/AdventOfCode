"""
Description du module: Advent of Code Day 19
Auteur: Steve de Rose
Date de création: 19.12.2023
"""

INVERSE = {'<': '>', '>': '<'}
OPERATOR_MAPPING = {'<': lambda a, b: a < b, '>': lambda a, b: a > b}


def evaluate_condition(condition, part):
    """
    Évalue une condition.
    """
    x, op, y = condition[0], condition[1], condition[2:]
    return OPERATOR_MAPPING[op](part[x], int(y))


def process_part(workflows, part):
    """
    Traite une pièce selon les plans.
    """
    current_workflow = 'in'

    while True:
        workflow = workflows[current_workflow]

        for condition, destination in workflow:
            if not condition or evaluate_condition(condition, part):
                if destination in {'R', 'A'}:
                    return None if destination == 'R' else part

                current_workflow = destination
                break


def parse_input(file_path='./input_19.txt'):
    """
    Lit le fichier d'entrée et renvoie les dictionnaires des plans et des pièces.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        workflows_raw, parts_raw = f.read().split('\n\n')

    workflows = {}
    for line in workflows_raw.splitlines():
        if line:
            name, rules = line[:-1].split('{')
            workflows[name] = [tuple(rule.split(':')) if ':' in rule else (
                '', rule) for rule in rules.split(',')]

    parts = [dict((key, int(value)) for data in part.strip('{}').split(
        ',') for key, value in [data.split('=')]) for part in parts_raw.split('\n') if part]

    return workflows, parts


def process_rule(rule):
    """
    Traite une règle.
    """
    vals = {var: [False] + [True] * 4000 for var in 'xmas'}

    for condition in rule:
        if condition:
            var, op, bound = condition[0], condition[1], int(condition[2:])
            start, end = (0, bound) if op == '<' else (bound + 1, 4001)
            for index in range(start, end):
                vals[var][index] = False

    result = 1
    for value in vals.values():
        result *= sum(value)

    return result


def invert_rule(rule):
    """
    Inverse une règle de comparaison.
    """
    return rule[0] + INVERSE[rule[1]] + rule[2:]


def process_workflow(name, old_rules, workflows):
    """
    Traite un plan.
    """
    total = 0
    new_rules = []

    for rule, workflow in workflows[name]:
        if workflow != 'R':
            rules = old_rules + new_rules + [rule]
            total += (process_rule(rules) if workflow ==
                      'A' else process_workflow(workflow, rules, workflows))

        if rule:
            new_rules.append(invert_rule(rule))

    return total


def main():
    """
    Fonction principale.
    """
    workflows, parts = parse_input()

    total_rating = sum(sum(part.values()) for part in filter(
        None, (process_part(workflows, part) for part in parts)))
    print('Solution Partie 1 :', total_rating)

    result = process_workflow('in', [], workflows)
    print('Solution Partie 2 :', result)


if __name__ == "__main__":
    main()
