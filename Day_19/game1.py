from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwords():
    tim.forward(10)


def move_backwords():
    tim.backward(10)


def move_left():
    tim.setheading(tim.heading() + 10)


def move_right():
    tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwords, "w")
screen.onkey(move_backwords, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
