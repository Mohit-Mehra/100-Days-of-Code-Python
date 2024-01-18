# from turtle import Turtle, Screen
import random

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("cyan")
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)


# tim = Turtle()
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# tim = Turtle()

# colors = [
#     "red",
#     "brown",
#     "forest green",
#     "medium violet red",
#     "dark red",
#     "navy",
#     "light slate gray",
#     "green yellow",
#     "dark slate blue",
#     "dark magenta",
# ]


# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.left(angle)


# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))


# screen = Screen()
# screen.exitonclick()
