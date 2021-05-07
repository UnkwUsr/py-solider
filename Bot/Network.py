from .Neuron import Neuron
from .InputNeuron import InputNeuron

class Network:
    def __init__(self, count_inputs, count_outputs):
        self.input_layer = [InputNeuron() for x in range(count_inputs)]

        self.hidden_layer = [Neuron() for x in range(16)]
        for n in self.hidden_layer:
            for input_n in self.input_layer:
                n.setInputWeight(input_n, 1)

        self.output_layer = [Neuron() for x in range(count_outputs)]
        for n in self.output_layer:
            for input_n in self.hidden_layer:
                n.setInputWeight(input_n, 1)

        self.printNetwork()

    def process(self):
        output_values = []
        for n in self.output_layer:
            output_values.append(n.getValue())

        return output_values

    def train_on_error(self, what_decided):
        orig_res = self.process()
        print("[Before train]", orig_res)

        for neuron in self.hidden_layer:
            for input_neuron in neuron.inputs_weights:
                original_weight = neuron.inputs_weights[input_neuron]
                neuron.inputs_weights[input_neuron] /= 2

                new_res = self.process()
                if new_res[what_decided] >= orig_res[what_decided]:
                    # revert because we need decrease output for errorneus answer
                    neuron.inputs_weights[input_neuron] = original_weight

        # neuron_with_bad_value = self.output_layer[what_decided]
        # possible_bad_inputs_weights = neuron_with_bad_value.inputs_weights
        # prev_res = self.process()[what_decided]

        # neurons_to_modify = []

        # # find who need modify
        # for n in possible_bad_inputs_weights:
        #     prev_weight = possible_bad_inputs_weights[n]
        #     possible_bad_inputs_weights[n] /= 1.1
        #     new_res= self.process()[what_decided]
        #     if new_res < prev_res:
        #         neurons_to_modify.append({"n": n, "val": possible_bad_inputs_weights[n]})

        #     # revert
        #     possible_bad_inputs_weights[n] = prev_weight

        # apply modifies to neurons
        # for a in neurons_to_modify:
        #     possible_bad_inputs_weights[a["n"]] = a["val"]

        print("[After train]", self.process())

        # normalize weights (due to float has not unlimited precision)
        # mx = possible_bad_inputs_weights[max(possible_bad_inputs_weights, key=possible_bad_inputs_weights.get)]
        # print("Mx:", mx)
        # for n in possible_bad_inputs_weights:
        #     print(possible_bad_inputs_weights[n])
        #     possible_bad_inputs_weights[n] /= mx

        self.printNetwork()


    def getSolutions(self, input_data):
        self.setDataInputLayer(input_data)

        output_values = self.process()

        # has no possible solutions
        if max(output_values) == 0:
            return []

        possible_solutions = []
        for i in range(len(output_values)):
            res = output_values[i]
            if res == max(output_values):
                possible_solutions.append(i)


        return possible_solutions


    def setDataInputLayer(self, data):
        if len(data) != len(self.input_layer):
            print("ERROR", "Bad data for input layer")
        else:
            for i in range(len(data)):
                n = self.input_layer[i]
                n.setValue(data[i])


    # use with `watch cat net.status`
    def printNetwork(self):
        with open("net.status", 'w') as net_file:
            net_file.write("")

            for out in self.output_layer:
                net_file.write(makeUniqStr(out) + "\n")
                for inp in out.inputs_weights:
                    net_file.write("\t" + makeUniqStr(inp) + " weight: " + str(out.inputs_weights[inp]) + "\n")


def makeUniqStr(a):
    return str(id(a))

