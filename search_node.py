__author__ = 'Andreas'


class SearchNode:
    def __init__(self, state, g, h, parent):
        self.state = state
        self.g = g
        self.h = h
        self.parent = parent

    def get_f(self):
        return self.g + self.h

    def replace_with(self, node):
        self.g = node.g
        self.h = node.h
        self.parent = node.parent
