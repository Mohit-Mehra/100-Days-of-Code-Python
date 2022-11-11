# Find the Reverse of a Number

num = 1234
temp = num
reverse = 0

# Method 1: Using Simple Iteration
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
print(reverse)

# Method 2: Using String Slicing
num = 1234
print(str(num)[::-1])

# Method 3: Using Recursion
num = 1234
reverse = 0
def recurSum(number,reverse):
    if number == 0:
        return reverse
    remainder = int(number%10)
    reverse = (reverse*10) + remainder
    return recurSum(int(number/10),reverse)
print(recurSum(num,reverse))