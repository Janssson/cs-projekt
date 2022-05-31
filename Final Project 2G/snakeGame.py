#IMPORT
from trace import Trace
from cmu_graphics import *


#BACKGROUND
app.background = rgb(197, 245, 86)


#FPS
app.stepsPerSecond = 5


#GRID
app.rows = 4
app.cols = 4
app.grid = makeList(app.rows, app.cols)


#DISTANCE
app.dist = 50


#PLAYER
color = gradient('blue', 'darkblue', start='right')
snakeHead = Group(Circle(175, 175, 25, fill=color))
snake = [snakeHead, Circle(175-app.dist, 175, 25, fill=color),
        Circle(175-app.dist * 2, 175, 25, fill=color)]
snakeEyes1 = Group(Circle(175, 165, 5), Circle(175, 185, 5))
snakeEyes2 = Group(Circle(165, 175, 5), Circle(185, 175, 5))
snakeHead.add(snakeEyes1)
snakeHead.add(snakeEyes2)

#app.snakeOffscreen = False
app.snakeDx = 1
app.snakeDy = 0


#ROWS & COLS
for row in range(app.rows):
    for col in range(app.cols):
        posX = 0 + col * 100
        posX2 = 50 + col * 100
        posY = 0 + row * 100
        posY2 = 50 + row * 100
        gridColor = rgb(189, 235, 82)
        app.grid[row][col] = Group(Rect(posX, posY, 50, 50, fill=gridColor), Rect(posX2, posY2, 50, 50, fill=gridColor))


#NEWSPEED
def newSnakeSpeed(newDx, newDy):
    app.snakeDx = newDx
    app.snakeDy = newDy


#MOVEMENT
def onKeyPress(key):
    if (key == 'd'):
        if (app.snakeDx == 0):
            newSnakeSpeed(1, 0)
            #snakeEyes2.visible = False


    elif (key == 'a'):
        if (app.snakeDx == 0):
            newSnakeSpeed(-1, 0)
            #snakeEyes2.visible = False

    elif (key == 's'):
        if (app.snakeDy == 0):
            newSnakeSpeed(0, 1)
            #snakeEyes1.visible = False
    
    elif (key == 'w'):
        if (app.snakeDy == 0):
            newSnakeSpeed(0, -1)
            #snakeEyes1.visible = False


#FOOD
food = Group(Circle(25 + randrange(0, 8)*50, 25 + randrange(0, 8)*50, 20, fill='red'))
def foodSpawn():
    randcol = 25+randrange(0, 8)*50
    randrow = 25+randrange(0, 8)*50
    food.centerX = randcol
    food.centerY = randrow
foodSpawn()


#GAMEOVER
def gameOver():
    count.value = 0
    Rect(25, 25, 350, 350, fill=rgb(221, 222, 220))


#MOVECIRCLE
def moveCircle(circle, dx, dy):
    circle.centerX += dx * app.dist
    circle.centerY += dy * app.dist

#FOODCOUNT
count = Label(0, 375, 25, fill='white', size=40)


def onStep():
    # if (snake[0].centerX > 400 or snake[0].centerX < 0 or snake[0].centerY > 400 or snake[0].centerY < 0):
    #     app.snakeOffscreen = True

    # if (app.snakeOffscreen == True):
    #     gameOver()

    if (snake[0].centerX > 400):
        snake[0].centerX = -150
    
    elif (snake[0].centerX < 0):
        snake[0].centerX = 550

    positions = []

    for circle in snake:
        positions.append((circle.centerX, circle.centerY))

    for i in range(len(positions)):
        if (i == 0):
            moveCircle(snake[0], app.snakeDx, app.snakeDy)
        else:
            snake[i].centerX = positions[i-1][0]
            snake[i].centerY = positions[i-1][1]

        snake[i].toFront()


#HITSFOOD
    if (snake[0].hitsShape(food)):
        snake.append(Circle(positions[i-1][0], positions[i-1][1], 25, fill=color))
        foodSpawn()
        count.value += 1


#HITSSNAKE
    if (snake[0].hitsShape(snake[i])):
        gameOver()





cmu_graphics.run()