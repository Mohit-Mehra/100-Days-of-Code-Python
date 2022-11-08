# Greatest of Two Numbers

num1 = int(input("Enter First No :- "))
num2 = int(input("Enter Second No :- "))

# Method 1: Using if-else Statements
if num1 > num2:
    print(num1)
else:
    print(num2)


# Method 2: Using Ternary Operator
print((num1 if num1 > num2 else num2))

# Method 3: Using inbuilt max() Function
print(max(num1,num2))