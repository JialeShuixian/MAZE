import play
import pygame
from random import randint

play.set_backdrop('light green')

score_txt = play.new_text(words='Score:', x=play.screen.right-100, y=play.screen.top-30, size=70)
score = play.new_text(words='0', x=play.screen.right-30, y=play.screen.top-30, size=70)

text = play.new_text(words='Tap SPACE to jump, LEFT/RIGHT to move', x=0, y=play.screen.bottom+60, size=70)

sea = play.new_box(
        color='blue', width=play.screen.width, height=50, x=0, y=play.screen.bottom+20
    )

def draw_platforms():
    pass

def draw_coins():

@play.when_program_starts
def start():

    draw_platforms()
    draw_coins()

@play.repeat_forever
async def game():
    await play.timer(seconds=1/48)

play.start_program()
