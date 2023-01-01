# Check Whether a Given Number is an Armstrong Number or Not.
#  abcd = a^n + b^n + c^n + d^n = abcd
# where n = lenth/digit in number

number = 370

# Method 1 : Using Iteration
num = number
digit , sum = 0 , 0
length = len(str(num))
for i in range(length):
    digit = int(num % 10)
    num = num / 10
    sum += pow(digit,length)
if sum == number:
    print("Armstrong")
else:
    print("Not Armstrong")

# Method 2 : Using Recursion
num = number
digit , sum = 0 , 0
length = len(str(num))
def checkArmstrong(num,length,sum):
    if num == 0:
        return sum
    sum += pow(int(num%10),length)
    return checkArmstrong(num/10,length,sum)
if checkArmstrong(num,length,sum) == number:
    print("Asmstrong")
else:
    print("Not Armstrong")

