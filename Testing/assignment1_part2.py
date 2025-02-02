class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}")

# Create two book objects
book1 = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
book2 = Book("Walter Scott", "Ivanhoe: A Romance")

# Display the books
book1.display()
book2.display()
