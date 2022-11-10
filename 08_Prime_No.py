# Check Whether a Number is a Prime or Not
num = 15
flag = 0 

# Method 1: Simple iterative solution
for i in range(2,num):
    if num % i == 0:
        flag = 1
        break
if flag == 1:
    print("Not Prime")
else:
    print("Prime")
    
# Method 2: Basic Recursion technique
def checkPrime(num,iter=2):
    if num == iter:
        return True
    if num % iter == 0:
        return False
    return checkPrime(num,iter+1)
if checkPrime(num) == True:
    print("Prime")
else:
    print("Not Prime")
