class Library:
    def __init__(self,list,name):
        self.BookList = list
        self.name = name
        self.LenDict = {}

    def display_books(self):
        print(f"{self.name},We have {len(self.BookList)} books in our Library")
        sno =1
        for i in self.BookList:
            print(f"{sno} {i}")
            sno += 1

    def lendBook(self,book):
        if book in self.BookList:
            if book not in self.LenDict:
                self.LenDict.update({book:self.name})
                print("Lenderbook Database has been updated now,you can take the book now")
            else:
                print(f"This book is currently taken by {self.LenDict[book]}")

    def addBook(self,book):
        self.BookList.append(book)
        print("The new book is added to the BookList")

    def returnBook(self,book):
        if book in self.BookList:
            if book in self.LenDict.keys():
                self.LenDict.pop(book)
                print("Book has been returned")
            else:
                print("This book is not in use")
        else:
            print("this book is not in our Library")


l1 = Library(["python","java","javascript","angular","react","django","flask"],"Pranav")


if __name__ =='__main__':
    l1 = Library(["python", "java", "javascript", "angular", "react", "django", "flask"], "Pranav")
    while(True):
        print(f"Welcome to the {l1.name}'s Library,Enter your choice to continue")
        print(" 1 -> Display Books")
        print(" 2 -> Lend a Book")
        print(" 3 -> Add Books")
        print(" 4 -> Return a Book")

        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("invalid option")
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            l1.display_books()

        if user_choice == 2:
            book = input("Enter the book you want")
            l1.lendBook(book)

        if user_choice == 3:
            book = input("Enter the name of the book that you want to add")
            l1.addBook(book)

        if user_choice == 4:
            book =input("Enter the name of the book you want to return: ")
            l1.returnBook(book)

        print("press q to quit or c to continue")
        user_choice2 = ""
        while(user_choice2 !="c" and user_choice !="q"):
            user_choice2 = input()
            if user_choice2 == 'q':
                exit()
            elif user_choice2 =='c':
                continue

