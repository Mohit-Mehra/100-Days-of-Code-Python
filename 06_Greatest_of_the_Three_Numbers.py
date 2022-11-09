# Greatest of the Three Numbers
num1 = int(input('Enter First Number :- '))
num2 = int(input('Enter Second Number :- '))
num3 = int(input('Enter Third Number :- '))
max = 0
# Method 1: Using if-else Statements
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)

# Method 2: Using Nested if-else Statements
if num1 >= num2:
    if num1 >= num3:
        print(num1)
elif num2 >= num1:
    if num2 >= num3:
        print(num2)
else:
    print(num3)


# Method 3: Using Ternary Operator
max = num1 if num1 > num2 else num2
max = num3 if num3 > max else max
print(max)

