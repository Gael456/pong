import turtle as t

playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title("Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# Left Paddle
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.goto(-350, 0)

# Right Paddle
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.goto(350, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.goto(0, 0)

# ScoreBoard
pen = t.Turtle()
pen.speed(0)
pen.color("blue")

pen.hideturtle()
pen.goto(0, 240)
pen.write("score", align="center", font=('Arial', 24, 'normal'))


# LeftPaddle Movement
def leftUp():
    y = leftPaddle.ycor()
    if y == 600:
        y = 600
        leftPaddle.sety(y)
    else:
        y = y + 90
        leftPaddle.sety(y)

def leftDown():
    y = leftPaddle.ycor()
    if y ==-600:
        y = -600
        leftPaddle.sety(y)
    else:
        y = y - 90
        leftPaddle.sety(y)


def rightUp():
    y = rightPaddle.ycor()
    if y > 600:
        y = 600
        rightPaddle.sety(y)
    else:
        y = y + 90
        rightPaddle.sety(y)


def rightDown():
    y = rightPaddle.ycor()
    if y < -600:
        y = -600
        rightPaddle.sety(y)
    else:
        y = y - 90
        rightPaddle.sety(y)

window.listen()
window.onkeypress(leftPaddleUp, 'w')
window.onkeypress(leftPaddledown, 'w')
window.onkeypress(rightPaddleUp, 'Up')
window.onkeypress(rightPaddleDown, 'Down')

while True:
    window.update()
    ball.setx(ball.xcor() + ballxDirection)
    ball.sety(ball.ycor() + ballyDirection)
