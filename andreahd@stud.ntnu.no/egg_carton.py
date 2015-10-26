import copy
from math import ceil
from random import sample

# Problem: Egg carton

from random import randint


class EggCarton(object):
    def __init__(self, m, n, k):
        self.m = m  # rows
        self.n = n  # columns
        self.k = k  # constraint
        self.target = 1  # point at which we are satisfied
        self.full_set = set()
        for x in range(self.m):
            for y in range(self.n):
                self.full_set.add((x, y))

    @property
    def get_start(self):
        # create valid start position with zero eggs

        solution_set = set()
        return solution_set

    def collision_test(self, solution):
        """Counts the number of eggs in each row, column and diagonal"""
        row_list = [0] * self.m
        col_list = [0] * self.n
        right_diagonal_list = [0] * (self.m + self.n - 1)
        normal_right = int(ceil(len(right_diagonal_list) / 2))
        left_diagonal_list = [0] * (self.m + self.n - 1)

        for egg in solution:
            col_list[egg[0]] += 1
            row_list[egg[1]] += 1
            right_diagonal_list[egg[0] - egg[1] + normal_right] += 1
            left_diagonal_list[egg[0] + egg[1]] += 1

        max_count = max(max(row_list), max(col_list), max(right_diagonal_list), max(left_diagonal_list))
        if max_count > self.k:
            return max_count
        else:
            return False

    def random_neighbor(self, state):
        """Generates and returns random neighbor"""
        coin_flip = randint(0, 1)
        neighbor = copy.deepcopy(state)
        if coin_flip and state:  # list with len() > 0 resolves to True
            neighbor.remove(sample(neighbor, 1)[0])  # Does not remove "random" egg
            return neighbor
        else:
            # make set of free positions
            free_positions = self.full_set - state
            if not free_positions:
                print("no free positions!")
            # Pull random from free positions
            neighbor.add(sample(free_positions, 1)[0])  # add one egg
            return neighbor

    def generate_neighbors(self, state, number):
        """Creates n one more / one less egg combinations"""
        neighbors = []
        for _ in range(number):
            neighbors.append(self.random_neighbor(state))

        return neighbors

    def obj_function(self, solution):
        """Returns a rating [0, 1] on the quality on the solution"""

        collisions = self.collision_test(solution)
        if collisions:
            # an invalid board returns
            overflow = collisions - self.k
            return -overflow
        else:
            # valid boards returns egg amount divided by the total achievable eggs
            goal = float(min(self.m, self.n) * self.k)
            eggs = float(len(solution))
            egg_ratio = min(eggs / goal, 1)
            return egg_ratio
