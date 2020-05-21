from .Vision import Vision
from .Network import Network

class Bot:
    def __init__(self, game):
        self.game = game
        self.vision = Vision(game)

        self.network = Network(8, 4)

    def doMoveNum(self, move_num):
        move_name = ""
        if move_num == 0:
            move_name = "right"
        elif move_num == 1:
            move_name = "up"
        elif move_num == 2:
            move_name = "left"
        elif move_num == 3:
            move_name = "down"
        else:
            print("Error. Count of network outputs was changed?")
            return

        print("Doing move", move_name)
        self.game.move(move_name)
        if self.game.isDied:
            return -1
        elif self.game.isWinned:
            return 1
        # game continuing
        else:
            return 0


    def getVision(self):
        self.vision.update()
        vis = self.vision.getVision()
        return vis

    def checkBot(self):
        vis = self.getVision()
        vis_data = [vis[i] for i in vis]

        network_solution = self.network.getSolution(vis_data)
        if network_solution == -1:
            print("Nothing to do. Restarting")
            self.game.restart()
            return

        move_result = self.doMoveNum(network_solution)

        # is winned
        if move_result == 1:
            self.network.train(network_solution, True)
            self.game.restart()
        # is continuing playing
        elif move_result == 0:
            self.network.train(network_solution, True)
        # is died
        elif move_result == -1:
            self.network.train(network_solution, False)
            self.game.restart()

