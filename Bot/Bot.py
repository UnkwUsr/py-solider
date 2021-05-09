from random import randint
from .Vision import Vision
from Game.Pos import side_opposite
import os

class Bot:
    def __init__(self, game):
        self.game = game
        self.map = self.game.game_map

        self.vision = Vision(self.game)

    def bot_step(self):
        if self.game.isWinned:
            self.game.restart()
            return

        self.vision.count_sides()
        sides = {x: y for x, y in self.vision.sides.items() if y != 0}

        if not sides:
            # print("Lose. (unreachable if all works correct)")
            return

        s = self.find_best_step(sides)

        self.game.move(s)

    def find_best_step(self, sides):
        r = list(sides)[0]

        for s in sides:
            if sides[s] < sides[r]:
                r = s
                continue

            if sides[s] == sides[r]:
                if side_opposite(s) in sides:
                    r = s

        return r

