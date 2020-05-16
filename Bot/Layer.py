from .Neuron import Neuron

class Layer:
    def __init__(self, count_neurons, inputs):
        self.neurons = [Neuron(inputs) for x in range(count_neurons)]

    def process(self):
        for n in self.getNeurons():
            n.activate()

    def getNeurons(self):
        return self.neurons

