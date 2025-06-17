# It is always executed even in function where print statement will not execute


def table(n):
   
    try:
        for i in range(1,11):
            print(f"{int(n)} X {i} = {int(n) * i}")
    except Exception as e:
            print(e)
    finally:
         print("end of the program")
    
num = input("Enter the number: ")
table(num)
