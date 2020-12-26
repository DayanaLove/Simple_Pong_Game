import turtle

window = turtle.Screen()
window.title("pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)
# Score
score_a = 0
score_b = 0

# paddle1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)  # makes the paddle longer
paddle1.penup()  # makes it so the turtle does not draw a line(?)
paddle1.goto(-350, 0)

# paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(+350, 0)  # Notice the +350, makes it so its on the right side on the screen

# Ball
ball = turtle.Turtle()
ball.speed(0)

ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # change in x cords, everytime the ball moves it moves by 2 pixels
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0) # Animation speed
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle1_up():
    y = paddle1.ycor()
    y += 20  # adds 20 pixels to the y cords
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 20  # adds 20 pixels to the y cords
    paddle2.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


# Keyboard Binding
window.listen()  # tells the program to listen for keyboard input
window.onkeypress(paddle1_up, "w")  # binds the key "w" to the function paddle1_up
window.onkeypress(paddle1_down, "s")  # binds the key "w" to the function paddle1_up
window.onkeypress(paddle2_up, "Up")  # binds the key "w" to the function paddle1_up
window.onkeypress(paddle2_down, "Down")  # binds the key "w" to the function paddle1_up

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:  # if ball's y cords is greater than 290
        ball.sety(290)
        ball.dy *= -1  # Reverse the direction of the ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:  # Right side
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),  align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #  paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() -50):    # Checks is the ball is on the right edge and if the ycord is greater than or less than the paddle
        ball.setx(340)
        ball.dx *= -1  # this bounces the ball or reveres the direction

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

