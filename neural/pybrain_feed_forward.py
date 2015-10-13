from pybrain.tools.shortcuts import buildNetwork

__author__ = 'Andreas'

net = buildNetwork(2, 3, 1)
net.activate([2, 1])
