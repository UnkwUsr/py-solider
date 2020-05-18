import numpy as np
from random import uniform as randfloat

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, inputs):
        self.ws = {x: randfloat(0, 1) for x in inputs}
        self.value = 0

    # def updateW(new_w):
        # self.w = new_w

    def activate(self):
        summ = sum([(n.value * self.ws[n]) for n in self.ws])
        self.value = sigmoid(summ)

