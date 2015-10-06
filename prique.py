import heapq
import queue

__author__ = 'Andreas'


class Frontier:
    def __init__(self):
        self.d = dict()
        self.h = []
        self.insert_count = 0

    def __contains__(self, node):
        """returns true if a node with the same state is contained in the dictionary"""
        return node.state in self.d

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

    def get(self, node):
        return self.d[node.state]


class BfsQueue:
    def __init__(self):
        self.h = []

    def __contains__(self, node):
        return node in self.h

    # def insert(self, node):
    #     """Insert node into queue"""
    #     self.q.append(node)

    def pop(self):
        """returns and removes the first element in the queue"""
        return self.h.pop(0)

    def get(self, node):
        for item in self.h:
            if item == node:
                return node
        return False

    def insert(self, node):
        self.h.append(node)
