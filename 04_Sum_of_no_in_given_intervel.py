# Sum of the Numbers in a Given Interval

num1 = int(input("Enter First No :- "))
num2 = int(input("Enter Second No :- "))
sum = 0

# Method 1: Using Brute Force
for i in range(num1,num2+1):
    sum += i
print(sum)

# Method 2: Using the Formula
# Formula to Find the Sum of Numbers in an Interval

# The formula to find the sum of n natural numbers is:
# Sum = n * ( n + 1 ) / 2

# Therefore in order to find the sum in a given interval we'll minus the sum of the numbers until the lower range from the whole sum and add an offset as the lowest bound is itself included in the summation. Hence the final formula is :
# Sum = b * ( b + 1 ) / 2 – a * ( a + 1 ) / 2 + a .
sum = int((num2 * (num2 + 1)/2) - (num1 * (num1 + 1)/2) + num1)
print(sum)

# Method 3: Using Recursion
def recursum(sum,num1,num2):
    if num1 > num2:
        return sum
    return num1 + recursum(sum,num1+1,num2)
sum = 0
print(recursum(sum,num1,num2))