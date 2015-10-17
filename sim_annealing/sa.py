import random
import math

__author__ = 'anddor'


def sa_algorithm(problem, temp, d_temp):
    p = problem.get_start  # p is the current solution, not the value

    while True and temp:
        value = problem.obj_function(p)
        if value >= problem.target:
            return p

        neighbors = problem.generate_neighbors(p, 16)  # generates 16 neighbors
        p_max = max(neighbors, key=problem.obj_function)  # p_max is the current best next solution
        q = (problem.obj_function(p_max) - value) / max(value, 0.00000001)  # to avoid divide by zero
        value = min(1, math.exp(-q / temp))
        x = random.random()  # Will never return 1. Is this a problem?
        if x < value:
            p = p_max
        else:
            p = neighbors[random.randint(0, len(neighbors) - 1)]  # random neighbor

        temp -= d_temp
    return p
