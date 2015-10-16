import copy
from math import ceil


# Problem: Egg carton

from random import randint


class EggCarton(object):
    def __init__(self, m, n, k):
        self.m = m  # rows
        self.n = n  # columns
        self.k = k  # constraint
        self.target = 1  # point at which we are satisfied

    @property
    def get_start(self):
        # create valid start position with zero eggs
        return []

    def collision_test(self, solution):
        """Counts the number of eggs in each row, column and diagonal"""
        row_list = [0] * self.m
        col_list = [0] * self.n
        right_diagonal_list = [0] * (self.m + self.n - 1)
        normal_right = int(ceil(len(right_diagonal_list) / 2))
        left_diagonal_list = [0] * (self.m + self.n - 1)

        for egg in solution:
            row_list[egg[0]] += 1
            col_list[egg[1]] += 1
            right_diagonal_list[egg[0] - egg[1] + normal_right] += 1
            left_diagonal_list[egg[0] + egg[1]] += 1

        max_count = max(max(row_list), max(col_list), max(right_diagonal_list), max(left_diagonal_list))
        if max_count > self.k:
            return True
        else:
            return False

    def random_neighbor(self, state):
        """Generates and returns random neighbor"""
        coin_flip = randint(0, 1)
        neighbor = copy.deepcopy(state)
        if coin_flip and state:  # list with len() > 0 resolves to True
            neighbor.pop(randint(0, len(neighbor) - 1))  # Remove one random egg
            return neighbor
        else:
            # Check if in list?
            neighbor.append((randint(0, self.m - 1), randint(0, self.n - 1)))  # add one egg
            return neighbor

    def generate_neighbors(self, state, number):
        """Creates n one more / one less egg combinations"""
        neighbors = []
        for _ in range(number):
            neighbors.append(self.random_neighbor(state))

        return neighbors

    def obj_function(self, solution):
        """Returns a rating [0,1] on the quality on the solution"""
        if self.collision_test(solution):
            # an invalid board returns 0
            return 0
        else:
            # valid boards returns egg amount divided by the total achievable eggs
            goal = min(self.m, self.n) * self.k
            eggs = len(solution)
            return eggs / goal
