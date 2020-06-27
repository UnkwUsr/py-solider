from .Vision import Vision
from .Network import Network

class Bot:
    def __init__(self, game):
        self.stat = {'wins': 0, 'loses': 0, 'stucks': 0}

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
            # print("Bot say that no possible solutions. Restarting")

            # be careful! map 5x5 has start-positions from that win not possible
            self.stat['loses'] += 1
            self.printStats()

            # there need to be some training stuff

            self.game.replay()
            return

        move_result = self.doMoveNum(network_solution)

        # is continuing playing
        if move_result == 0:
            pass
            # self.network.train(network_solution, True)
        # is win
        elif move_result == 1:
            self.stat['wins'] += 1
            self.printStats()

            self.network.train(network_solution, True)
            self.game.restart()
        # is died
        elif move_result == -1:
            self.stat['loses'] += 1
            self.printStats()

            self.network.train(network_solution, False)
            self.game.replay()


    def printStats(self):
        print("Wins: " + str(self.stat['wins']),
                "Loses: " + str(self.stat['loses']))

