from random import randint
from copy import deepcopy
from .Pos import Pos
from .Map import Map
from .Blocks import Block

TEXT_YOU_DIED = "You died. Restart (key r) or replay (key e)"
TEXT_YOU_WINNED = "You winned. Restart (key r) or replay (key e)"

class Solider:
    """Main game class"""

    def __init__(self, map_width, map_height):
        self.suppress_msg = False

        self.game_map = Map(map_width, map_height)

        self.restart()

    def restart(self):
        self.isDied = False
        self.isWinned = False
        self.game_map.reset()
        # save start pos for ability to 'replay'
        self.start_pos = Pos(randint(0, self.game_map.width - 1), randint(0, self.game_map.height - 1))
        self.pos = self.start_pos
        self.syncPlayer(init=True)

    # as restart, but do not change start position
    def replay(self):
        self.isDied = False
        self.isWinned = False
        self.game_map.reset()
        self.pos = self.start_pos
        self.syncPlayer(init=True)

    def move(self, direction):
        if self.isDied:
            self.printMsg(TEXT_YOU_DIED)
            return
        elif self.isWinned:
            self.printMsg(TEXT_YOU_WINNED)
            return

        new_pos = deepcopy(self.pos)
        new_pos.move(direction)

        if self.game_map.isSolid(new_pos):
            self.printMsg(TEXT_YOU_DIED)
            self.isDied = True
            self.game_map.set_block(self.pos, Block.DIED)
        else:
            self.pos = deepcopy(new_pos)
            self.syncPlayer()

            if self.checkWin():
                self.printMsg(TEXT_YOU_WINNED)
                self.isWinned = True
                self.game_map.set_block(self.pos, Block.WINNER)


    def syncPlayer(self, init=False):
        if init:
            self.game_map.set_block(self.pos, Block.START)
        else:
            self.game_map.set_block(self.pos, Block.PLAYER)
            if self.game_map.get_block(self.pos_prev) != Block.START:
                self.game_map.set_block(self.pos_prev, Block.DRAWED)

        self.pos_prev = deepcopy(self.pos)

    def checkWin(self):
        count_drawed = 0
        for p in self.game_map:
            if self.game_map.get_block(p) != Block.EMPTY:
                count_drawed += 1
        if count_drawed >= self.game_map.width * self.game_map.height:
            return True
        else:
            return False

    def getMap(self):
        return self.game_map


    def toggleSuppressMsgs(self):
        self.suppress_msg = not self.suppress_msg

    def printMsg(self, msg):
        if not self.suppress_msg:
            print(msg)

