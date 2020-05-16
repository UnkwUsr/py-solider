class Pos:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    def left(self, count=1):
        self.x -= count
    def right(self, count=1):
        self.x += count
    def up(self, count=1):
        self.y -= count
    def down(self, count=1):
        self.y += count
