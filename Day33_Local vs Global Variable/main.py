x = 10 # Global Variable
print(f"This is the Global variable {x}")

def local():
    y = 20 # Local variable
    print(f"This is the Local variable {y}")
    # Global variable can access within any function
    print(f"This is the Global variable {x}")
local()

# It will throw the error because local variable only access within the funcction it cannot access outside the function
# print(f"This is the Local variable {y}")


# If you want to access the global varibale within function then use global keyword

a = 100

def func():
    global a 
    a = 200
    b = 300
    print(a)
    print(b)
func()