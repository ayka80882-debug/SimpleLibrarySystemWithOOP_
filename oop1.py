from book import Book
from student import Student

book1 = Book(1, "Clean Code", "Robert Martin", 464)
book2 = Book(2, "Python Crash Course", "Eric Matthes", 560)

student1 = Student(1, "Ramal")

book1.showInfo()
student1.borrowBook(book1)
book1.showInfo()

student1.returnBook(book1)
book1.showInfo()
