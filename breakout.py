import turtle
import random

screen = turtle.Screen()
screen.setup(width=800, height=400)
screen.bgcolor("black")
screen.title("Atari Breakout!")
screen.tracer(0)

rectangle = ((-50, -10), (-50, 10), (50, 10), (50, -10))
turtle.register_shape("rectangle", rectangle)

slider = turtle.Turtle()
slider.shape("rectangle")
slider.setheading(90)
slider.penup()
slider.color("white")
slider.goto(0, -175)

def move_left():
    x = slider.xcor() - 30
    if x > -350:
        slider.setx(x)

def move_right():
    x = slider.xcor() + 30
    if x < 350:
        slider.setx(x)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

def rects():
    r1 = ((-30, -10), (-30, 10), (30, 10), (30, -10))
    r2 = ((-40, -10), (-40, 10), (40, 10), (40, -10))
    r3 = ((-50, -10), (-50, 10), (50, 10), (50, -10))

    turtle.register_shape("r1", r1)
    turtle.register_shape("r2", r2)
    turtle.register_shape("r3", r3)

    blocks = []

    for i in range(12):
        block = turtle.Turtle()
        block.shape("r1")
        block.setheading(90)
        block.penup()
        block.color("red")
        block.goto(-355 + i * 70, 175)
        blocks.append(block)

    for i in range(9):
        block = turtle.Turtle()
        block.shape("r2")
        block.setheading(90)
        block.penup()
        block.color("blue")
        block.goto(-370 + i * 90, 150)
        blocks.append(block)
    for i in range(8):
        block = turtle.Turtle()
        block.shape("r3")
        block.setheading(90)
        block.penup()
        block.color("green")
        block.goto(-340 + i * 110, 120)
        blocks.append(block)

    return blocks

b = turtle.Turtle()
b.shape("circle")
b.penup()
b.color("white")
b.goto(0, 0)
b.speed(0)
b.setheading(random.randint(135, 225))

blocks = rects()

game_over = False
ball_moving = False

def move_ball():
    global game_over, ball_moving

    if game_over or not ball_moving:
        return

    b.forward(2)
    if b.xcor() > 390 or b.xcor() < -390:
        b.setheading(180 - b.heading())

    if b.ycor() > 190:
        b.setheading(360 - b.heading())

    if b.distance(slider) < 55 and b.ycor() > -160:
        angle = random.randint(-30, 30)
        b.setheading(360 - b.heading() + angle)

    for block in blocks:
        if block.isvisible() and b.distance(block) < 35:
            block.hideturtle()
            blocks.remove(block)
            b.setheading(360 - b.heading())
            break

    if b.ycor() < -190:
        game_over = True
        display_game_over()
        return  

    if not blocks:
        display_win()
        return  

    screen.update()

    if not game_over:  
        screen.ontimer(move_ball, 10)

def start_ball():
    space()
    global ball_moving
    ball_moving = True
    text.clear()
    move_ball()

def display_game_over():
    game_over_text = turtle.Turtle()
    game_over_text.hideturtle()
    game_over_text.color("red")
    game_over_text.penup()
    game_over_text.goto(0, 0)
    game_over_text.write("GAME OVER!", align="center", font=("Arial", 24, "bold"))
    screen.ontimer(screen.bye, 2000)  


def display_win():
    win_text = turtle.Turtle()
    win_text.hideturtle()
    win_text.color("yellow")
    win_text.penup()
    win_text.goto(0, 0)
    win_text.write("YOU WIN!", align="center", font=("Arial", 24, "bold"))
    global game_over
    game_over = True

text = turtle.Turtle()
def display_text():
    text.hideturtle()
    text.color("white")
    text.penup()
    text.goto(0,30)
    text.write("PRESS SPACE TO START!", align="center", font=("Arial", 24, "bold"))

def space():
    tex = turtle.Turtle()
    tex.hideturtle()
    tex.color("white")
    tex.penup()
    tex.goto(-300,30)
    tex.write("Use Space Bar to \n increase speed", align="center", font=("Arial", 14, "normal"))

display_text()


screen.onkeypress(start_ball, "space")
screen.update()
screen.mainloop()
