import os
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
leftPaddle.penup()
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.goto(-350, 0)

# Right Paddle
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.penup()
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.goto(350, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ballxDirection = 0.2
ballyDirection = 0.2

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
    if y > 200 or y == 200:
        y = 230
        leftPaddle.sety(y)
    else:

        y = y + 90
        leftPaddle.sety(y)



def leftDown():
    y = leftPaddle.ycor()
    if y < -600:
        y = -600
        leftPaddle.sety(y)
    else:
        y = y - 90
        leftPaddle.sety(y)


def rightUp():
    y = rightPaddle.ycor()
    y = y + 90
    rightPaddle.sety(y)

def rightDown():
    y = rightPaddle.ycor()
    y = y - 90
    rightPaddle.sety(y)


window.listen()
window.onkeypress(leftUp, 'w')
window.onkeypress(leftDown, 's')
window.onkeypress(rightUp, 'Up')
window.onkeypress(rightDown, 'Down')

while True:
    window.update()
    ball.setx(ball.xcor() + ballxDirection)
    ball.sety(ball.ycor() + ballyDirection)

    if ball.ycor() > 290:
        ball.sety(290)
        ballyDirection = -ballyDirection

    if ball.ycor() < -290:
        ball.sety(-290)
        ballyDirection = -ballyDirection

    if ball.xcor() > 390:
        ball.goto(0, 0)
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("Player A: {}                   Player B: {}".format(playerAscore, playerBscore),
                  align="center", font=('Monaco', 24, 'normal'))
        os.system("afplay wallhit.wav&")

    if (ball.xcor()) < -390:  # Left width paddle Border
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Player A: {}                   Player B: {} ".format(playerAscore, playerBscore),
                  align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

        # Paddle Collisions
        if (ball.xcor() > 340) and (ball.xcor() < 350) and (
                rightPaddle.ycor() + 40 > ball.ycor() > rightPaddle.ycor() - 40):
            ball.setx(340)
            ball_dx = ball_dx * - 1
            os.system("afplay paddle.wav&")

        if (ball.xcor() < -340) and (ball.xcor() > -350) and (
                leftPaddle.ycor() + 40 > ball.ycor() > leftPaddle.ycor() - 40):
            ball.setx(-340)
            ball_dx = ball_dx * - 1
            os.system("afplay paddle.wav&")
