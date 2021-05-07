from enum import Enum


class MapPart(Enum):
    HORIZONTAL_RIGHT = 0
    RIGHT_UP = 1
    VERTICAL_UP = 2
    LEFT_UP = 3
    HORIZONTAL_LEFT = 4
    LEFT_DOWN = 5
    VERTICAL_DOWN = 6
    RIGHT_DOWN = 7
    PLAYER_POS = 8


class Vision:
    def __init__(self, game):
        self.game = game
        self.game_map = game.getMap()

    # we split all map to 4 parts related to current player position
    # and then add 4 horizontal and vertical lines related to current player position
    # (2 for horiz and 2 for vert)
    def getMapStateRelatedToCurrentPosition(self):
        parts_states = dict()
        for part in MapPart:
            parts_states[part] = []

        for pos in self.game_map:
            parts_states[self.determine_part(pos)].append(int(self.game_map.isSolid(pos)))

        # print(parts_states)

        map_state = []
        for part in MapPart:
            map_state.extend(parts_states[part])

        # print(map_state)

        return map_state

        # right_up_part = []
        # left_up_part = []
        # left_down_part = []
        # right_down_part = []

    def determine_part(self, pos):
        game_pos = self.game.pos

        if pos.y == game_pos.y and pos.x > game_pos.x:
            return MapPart.HORIZONTAL_RIGHT
        if pos.y == game_pos.y and pos.x < game_pos.x:
            return MapPart.HORIZONTAL_LEFT
        if pos.x == game_pos.x and pos.y > game_pos.y:
            return MapPart.VERTICAL_DOWN
        if pos.x == game_pos.x and pos.y < game_pos.y:
            return MapPart.VERTICAL_UP

        if pos.x > game_pos.x and pos.y < game_pos.y:
            return MapPart.RIGHT_UP
        if pos.x < game_pos.x and pos.y < game_pos.y:
            return MapPart.LEFT_UP
        if pos.x < game_pos.x and pos.y > game_pos.y:
            return MapPart.LEFT_DOWN
        if pos.x > game_pos.x and pos.y > game_pos.y:
            return MapPart.RIGHT_DOWN

        if pos.x == game_pos.x and pos.y == game_pos.y:
            return MapPart.PLAYER_POS

        print("unreachable in determine_part func in Vision.py")
        print("pos", pos, "\ngame_pos", game_pos)
        exit(1)

    def getAllMapState(self):
        map_vis = []
        for pos in self.game_map:
            map_vis.append(int(self.game_map.isSolid(pos)))

        return map_vis

