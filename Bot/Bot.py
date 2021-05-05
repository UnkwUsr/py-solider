from random import randint
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
            print("Unreachable error. Wrong count of network outputs?", "move_id = ", move)
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

        # normalize vis
        vis_data = [vis[i] for i in vis]
        for i in range(len(vis_data)):
            if vis_data[i] > 1:
                vis_data[i] = 1

        return vis_data

    def bot_step(self):
        network_solution = self.get_solution_from_network()

        if network_solution == -1:
            return

        # there not exactly one solution. Starting trying each possible solution
        # if network_solution == -2:
        #     return

        move_result = self.doBotMove(network_solution)

        # is continuing playing
        if move_result == BotMoveResult.CONTINUE:
            self.is_obscure_moment = False

            pass
        # is win
        elif move_result == BotMoveResult.WIN:
            self.is_obscure_moment = False
            # we are win, so restore predefined_solution_id
            self.predefined_solution_id = -1

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


    def get_solution_from_network(self):
        vis_data = self.getVision()

        possible_solutions = self.network.getSolutions(vis_data)
        network_solution = -1
        # has exactly one possible solution

        if len(possible_solutions) == 0:
            # print("Bot say there no possible solutions. Restarting")

            # be careful! map 5x5 has start-positions from that win not possible
            self.stat['loses'] += 1
            self.printStats()

            print("TODO: there need to be some training stuff for no possible solutions")

            self.game.replay()
            return -1

        if len(possible_solutions) == 1:
            network_solution = possible_solutions[0]
        # has more than one possible solution
        else:
            # try each solution and find what is good
            # self.possible_solutions = possible_solutions
            # self.predefined_solution_id = 0

            # return -2

            return possible_solutions[randint(0, len(possible_solutions) - 1)]

        return network_solution


    def printStats(self):
        print("Wins: " + str(self.stat['wins']),
                "Loses: " + str(self.stat['loses']))

class BotMoveResult(Enum):
    DIED = 0
    WIN = 1
    CONTINUE = 2

