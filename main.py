
import pyxel
from Game.Game import Solider
from Game.Pos import Pos
from Bot.Bot import Bot


WIDTH=4
HEIGHT=4

pyxel.init(WIDTH, HEIGHT)

solider_game = Solider(WIDTH, HEIGHT)
bot = Bot(solider_game)

def update():
    if pyxel.btnp(pyxel.KEY_H):
        solider_game.move("left")
    if pyxel.btnp(pyxel.KEY_L):
        solider_game.move("right")
    if pyxel.btnp(pyxel.KEY_J):
        solider_game.move("down")
    if pyxel.btnp(pyxel.KEY_K):
        solider_game.move("up")

    if pyxel.btnp(pyxel.KEY_R):
        solider_game.restart()

    if pyxel.btnp(pyxel.KEY_V):
        print(bot.getVision())
    if pyxel.btnp(pyxel.KEY_B):
        bot.checkBot()

def draw():
    pyxel.cls(0)
    game_map = solider_game.getMap()
    for pos in game_map:
        pyxel.pset(pos.x, pos.y, game_map.get(pos).value)

    # for y in range(WIDTH):
        # for x in range(HEIGHT):
            # t = Pos(x, y)
            # pyxel.pset(x, y, game_map.get(t).value)

pyxel.run(update, draw)
