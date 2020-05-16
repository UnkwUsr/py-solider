from .Layer import Layer

class Network:
    def __init__(self, input_layer, hidden_layers, output_layer):
        self.layers = []

        self.layers.append(input_layer)
        self.layers.extend(hidden_layers)
        self.layers.append(output_layer)

    def process(self):
        for l in self.layers[1:]:
            l.process()

    def setDataInputLayer(self, data):
        if len(data) != len(self.getInputLayer().getNeurons()):
            print("ERROR", "Bad data for input layer")
        else:
            for i in range(len(data)):
                n = self.getInputLayer().getNeurons()[i]
                n.value = data[i]
    def getDataOutputLayer(self):
        res = []
        for n in self.getOutputLayer().getNeurons():
            res.append(n.value)
        return res

    def getInputLayer(self):
        return self.layers[0]
    def getOutputLayer(self):
        return self.layers[-1]


    def printNetwork(self):
        for l in self.layers:
            print(l)
            for n in l.getNeurons():
                print("\t", n, "w =", n.w)
            print()

