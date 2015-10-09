import neuron
import sys

__author__ = 'Andreas'


# step 1: Initialize perceptron


inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
and_outputs = [0, 0, 0, 1]
or_outputs = [0, 1, 1, 1]


def neural_network(desired_outputs):
    perceptron = neuron.SimpleNeuron(2, (-0.5, 0.5), (-0.5, 0.5), 0.1)

    epoch = 1
    errors = 1
    while errors and epoch < 30:

        # step 2 and 3: activate and train
        errors = 0
        for p in range(len(inputs)):
            e = perceptron.activate(inputs[p], desired_outputs[p])
            if abs(e):
                errors += 1

        print("-------- After epoch {}: --------".format(epoch))
        print("errors: {}"
              " weight 1: {}"
              " weight 2: {} ".format(errors, round(perceptron.weights[0],4), round(perceptron.weights[1], 6)))
        epoch += 1

for c in range(10):
    print()
    print("Goal: AND - cycle: ", c+1)
    neural_network(and_outputs)

for c in range(10):
    print("Goal: OR - cycle: ", c+1)
    neural_network(or_outputs)

