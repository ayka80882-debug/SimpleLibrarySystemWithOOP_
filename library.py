from student import *


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.students = []


    def addBook(self, book):
        self.books.append(book)


    def addStudent(self, student):
        self.students.append(student)


    def showBooks(self):
        if not self.books:
            print("There are no books.")
            return

        for book in self.books:
            book.showInfo()
            print("----------------------")


    def showStudents(self):
        if not self.students:
            print("There are no students.")
            return
        
        for student in self.students:
            student.showInfo()
            print("----------------------")

    def searchBook(self, bookID):
        for book in self.books:
            if book.bookID == bookID:
                return book
        return 


    def searchStudent(self, studentID):
        for student in self.students:
            if student.studentID == studentID:
                return student
        return 


    def borrowBook(self, studentID, bookID):
        student = self.searchStudent(studentID)
        book = self.searchBook(bookID)

        if student is None or book is None:
            print("Student or book not found.")
            return

        if book.isBorrowed:
            print("This book is already borrowed.")
            return

        book.isBorrowed = True
        student.borrowedBooks.append(book)
        print("Book borrowed.")


    def returnBook(self, studentID, bookID):
        student = self.searchStudent(studentID)
        book = self.searchBook(bookID)

        if student is None or book is None:
            print("Student or book not found.")
            return

        if book not in student.borrowedBooks:
            print("This student did not borrow this book.")
            return

        book.isBorrowed = False
        student.borrowedBooks.remove(book)
        print("Book returned.")