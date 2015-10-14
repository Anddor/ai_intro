from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

__author__ = 'Andreas'

# 1

ds = SupervisedDataSet(1,1)
for i in range(1, 9):
    ds.addSample(i, i)

for nodes in range(8, 0, -1):

    print("----------- Nodes: ", nodes, " -------------")

    net = buildNetwork(1, nodes, 1, hiddenclass=TanhLayer)

    trainer = BackpropTrainer(net, ds)

    trainer.trainUntilConvergence(verbose=False, validationProportion=0.15, maxEpochs=1000, continueEpochs=10)

    print("heltall: 10")
    print(net.activate([10]))

    print("heltall: 1")
    print(net.activate([1]))

    print("heltall: 2")
    print(net.activate([2]))

    print("heltall: 3")
    print(net.activate([3]))

    print("heltall: 4")
    print(net.activate([4]))

    print("heltall: 5")
    print(net.activate([5]))

    print("heltall: 6")
    print(net.activate([6]))

    print("heltall: 7")
    print(net.activate([7]))

    print("heltall: 8")
    print(net.activate([8]))