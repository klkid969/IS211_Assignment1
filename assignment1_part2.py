class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}")
        
book1 = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
book2 = Book("Walter Scott", "Ivanhoe: A Romance")

book1.display()  # Should print: Harry Potter and the Goblet of Fire, written by J.K. Rowling
book2.display()  # Should print: Ivanhoe: A Romance, written by Walter Scott
