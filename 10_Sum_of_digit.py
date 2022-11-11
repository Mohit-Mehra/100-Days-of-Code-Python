# Find the sum of the Digits of a Number

num = 12345

# Method 1: Using String Extraction method
num1 = "12345"
sum = 0
for i in num1:
    sum = sum + int(i)
print(sum)

# Method 2: Using Brute Force
sum = 0
while num != 0:
    digit = int(num % 10)
    sum += digit
    num = num / 10
print(sum)

# Method 3: Using Recursion 
def findSum(num):
    if num == 0:
        return 0
    return int(num % 10) + findSum(num / 10)

print(findSum(num))





