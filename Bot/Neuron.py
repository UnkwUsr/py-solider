import numpy as np
from random import uniform as randfloat

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, inputs):
        self.w = randfloat(0, 1)
        self.inputs = inputs
        self.value = 0

    def updateW(new_w):
        self.w = new_w

    def activate(self):
        summ = sum([(x.value * self.w) for x in self.inputs])
        self.value = sigmoid(summ)

