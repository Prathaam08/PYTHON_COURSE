# IT WILL GIVE ERROR IF USER INPUT IS WRONG
num = int(input("Enter the number between 5 and 9 :"))
if ( num < 5 or num > 9):
    raise ValueError("Number should be between 5 and 9")