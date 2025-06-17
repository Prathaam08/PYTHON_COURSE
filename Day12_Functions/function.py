def calAvg(a,b):
    print((a+b)/2)

def isGreater(a,b):
    if(a > b):
        print("First number is greater that is :",a)
    else:
        print("Second number is greater or equal to a that is :", b)

a = 80
b = 50

calAvg(a,b)
isGreater(a,b)

# Function to Check Even or Odd
def isEven(a):
    if( a % 2 == 0):
        print(a,"is even number")
    else:
        print(a,"is odd number")

a = 69
isEven(a)

# Function to Reverse a String
def reverseString(s):
    print(s[::-1])

reverseString("Pratham")

