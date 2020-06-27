"""
Game Solider
Controls:
hjkl - move
r - restart
"""
from random import randint
from copy import deepcopy
from .Pos import Pos
from .Map import Map
from .Blocks import Block

TEXT_YOU_DIED = "You died. Restart (default key r) for continue"
TEXT_YOU_WINNED = "You winned. Please restart (default key r) for continue"

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
        #with borders
        # self.pos = Pos(randint(1, map_width - 2), randint(1, map_height - 2))
        self.pos = Pos(randint(0, self.game_map.width - 1), randint(0, self.game_map.height - 1))
        self.syncPlayer(init=True)


    def move(self, direction):
        if self.isDied:
            self.printMsg(TEXT_YOU_DIED)
            return
        elif self.isWinned:
            self.printMsg(TEXT_YOU_WINNED)
            return

        new_pos = deepcopy(self.pos)
        if direction == "left":
            new_pos.left()
        if direction == "right":
            new_pos.right()
        if direction == "down":
            new_pos.down()
        if direction == "up":
            new_pos.up()

        if self.game_map.isSolid(new_pos):
            self.printMsg(TEXT_YOU_DIED)
            self.isDied = True
        else:
            self.pos = deepcopy(new_pos)
            self.syncPlayer()

            if self.checkWin():
                self.printMsg(TEXT_YOU_WINNED)
                self.isWinned = True


    def syncPlayer(self, init=False):
        if init:
            self.game_map.set(self.pos, Block.START)
        else:
            self.game_map.set(self.pos, Block.PLAYER)
            if self.game_map.get(self.pos_prev) != Block.START:
                self.game_map.set(self.pos_prev, Block.DRAWED)

        self.pos_prev = deepcopy(self.pos)

    def checkWin(self):
        count_drawed = 0
        for p in self.game_map:
            if self.game_map.get(p) != Block.EMPTY:
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
