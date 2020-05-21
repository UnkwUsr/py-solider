from random import randint
from .Neuron import Neuron
from .InputNeuron import InputNeuron

class Network:
    def __init__(self, count_inputs, count_outputs):
        self.input_layer = [InputNeuron() for x in range(count_inputs)]
        self.output_layer = [Neuron() for x in range(count_outputs)]
        for n in self.output_layer:
            for input_n in self.input_layer:
                n.setInputWeight(input_n, 1)

    def process(self):
        output_values = []
        for n in self.output_layer:
            output_values.append(n.getValue())

        return output_values

    def train(self, what_decided, isGood):
        if not isGood:
            print("before train", self.process())
            neuron_with_bad_value = self.output_layer[what_decided]
            posible_bad_inputs_weights = neuron_with_bad_value.inputs_weights
            prev_res = self.process()[what_decided]
            for n in posible_bad_inputs_weights:
                prev_weight = posible_bad_inputs_weights[n]
                posible_bad_inputs_weights[n] /= 2
                new_res= self.process()[what_decided]
                if new_res >= prev_res:
                    posible_bad_inputs_weights[n] = prev_weight
            print("after train", self.process())


    def getSolution(self, input_data):
        self.setDataInputLayer(input_data)

        output_values = self.process()

        # has no possible solutions
        if max(output_values) == 0:
            print("No posible solutions. We are trapped?")
            return -1

        possible_solutions = []
        for i in range(len(output_values)):
            res = output_values[i]
            if res == max(output_values):
                possible_solutions.append(i)
        print("Posible solutions:", possible_solutions)

        solution = -1
        # has exactly one possible solution
        if len(possible_solutions) == 1:
            solution = possible_solutions[0]
        # has more than one possible solutions
        else:
            solution = possible_solutions[randint(0, len(possible_solutions) - 1)]

        return solution


    def setDataInputLayer(self, data):
        if len(data) != len(self.input_layer):
            print("ERROR", "Bad data for input layer")
        else:
            for i in range(len(data)):
                n = self.input_layer[i]
                n.setValue(data[i])


    def printNetwork(self):
        # TODO: print graph of network wital all neurons
        pass
