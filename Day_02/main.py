# Data Types

# Strings - "Hello"

print("Hello"[4])  # Slicing

print("123" + "456")

# Integer

print(123 + 456)

print(123_456_789)

# Float

print(3.14159)

# Boolean

True
False

# num_char = len(input("What is your name?"))
# new = str(num_char)
# print("Your name has " + new + " characters.")


a = str(123)
print(type(a))


print(70 + float("100.5"))

print(str(70) + str(100.5))


3 + 5
3 - 5
5 * 5
print(10 / 2)  # output is float
print(5**2)  # Power

# precedence - Left to right
# ()
# **
# * /
# + -
print(3 * 3 + 3 / 3 - 3)

print(round(2.666666, 2))

print(8 // 3)  # floor division

result = 4 / 2
result /= 2
print(result)


# f-string

score = 520
max_score = 10000
print(f"Your Score is {score} and your max score is {max_score}")
