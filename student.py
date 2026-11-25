from book import *

<<<<<<< HEAD

class Student:
    def __init__(self, studentID, name):
        self.studentID = studentID
        self.name = name
        self.borrowedBooks = []


    def showInfo(self):
                print(f"""

ID: {self.studentID}
Title: {self.name}
Author: {len(self.borrowedBooks)}
        """)


    def borrowBook(self, book):
        if book.isAvailable:
              book.borrow()
              self.borrowedBooks.append(book)
        else:
              print("Book is not available...")

=======
class Student:
    def __init__(self,name):
        self.name = name
        self.borrowedBooks = []

    def showInfo(self):
        print(f"""
                
            ID: {self.bookID}
            title: {self.title}
            author: {self.author}
            pageCount: {self.pageCount}
        
        """)

    def borrowBook(self, book):
        if book.isAvialable:
            book.borrow()
            self.borrowedBooks.append(book)
        else:
            print("Book is not avialable...")
>>>>>>> e0700fd5e88c1472dd3decc42badd570d2ad9973

    def returnBook(self, book):
        if book in self.borrowedBooks:
            book.returnBook()
            self.borrowedBooks.remove(book)
        else:
<<<<<<< HEAD
            print("Book is not available...")


student1 = Student(1, "Taleh")
student2 = Student(2, "Ramiz")
student3 = Student(3, "Ramal")


book1 = Book(1, "Clean Code", "Robert Martin", 464)

=======
            print("Book is not avialable...")

student1 = Student(1 ,"Taleh")
student2 = Student(2 ,"Ramiz")
student3 = Student(3 ,"Ramal")

book1 = Book(1 ,"Clean Code" , "Robert Martin",464)
>>>>>>> e0700fd5e88c1472dd3decc42badd570d2ad9973

student1.borrowBook(book1)
print("Reading...")
student1.returnBook(book1)