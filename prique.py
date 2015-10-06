import heapq

__author__ = 'Andreas'


class Frontier:
    def __init__(self):
        self.d = dict()
        self.h = []
        self.insert_count = 0

    def insert(self, node):
        """Insert node into dictionary and queue"""
        # Inserts the node into the dictionary
        self.d[node.state] = node
        # Inserts the node into the heap queue, ordered by the node.get_f value)
        heapq.heappush(self.h, node)

    def pop(self):
        """returns and removes the node with the lowest f-value"""
        # pops node from heap
        node = heapq.heappop(self.h)
        # removes value from dictionary as well
        return self.d.pop(node.state, None)

    def contains(self, node):
        """returns true if a node with the same state is contained in the dictionary"""
        return node.state in self.d

    def get(self, state):
        return self.d[state]
