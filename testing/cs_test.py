from turtle import color
from cmu_graphics import *
app.stepsPerSecond = 60

player = Rect(200, 200, 50, 50)
player.vx = 5
player.vy = 5


def onKeyHold(keys):
    if ('d' in keys):
        player.centerX += player.vx
    
    if ('a' in keys):
        player.centerX -= player.vx

    if ('w' in keys):
        player.centerY -= player.vy

    if ('s' in keys):
        player.centerY += player.vy
cmu_graphics.run()
