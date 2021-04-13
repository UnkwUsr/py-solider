from .Vision import Vision
from .Network import Network
from enum import Enum

class Bot:
    def __init__(self, game):
        self.stat = {'wins': 0, 'loses': 0}

        self.game = game
        self.vision = Vision(game)

        self.network = Network(8, 4)

    def doBotMove(self, move):
        move_name = ""
        if move == 0:
            move_name = "right"
        elif move == 1:
            move_name = "up"
        elif move == 2:
            move_name = "left"
        elif move == 3:
            move_name = "down"
        else:
            print("Unreachable error. Wrong count of network outputs?")
            return

        self.game.move(move_name)
        if self.game.isDied:
            return BotMoveResult.DIED
        elif self.game.isWinned:
            return BotMoveResult.WIN
        # game continuing
        else:
            return BotMoveResult.CONTINUE


    def getVision(self):
        self.vision.update()
        vis = self.vision.getVision()
        return vis

    def bot_step(self):
        vis = self.getVision()
        vis_data = [vis[i] for i in vis]
        # TODO: remove normalizing because is less efficient
        # normalize vis
        for i in range(len(vis_data)):
            if vis_data[i] > 1:
                vis_data[i] = 1

        network_solution = self.network.getSolution(vis_data)
        if network_solution == -1:
            # print("Bot say there no possible solutions. Restarting")

            # be careful! map 5x5 has start-positions from that win not possible
            self.stat['loses'] += 1
            self.printStats()

            print("TODO: there need to be some training stuff")

            self.game.replay()
        else:
            move_result = self.doBotMove(network_solution)

            # is continuing playing
            if move_result == BotMoveResult.CONTINUE:
                pass
            # is win
            elif move_result == BotMoveResult.WIN:
                self.stat['wins'] += 1
                self.printStats()

                self.network.train(network_solution, True)
                self.game.restart()
            # is died
            elif move_result == BotMoveResult.DIED:
                self.stat['loses'] += 1
                self.printStats()

                self.network.train(network_solution, False)
                self.game.replay()


    def printStats(self):
        print("Wins: " + str(self.stat['wins']),
                "Loses: " + str(self.stat['loses']))

class BotMoveResult(Enum):
    DIED = 0
    WIN = 1
    CONTINUE = 2

