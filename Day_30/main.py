# Erorrs

# with open("a_file.txt") as file:
#     file.read()

# Key Error
# IndexError
# TypeError


# try:
#     file = open("a.txt")
#     a = {"key": "value"}
#     print(a["assa"])
# except FileNotFoundError:
#     file = open("Day_30/a.txt", "w")
#     file.write("Something")
# except KeyError as error:
#     print(f"The Key {error} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("Thsi is an error that I made up.")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3m")

bmi = weight / height**2
print(bmi)
