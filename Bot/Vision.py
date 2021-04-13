from copy import deepcopy

class Vision:
    def __init__(self, game):
        self.game = game
        self.game_map = game.getMap()

        self.resetVision()

    def resetVision(self):
        # mnemonic for sides direction: unit circle
        self.vision = {"right": 0, "up": 0, "left": 0, "down": 0,
                "right_up": 0, "left_up": 0, "left_down": 0, "right_down": 0}

    def getVision(self):
        return self.vision

    def visionMove(self, pos, mov):
        mov(pos)
        if self.game_map.isSolid(pos):
            return False
        else:
            return True

    def update(self):
        """return list with distances to solid blocks for 8 directions"""

        self.resetVision()
        pos_view = self.game.pos

        pos = deepcopy(pos_view)
        mov = lambda p: p.right()
        while self.visionMove(pos, mov):
            self.vision["right"] += 1
        pos = deepcopy(pos_view)
        mov = lambda p: p.up()
        while self.visionMove(pos, mov):
            self.vision["up"] += 1
        pos = deepcopy(pos_view)
        mov = lambda p: p.left()
        while self.visionMove(pos, mov):
            self.vision["left"] += 1
        pos = deepcopy(pos_view)
        mov = lambda p: p.down()
        while self.visionMove(pos, mov):
            self.vision["down"] += 1

        pos = deepcopy(pos_view)
        mov = lambda p: ([p.right(), pos.up()])
        while self.visionMove(pos, mov):
            self.vision["right_up"] += 1
        pos = deepcopy(pos_view)
        mov = lambda p: ([p.left(), pos.up()])
        while self.visionMove(pos, mov):
            self.vision["left_up"] += 1
        pos = deepcopy(pos_view)
        mov = lambda p: ([p.left(), pos.down()])
        while self.visionMove(pos, mov):
            self.vision["left_down"] += 1
        pos = deepcopy(pos_view)
        mov = lambda p: ([p.right(), pos.down()])
        while self.visionMove(pos, mov):
            self.vision["right_down"] += 1

