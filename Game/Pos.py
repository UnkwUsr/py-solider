from enum import Enum

class Sides(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3

class Pos:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    def move(self, direction, count=1):
        if direction == Sides.RIGHT:
            self.x += count
            return
        if direction == Sides.UP:
            self.y -= count
            return
        if direction == Sides.LEFT:
            self.x -= count
            return
        if direction == Sides.DOWN:
            self.y += count
            return

        print("unreachable in func move() in Pos.py", direction)
        exit(1)

    def copy(self):
        return Pos(self.x, self.y)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

def side_opposite(side):
    r = side.value + 2
    r %= 4

    return Sides(r)

