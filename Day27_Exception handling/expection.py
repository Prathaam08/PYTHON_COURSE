# supppose we are printing the table and user give input string instead of int

num = input("Enter the number: ")
print(f"Multiplication table of {num} is : ")
try:
    for i in range(1,11):
        print(f"{int(num)} X {i} = {int(num) * i}")
except Exception as e:
    print(e)

#    OR

# except:
#     print("Invalid input")


print("End of Program")
