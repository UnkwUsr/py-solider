from enum import Enum

class Block(Enum):
    EMPTY = 0

    PLAYER = 1
    WINNER = 6
    DIED = 8

    BORDER = 3
    START = 4
    DRAWED = 5

