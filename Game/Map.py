from .Blocks import Block
from .Pos import Pos


class Map:
    def __init__(self, init_width, init_height):
        self.width = init_width
        self.height = init_height

        #set borders
        # for y in range(self.height):
            # self.map[y][0] = Block.BORDER
            # self.map[y][self.width - 1] = Block.BORDER
        # for x in range(self.width):
            # self.map[0][x] = Block.BORDER
            # self.map[self.height - 1][x] = Block.BORDER

    def __iter__(self):
        return MapIterator(self)

    def reset(self):
        self.map = [[Block.EMPTY for x in range(self.width)] for y in range(self.height)]

    def set(self, pos, block):
        self.map[pos.y][pos.x] = block

    def get(self, pos):
        return self.map[pos.y][pos.x]

    def isSolid(self, pos):
        if (pos.x < 0 or pos.x > self.width - 1 or
                pos.y < 0 or pos.y > self.height - 1 or
                self.get(pos) != Block.EMPTY):
            return True
        else:
            return False

class MapIterator:
    def __init__(self, game_map):
        self.map = game_map

        self.x = 0
        self.y = 0

    def __next__(self):
        if self.y < self.map.height:
            pos = Pos(self.x, self.y)
            if self.x < self.map.width - 1:
                self.x += 1
            else:
                self.y += 1
                self.x = 0

            return pos

        raise StopIteration
