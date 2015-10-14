from math import ceil
# Problem: Egg carton


class EggCarton(object):
    def __init__(self, m, n, k):
        self.m = m # rows
        self.n = n # columns
        self.k = k # constraint

    def get_start(self):
        # create random valid start position with zero eggs
        return []

    def collision_test(self, solution):
        row_list = [0] * self.m
        col_list = [0] * self.n
        right_diag_list = [0] * (self.m + self.n - 1)
        normal_right = ceil(len(right_diag_list) / 2)
        left_diag_list = [0] * (self.m + self.n - 1)

        for egg in solution:
            row_list[egg[0]] += 1
            col_list[egg[1]] += 1
            right_diag_list[egg[0] - egg[1] + normal_right] += 1
            left_diag_list[egg[0] + egg[1]] += 1

        if max(row_list, col_list, right_diag_list, left_diag_list) > self.k:
            return True
        else:
            return False

    def generate_neighbors(self, state):
        """Creates all the possible one more egg combinations"""
        combos = set()
        combos.add(state)
        for x in range(self.m):
            for y in range(self.n):
                combos.add()


    def obj_function(self, solution):
        """Returns a rating [0,1] on the quality on the solution"""
        if self.collision_test(solution):
            # an invalid board returns 0
            return 0
        else:
            # valid boards returns amount divided by the total achievable eggs
            goal = min(self.m, self.n) * self.k
            eggs = len(solution)
            return eggs/goal


