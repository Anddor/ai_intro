from random import random

__author__ = 'anddor'


def sa_algorithm(problem):
    p = problem.get_start()
    temp = problem.get_tmax()
    d_temp = problem.dTemp

    while True:
        value = problem.obj_function(p)
        if value >= problem.target:
            return p

        neighbors = problem.generate_neighbors(p)
        p_max = max(neighbors, key=problem.obj_function())
        q = (problem.obj_function(p_max) - value) / value
        x = random.random()  # Will never return 1. Is this a problem?
        if x > p:
            p = p_max
        else:
            p = neighbors[random.randint(0, len(neighbors))]

        temp -= d_temp
