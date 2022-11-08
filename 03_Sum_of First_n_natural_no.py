# Sum of the First N Natural Numbers

num = int(input("Enter Number :-"))

# Method 1: Using Loop
sum = 0
for i in range(num+1):
    sum += i
print(sum)

# Method 2: Using Formula for the Sum of Nth Term
# Formula to Find the Sum of N terms
# Sum = ( Num * ( Num + 1 ) ) / 2

print(int(num*(num+1)/2))

# Method 3: Using Recursion
def getSum(num):
    if num == 1:
        return 1
    return num + getSum(num-1)
print(getSum(num))