class library:

    def __init__(self):
         self.books = []

    def addBooks(self , name , genre):
        book = {"name" : name , "genre" : genre}
        self.books.append(book)
        print(f"The book '{name}' of genre '{genre}' is added to the library")

    def showBook(self):
        if not self.books:
            print("There is no Books in library")
        else:
            print("\n Books in Library is :")
            for i , book in enumerate(self.books , 1):
                 print(f"{i}. Name : {book['name']} , Genre : {book['genre']}")
    
    def delBooks(self ):
         if not self.books:
              print("There are no Books in Library")
              return
         self.showBook()
         askUser = int(input("Enter the Book Number to delete ( 1 , 2 ,...)"))
         if 1 <= askUser <= len(self.books):
                    removed_book = self.books.pop(askUser - 1)
                    print(f"Deleted: '{removed_book['name']}' from the library.")
         else:
                    print("Invalid book number.")
                 
                  

    def noOfBoooks(self):
        if not self.books:
            print("There is no books in library")
        else:
              length = len(self.books)
              print(f"The No. of Books in Library is : {length}")
                    
mylib = library()

while True:
      userInput = input("Press:\n1. Add Books\n2. View Books\n3. No. of Books\n4. Delete Book\n5. exit\n>")
      if userInput == "1":
           name = input("Enter the name of the Book: ").capitalize()
           genre = input("Enter the genre of the Book: ").capitalize()
           mylib.addBooks(name , genre)
      elif userInput == "2" :
           mylib.showBook()
      elif userInput == "3":
           mylib.noOfBoooks()
      elif userInput == "4":
           mylib.delBooks()
      elif userInput == "5":
           print("Thank You")
           break
      else:
           print("Invalid Input")
           
