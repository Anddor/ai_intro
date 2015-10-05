import search_node
import math

__author__ = 'Andreas'


class Problem(object):
    def __init__(self, goal_state, initial_state, world):
        self.goal_state = goal_state
        self.initial_state = initial_state
        self.world = world

    def goal_test(self, state):
        if self.heuristic(state) == 0:
            return True
        else:
            return False

    def heuristic(self, state):
        distance = math.fabs(state[0] - self.goal_state[0]) + math.fabs(state[1] - self.goal_state[1])
        return distance

    def generate_children(self, node):
        children = []
        # North
        try:
            if not self.world[node.state[0]][node.state[1] - 1] == "#":
                state = [node.state[0], node.state[1] - 1]
                child = search_node.SearchNode(state, node.g + 1, self.heuristic(state), node)
                children.append(child)
        except IndexError:
            pass
        # East
        try:
            if not self.world[node.state[0] + 1][node.state[1]] == "#":
                state = [node.state[0] + 1, node.state[1]]
                child = search_node.SearchNode(state, node.g + 1, self.heuristic(state), node)
                children.append(child)
        except IndexError:
            pass
        # West
        try:
            if not self.world[node.state[0] - 1][node.state[1]] == "#":
                state = [node.state[0] - 1, node.state[1]]
                child = search_node.SearchNode(state, node.g + 1, self.heuristic(state), node)
                children.append(child)
        except IndexError:
            pass

        # South
        try:
            if not self.world[node.state[0]][node.state[1] + 1] == "#":

                state = [node.state[0], node.state[1] + 1]
                child = search_node.SearchNode(state, node.g + 1, self.heuristic(state), node)
                children.append(child)
        except IndexError:
            pass
        return children
