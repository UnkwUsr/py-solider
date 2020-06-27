import pyxel
from Game.Game import Solider
from Game.Pos import Pos
from Bot.Bot import Bot

# WARNING: map 5x5 has points, from that we CAN'T win
WIDTH=4
HEIGHT=4

FPS_RATE=30
pyxel.init(WIDTH, HEIGHT, fps=FPS_RATE)

solider_game = Solider(WIDTH, HEIGHT)
bot = Bot(solider_game)
auto_bot = False

def update():
    global auto_bot
    if pyxel.btnp(pyxel.KEY_A):
        solider_game.toggleSuppressMsgs()
        auto_bot = not auto_bot
    if auto_bot:
        bot.checkBot()

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
    if pyxel.btnp(pyxel.KEY_E):
        solider_game.replay()

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
