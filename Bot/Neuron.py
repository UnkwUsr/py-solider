import numpy as np
from random import uniform as randfloat

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def my_activator(x):
    if x >= 1:
        return x
    else:
        return 0

class Neuron:
    def __init__(self):
        self.inputs_weights = {}
        self.value = 0

    def getListWeights(self):
        return self.ws
    def setInputWeight(self, input_neuron, weight):
        """ Can add new inputs and modify weight exsisting input"""
        self.inputs_weights[input_neuron] = weight

    def getValue(self):
        summ = sum([(n.getValue() * self.inputs_weights[n]) for n in self.inputs_weights])
        # result = my_activator(summ)
        result = summ
        return result

