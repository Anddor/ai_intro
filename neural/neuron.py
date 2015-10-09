import random

__author__ = 'Andreas'


def generate_weights(length, weight_range):
    l = []
    for i in range(length):
        w = random.uniform(weight_range[0], weight_range[1])
        l.append(w)
    return l


class SimpleNeuron(object):
    def __init__(self, input_length, weight_range, threshold_range, learning_rate):
        self.learning_rate = learning_rate
        self.weights = generate_weights(input_length, weight_range)
        self.threshold = random.uniform(threshold_range[0], threshold_range[1])

    def fire(self, inputs):
        weight_sum = 0
        for i in range(len(inputs)):
            weight_sum += inputs[i]*self.weights[i]
        if weight_sum > self.threshold:
            return 1
        else:
            return 0

    def activate(self, inputs, desired_output):
        output = self.fire(inputs)
        error = desired_output - output
        # weight training
        for i in range(len(self.weights)):
            self.weights[i] += self.learning_rate * inputs[i] * error
        return error
