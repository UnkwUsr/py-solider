from Game.Pos import Sides

class Vision:
    def __init__(self, game):
        self.game = game
        self.map = game.getMap()

        self.sides = dict()

    def count_sides(self):
        for s in Sides:
            self.sides[s] = 0

        for s in Sides:
            pos = self.game.pos.copy()
            pos.move(s)
            while not self.map.isSolid(pos):
                pos.move(s)
                self.sides[s] += 1

