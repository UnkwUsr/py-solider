import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class InputNeuron:
    def __init__(self):
        self.value = 0

    def setValue(self, new_value):
        self.value = new_value

    def getValue(self):
        return self.value

