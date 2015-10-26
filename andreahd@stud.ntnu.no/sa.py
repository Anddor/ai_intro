import os
import random
import math

__author__ = 'anddor'


def sa_algorithm(problem, temp, d_temp):
    p = problem.get_start  # p is the current solution, not the value
    start_temp = temp
    while True and temp > 0:

        value = problem.obj_function(p)
        # print status:
        os.system('clear')
        progress = "=" * int(math.floor(value * 10))
        left = " " * int(math.floor((1 - value) * 10))
        print "Progress: [{} {}]".format(progress, left)

        temp_progress = "=" * int(math.floor(start_temp / temp * 10))
        temp_left = " " * int( math.ceil(1 - (start_temp / temp * 10)))
        print "Temp: [{} {}]".format(temp_progress, temp_left)

        if value >= problem.target:
            return p

        neighbors = problem.generate_neighbors(p, 30)  # generates 30 neighbors
        p_max = max(neighbors, key=problem.obj_function)  # p_max is the current best next solution
        q = (problem.obj_function(p_max) - value) / max(value, 0.01)  # to avoid divide by zero
        small_p = min(1, math.exp(-q / temp))  #

        x = random.random()  # Will never return 1. Is this a problem?
        if x > small_p:
            p = p_max  # exploit
        else:
            p = neighbors[random.randint(0, len(neighbors) - 1)]  # explore

        temp -= d_temp

    print("freeze")
    return p
