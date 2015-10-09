import random

__author__ = 'Andreas'


class SimpleNeuron(object):
    def __init__(self, input_length, weight_range):
        self.weights = self.generate_weights(input_length, weight_range)

    def generate_weights(self, length, weight_range):
        l = []
        for i in range(length):
            w = random.random() - weight_range
            l.append(w)
        return l

    def fire(self, inputs):
        pass
