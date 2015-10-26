__author__ = 'anddor'


def triangle(position, x0, x1, x2, clip):
    """Membership function for triangle"""
    # ___/\___
    # x0 x1 x2

    value = 0.0
    if x0 <= position <= x1:
        value = (position - x0) / (x1 - x0)
    elif x1 <= position <= x2:
        value = (x2 - position) / (x1 - x0)
    value = min(value, clip)
    return value


def grade(position, x0, x1, clip):
    """Membership function for grade:"""
    #     ___
    # ___/
    # x0  x1
    value = 0.0
    if position >= x1:
        value = 1.0
    elif position <= x0:
        value = 0.0
    else:
        value = (position - x0) / (x1 - x0)
    value = min(value, clip)
    return value


def reverse_grade(position, x0, x1, clip):
    """Membership function for reverse grade"""
    # ___
    #    \___
    # x0  x1
    value = 0.0
    if position <= x0:
        value = 1.0
    elif position >= x1:
        value = 0.0
    else:
        value = (x1 - position) / (x1 - x0)
    value = min(value, clip)
    return value


def rule_eval(input1, method, input2):
    if method == 'or':
        return max(input1, input2)
    elif method == 'and':
        return min(input1, input2)


def mamdani(input_sets, action_set, inputs):
    # step 1: fuzzification
    fuzzy_list = []
    for i, crisp in enumerate(inputs):
        # each of the inputs
        match_dict = dict()
        for j, fuzzy in enumerate(input_sets[i].items()):
            # Ratio of match to each of the sets
            print(crisp)
            if fuzzy[0] == 'VerySmall' or fuzzy[0] == 'ShrinkingFast':
                fuzzy_value = reverse_grade(crisp, fuzzy[1][0], fuzzy[1][1], 1)
            elif fuzzy[0] == 'VeryBig' or fuzzy[0] == 'GrowingFast':
                fuzzy_value = grade(crisp, fuzzy[1][0], fuzzy[1][1], 1)
            else:
                fuzzy_value = triangle(crisp, fuzzy[1][0], fuzzy[1][1], fuzzy[1][2], 1)

            match_dict[fuzzy[0]] = fuzzy_value
        fuzzy_list.append(match_dict)

def main():
    distance_sets = {'VerySmall': (1, 2.5, None),
                     'Small': (1.5, 3, 4.5),
                     'Perfect': (3.5, 5, 6.5),
                     'Big': (3.5, 7, 8.5),
                     'VeryBig': (7.5, 9, None)}
    delta_sets = {'ShrinkingFast': (-4, -2.5, None),
                  'Shrinking': (-3.5, -2, -0.5),
                  'Stable': (-1.5, 0, 1.5),
                  'Growing': (0.5, 2, 3.5),
                  'GrowingFast': (2.5, 4, None)}
    input_sets = [distance_sets, delta_sets]

    action_set = {'BrakeHard': (-8, -5, None),
                  'SlowDown': (-7, -4, -1),
                  'None': (-3, 0, 3),
                  'SpeedUp': (1, 4, 7),
                  'FloorIt': (5, 10, None)}

    inputs = [3.4, 0.9]
    mamdani(input_sets, action_set, inputs)


main()
