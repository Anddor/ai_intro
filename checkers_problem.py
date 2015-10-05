import search_node
import math

__author__ = 'Andreas'


class Problem(object):
    def __init__(self, goal_state, initial_state):
        self.goal_state = goal_state
        self.initial_state = initial_state

    def print_state(self, state):
        for line in state:
            print(line)

    def goal_test(self, state):
        for col in range(len(state)):
            for row in range(len(state[col])):
                if not self.goal_state[col][row] == state[col][row]:
                    return False

    def distance_to_goal(self, num, x_pos, y_pos):

        # Find num in goal:
        goal_x = -1
        goal_y = -1

        for col in range (len(self.goal_state)):
            for row in range(len(self.goal_state[col])):
                if self.goal_state[col][row] == num:
                    goal_x = col
                    goal_y = row

        # compute distance
        if goal_x == -1:
            raise ValueError("Num not found in goal error")
        else:
            distance = math.fabs(goal_x - x_pos) + math.fabs(goal_y - y_pos)
            return distance

    def heuristic(self, state):
        total = 0
        for col in range(len(state)):
            for row in range(len(state[col])):
                total += self.distance_to_goal(state[row][col], col, row)
        return total

    def generate_children(self, node):
        children = []
        state = node.state
        for col in range(len(state)-1):
            for row in range(len(state[col])-1):
                hor_child_state = state.copy()
                hor_child_state[col][row], hor_child_state[col + 1][row] \
                    = hor_child_state[col + 1][row], hor_child_state[col][row]

                hor_child = search_node.SearchNode(hor_child_state, node.g + 1, self.heuristic(hor_child_state), node)

                ver_child_state = state.copy()
                ver_child_state[col][row], ver_child_state[col][row + 1] \
                    = ver_child_state[col][row + 1], ver_child_state[col][row]

                ver_child = search_node.SearchNode(ver_child_state, node.g + 1, self.heuristic(ver_child_state), node)

                children.extend([hor_child, ver_child])

        return children




