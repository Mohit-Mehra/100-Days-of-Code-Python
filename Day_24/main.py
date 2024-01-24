with open("Day_24/my_file.txt") as file:
    content = file.read()
    print(content)


with open("Day_24/new_file.txt", mode="w") as file:
    file.write("Hello")
