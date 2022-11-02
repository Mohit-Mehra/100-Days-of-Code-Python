# Check if a Number is Even or Odd

num = int(input("Enter a Number :- "))

#  Method 1: Using Brute Force
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Method 2 : Using Ternary Operator
# Syntax : ( True : Action ) if ( Condition ) else ( False : Action )
print("Even") if num%2==0 else print("Odd")

# Method 3 : Using Bitwise Operator
def isEven(num):
    return not num&1
if __name__ == "__main__":
    
    if isEven(num):
        print("Even")
    else:
        print("Odd")