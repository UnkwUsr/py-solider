from random import randint
from Game.Pos import side_opposite, Sides
import os

class Bot:
    def __init__(self, game):
        self.game = game
        self.map = self.game.game_map

    def bot_step(self):
        if self.game.isWinned:
            self.game.restart()
            return

        sides = self.count_sides()
        sides = {side: num for side, num in sides.items() if num != 0}

        if not sides:
            print("unreachable (no sides to move to)")
            return

        side = self.find_best_side(sides)
        self.game.move(side)

    def find_best_side(self, sides):
        result = list(sides)[0]

        for side in sides:
            if sides[side] < sides[result]:
                result = side
                continue

            if sides[side] == sides[result]:
                if side_opposite(side) in sides:
                    result = side

        return result

    def count_sides(self):
        sides = dict()
        for side in Sides:
            sides[side] = 0

        for side in Sides:
            pos = self.game.pos.copy()
            pos.move(side)
            while not self.map.isSolid(pos):
                pos.move(side)
                sides[side] += 1

        return sides

