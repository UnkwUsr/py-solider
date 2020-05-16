from .Vision import Vision
from .Network import Network
from .Layer import Layer

class Bot:
    def __init__(self, game):
        self.game = game
        self.vision = Vision(game)

        input_layer = Layer(8, [])
        hidden_layers = [Layer(64, input_layer.getNeurons())]
        # prev_layer = self.input_layer
        # self.hidden_layers = []
        # for x in hidden_layers_neuron_counts:
            # new_layer = Layer(x, prev_layer.getNeurons())
            # self.hidden_layers.append(new_layer)
            # prev_layer = new_layer
        output_layer = Layer(4, hidden_layers[-1].getNeurons())
        self.network = Network(input_layer, hidden_layers, output_layer)

    def getVision(self):
        self.vision.update()
        vis = self.vision.getVision()
        return vis

    def checkBot(self):
        # print(self.network.printNetwork())

        vis = self.getVision()
        vis_data = [vis[i] for i in vis]

        self.network.setDataInputLayer(vis_data)

        self.network.process()

        for x in self.network.getOutputLayer().getNeurons():
            print(x.value)

        print()
