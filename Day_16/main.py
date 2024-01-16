# import another_module
# print(another_module.variable)


# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan")
# timmy.forward(100)
# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

# print("| Pokemon Name | Type |")
# print("_______________________")
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Bulbasaur", "Charmander"])
table.add_column("Type", ["Electric", "Grass", "Fire"])

table.align = "l"

print(table)
