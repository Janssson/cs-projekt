#IMPORT
from cmu_graphics import *


#BACKGROUND
app.background = 'lightgreen'


#FPS
app.stepsPerSecond = 5


#GRID
app.rows = 4
app.cols = 4
app.grid = makeList(app.rows, app.cols)


#DISTANCE
app.dist = 50


#PLAYER
snake = [Circle(175, 175, 25), Circle(175-app.dist, 175, 25),
        Circle(175-app.dist * 2, 175, 25)]

app.snakeOffscreen = False
app.snakeDx = 1
app.snakeDy = 0


#ROWS & COLS
for row in range(app.rows):
    for col in range(app.cols):
        posX = 0 + col * 100
        posX2 = 50 + col * 100
        posY = 0 + row * 100
        posY2 = 50 + row * 100
        gridColor = 'green'
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

    if (key == 'a'):
        if (app.snakeDx == 0):
            newSnakeSpeed(-1, 0)
    
    if (key == 's'):
        if (app.snakeDy == 0):
            newSnakeSpeed(0, 1)
    
    if (key == 'w'):
        if (app.snakeDy == 0):
            newSnakeSpeed(0, -1)


#FOOD
food = Group(Circle(25 + randrange(0, 8)*50, 25 + randrange(0, 8)*50, 20, fill='red'))
def foodSpawn():
    randcol = randrange(0, 8)
    randrow = randrange(0, 8)
    food.centerX = randcol
    food.centerY = randrow
    pass
foodSpawn()


# Goal = Star(200, 200, 20, 5, fill = "yellow")
# def GoalSpawn():
#     X = randrange(25,375)
#     Y = randrange(25,375)
#     Goal.centerX = X
#     Goal.centerY = Y
#     pass
# GoalSpawn()

#GAMEOVER
def gameOver():
    app.stop()


#MOVECIRCLE
def moveCircle(circle, dx, dy):
    circle.centerX += dx * app.dist
    circle.centerY += dy * app.dist


def onStep():
    if (snake[0].centerX > 400 or snake[0].centerX < 0 or snake[0].centerY > 400 or snake[0].centerY < 0):
        app.snakeOffscreen = True

    if (app.snakeOffscreen == True):
        gameOver()

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
        food.clear()
        snake.append(Circle(positions[i-1][0], positions[i-1][1], 25))


#HITSSNAKE
    if (snake[0].hitsShape(snake[i])):
        gameOver()





cmu_graphics.run()