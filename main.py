import pyxel
from Game.Game import Solider
from Game.Blocks import Block
from Game.Pos import Pos, Sides
from Bot.Bot import Bot

# WARNING: map NxM has points, from that we CAN'T win
# (where N and M are odd)
WIDTH=4
HEIGHT=4

FPS_RATE=30
pyxel.init(WIDTH, HEIGHT, fps=FPS_RATE)

solider_game = Solider(WIDTH, HEIGHT)
bot = Bot(solider_game)
bot_auto_play = False

def update():
    global bot
    global bot_auto_play

    # a - toggle bot auto play
    if pyxel.btnp(pyxel.KEY_A):
        solider_game.toggleSuppressMsgs()
        bot_auto_play = not bot_auto_play
    if bot_auto_play:
        bot.bot_step()

    # h,j,k,l - control
    if pyxel.btnp(pyxel.KEY_H):
        solider_game.move(Sides.LEFT)
    if pyxel.btnp(pyxel.KEY_L):
        solider_game.move(Sides.RIGHT)
    if pyxel.btnp(pyxel.KEY_J):
        solider_game.move(Sides.DOWN)
    if pyxel.btnp(pyxel.KEY_K):
        solider_game.move(Sides.UP)

    # r - restart
    # e - replay
    if pyxel.btnp(pyxel.KEY_R):
        solider_game.restart()
    if pyxel.btnp(pyxel.KEY_E):
        solider_game.replay()

    # b - do one step by bot
    if pyxel.btnp(pyxel.KEY_B):
        bot.bot_step()

def draw():
    pyxel.cls(Block.EMPTY.value)
    game_map = solider_game.getMap()
    for pos in game_map:
        pyxel.pset(pos.x, pos.y, game_map.get_block(pos).value)

pyxel.run(update, draw)

