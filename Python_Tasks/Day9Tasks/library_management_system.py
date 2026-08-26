#16. Library Management System (Constructor & Inheritance)

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display(self):
        print("Title :", self.title)
        print("Author :", self.author)
        print("File Size :", self.file_size, "MB")


ebook = EBook("Python Programming", "Farooq Khan", 25)

ebook.display()