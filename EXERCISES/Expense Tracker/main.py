from datetime import datetime

expenses = [ ]

def add_expense():
    date_input = input("Date (YYYY-MM-DD) [Leave empty for today]:") 
    if not date_input:
          date = datetime.now().strftime("%Y-%m-%d")
    else:
          try:
               datetime.strptime(date_input , "%Y-%m-%d")
               date = date_input
          except ValueError:
                print("Invalid Format!!, Please enter YYYY_MM_DD")
                return
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    try:
        amount = int(input("Enter the amount: "))
    except:
       print("Please enter the number not word!!")
       return
    expenses.append({
        'Date' : date,
        'Category' : category,
        'Description' : description,
        'Amount' : amount 
    })

def view_expense():
    if not expenses:
      print("There is no expenses!!")
      return

    print("\nExpenses:\n")
    for i , expense in  enumerate(expenses,1):
       print(f"{i}. Date: {expense['Date']} , Category: {expense['Category']} ,   Description: {expense['Description']} , Amount: {expense['Amount']} ")

def filter_expense():
    print("Filter Option")
    print("\n 1. Category")
    print("\n 2. By Date")
    choice = input("Enter your option: ")
    if choice == '1':
        keyword = input("Enter the Category to filter by :".strip().lower())
        filtered = [e for e in expenses if e['Category'].lower() == keyword]
    elif choice == '2':
        keyword = input("Enter the Date to filter by :".strip().lower())
        try:
            datetime.strptime(keyword, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD (e.g., 2024-12-31).")
            return
        filtered = [e for e in expenses if e['Date'].lower() == keyword]
    else:
        print("Invalid input")
        return
    if not filtered :
        print("No matching expenses found.")
        return
    print("\n Filteres Result")
    for i , expense in enumerate(filtered, 1):
        print(f"{i}. Date: {expense['Date']} , Category: {expense['Category']} ,   Description: {expense['Description']} , Amount: {expense['Amount']} ")

def delete_expense():
    if not expenses:
        print("There is not Expenses")
        return
    view_expense()
    idx = int(input("Enter the record number to delete: "))
    if ( idx < 1 or idx >len(expenses)):
        print("No record at that number")
        return
    del expenses[idx-1]
    print("Expense Deleted!!!")

while True:
   
    user_input= input("\n1. Add Expenses\n2. view Expense\n3. Filter Expenses\n4. Delete Expense\n5. Exit\nEnter Your choice: ")

    if user_input == "1":
        add_expense()
    elif user_input == "2":
        view_expense()
    elif user_input == "3":
        filter_expense()
    elif user_input == "4":
        delete_expense()
    elif user_input == "5":
        print("Thank You!!")
        break
    