# Check if a Number is Positive and Negative

num = 15

#  Method 1: Using Brute Force
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Method 2 : Using Nested if-else
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

# Method 3 : Using Ternary Operator
# Syntax : ((Condition)? (if True:Action):(if False:Action))
print("Positive" if num>=0 else "Negative")