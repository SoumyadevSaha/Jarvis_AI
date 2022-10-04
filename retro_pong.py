import turtle

canvas = turtle.Screen()
canvas.title("Retro Pong by Jarvis")
canvas.bgcolor("black")
canvas.setup(width = 800, height = 600)
canvas.tracer(0)

f = 50
str1 = "Score : 0"
k = 0
scr = 0

# Paddle ->
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_len=5, stretch_wid=1)
paddle.color("white")
paddle.penup()
paddle.goto(0, -250)

# Ball ->
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.3
ball.dy = 0.3

# Game Functions

def paddle_right():
    x = paddle.xcor()
    x += f
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= f
    paddle.setx(x)

def listen():
    canvas.listen()
    canvas.onkeypress(paddle_left,"Left")
    canvas.onkeypress(paddle_right,"Right")

def listengmovr() :
    canvas.update()
    canvas.onkeypress(None, "Right")
    canvas.onkeypress(None, "Left")
    canvas.onkeypress(main, "space")

text = turtle.Turtle()
text.speed(0)
text.penup()
text.hideturtle()
text.color("white")
text.goto(0, 260)
text.write(str1, move=False, font=('monaco', 20, 'bold'), align='center')

def main2() :
    global scr
    ball.goto(0, 0)
    paddle.goto(0, -250)
    str1 = "         GAME OVER !!\n          SCORE : " + str(scr) + "\nPress Space-Bar to Play again."
    text.clear()
    text.goto(0, 200)
    text.write(str1, move=False, font=('monaco', 20, 'bold'), align='center')
    scr = 0
    ball.dx = 0.3
    ball.dy = 0.3
    while k == -1 :
        listengmovr()

def main():
    global k
    k = 0
    global str1
    global scr
    str1 = "SCORE : " + str(scr)
    text.clear()
    text.goto(0, 260)
    text.write(str1, move=False, font=('monaco', 20, 'bold'), align='center')
    while True :
        canvas.update()
        if (k != -1):
            listen()
        else:
            break
        
        # Moving the ball ->
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border Checking ->
        if ball.ycor() > 290 :
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290 :
            k = -1

        if ball.xcor() > 390 :
            ball.setx(390)
            ball.dx *= -1

        if ball.xcor() < -390 :
            ball.setx(-390)
            ball.dx *= -1

        # On hitting the paddle ->
        if (ball.ycor() <= -230 and ball.ycor() > -240) :
            if (ball.xcor() <= paddle.xcor() + 50 and ball.xcor() >= paddle.xcor() - 50):
                scr += 1
                ball.dy *= -1
                str1 = "SCORE : " + str(scr)
                text.clear()
                text.write(str1, move=False, font=('monaco', 20, 'bold'), align='center')
    main2()

main()
