
import time
def usingWhile():
    i = 0 
    while i < 100:
     i = i + 1 
     print(i)
    
def usingFor():
   for i in range(100):
      print(i+1)
    
init = time.time()
usingWhile()
t1 = time.time() - init

usingFor()
t2 = time.time() - init

print(f"The take to print using while loop is : {t1}")
print(f"The take to print using For loop is : {t2}")



print(1000)
print("wait!! , It will take 5 second to print the next line")
time.sleep(5)
print("Hello")
