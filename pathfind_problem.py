import search_node

__author__ = 'Andreas'


class Problem(object):
    def __init__(self, goal_state, initial_state, world, heuristic):
        self.goal_state = goal_state
        self.initial_state = initial_state
        self.world = world

        # If the heuristic parameter is true, a heuristic value is computed for nodes. If not, value is set to 0.
        if heuristic:
            self.heuristic_eval = lambda state: (
                abs(state[0] - self.goal_state[0]) + abs(state[1] - self.goal_state[1])
            )
        else:
            self.heuristic_eval = lambda node: (
                0
            )

        self.COST = {  # List of costs
                       "w": 100,  # Water
                       "m": 50,  # Mountains
                       "f": 10,  # Forests
                       "g": 5,  # Grasslands
                       "r": 1,  # Roads
                       ".": 1,
                       "A": 1,
                       "B": 1,
                       }

    def get_cost(self, pos_tuple):
        return self.COST[self.world[pos_tuple[0]][pos_tuple[1]]]

    def goal_test(self, state):
        return state == self.goal_state

    def generate_children(self, node):
        children = []
        # North
        if node.state[1] > 0:
            if not self.world[node.state[0]][node.state[1] - 1] == "#":
                state = (node.state[0], node.state[1] - 1)
                child = search_node.SearchNode(state, node.g + self.get_cost(state), self.heuristic_eval(state), node)
                children.append(child)

        # East
        if node.state[0] < len(self.world) - 1:
            if not self.world[node.state[0] + 1][node.state[1]] == "#":
                state = (node.state[0] + 1, node.state[1])
                child = search_node.SearchNode(state, node.g + self.get_cost(state), self.heuristic_eval(state), node)
                children.append(child)

        # West
        if node.state[0] > 0:
            if not self.world[node.state[0] - 1][node.state[1]] == "#":
                state = (node.state[0] - 1, node.state[1])
                child = search_node.SearchNode(state, node.g + self.get_cost(state), self.heuristic_eval(state), node)
                children.append(child)

        # South
        if node.state[1] < len(self.world[0]) - 1:
            if not self.world[node.state[0]][node.state[1] + 1] == "#":
                state = (node.state[0], node.state[1] + 1)
                child = search_node.SearchNode(state, node.g + self.get_cost(state), self.heuristic_eval(state), node)
                children.append(child)

        return children
