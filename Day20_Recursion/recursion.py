# Factorial 
def factorial(n):
    if ( n == 0 or n == 1):
        return 1
    else :
        return n * factorial( n - 1)
    
print(factorial(5))
print(factorial(4))
print(factorial(3))

# Fibonacci series
print("Fibonnaci Series")
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter number of terms: "))
for i in range(n):
    print(fibonacci(i), end=' ')
print()
    
# Sum of Natural Numbers
def sumOfNum(n):
    if ( n == 0):
        return 0
    elif ( n == 1):
        return 1
    else:
        return n + sumOfNum(n-1)

num = int(input("Enter number of terms: "))
print(f"Sum of {num} natural number is {sumOfNum(num)}")
print()

# Print Numbers from 1 to N
def print_forward(n):
    if ( n >= 1):
        print_forward(n-1)
        print(n ,  end =' ')

num = int(input("Enter a number: "))
print("Numbers from 1 to", num, "are:")
print_forward(num)



    

    
    
