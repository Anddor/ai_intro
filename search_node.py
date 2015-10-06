__author__ = 'Andreas'


class SearchNode:
    def __init__(self, state, g, h, parent):
        self.state = state
        self.g = g
        self.h = h
        self.parent = parent

    def __lt__(self, other):
        """Makes comparisons and sorting operate on the f and h values."""
        if self.get_f() == other.get_f():
            return self.h < other.h
        else:
            return self.get_f() < other.get_f()

    def __eq__(self, other):
        return self.state == other.state

    def get_f(self):
        """generates and returns the total cost of the node"""
        return self.g + self.h

    def replace_with(self, node):
        """For switching two nodes with same state and different cost."""
        self.g = node.g
        self.h = node.h
        self.parent = node.parent
