from enum import Enum

class Block(Enum):
    EMPTY = 7

    PLAYER = 5
    WINNER = 1
    DIED = 8

    BORDER = 3
    START = 4
    DRAWED = 0

