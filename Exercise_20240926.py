class Book:
    def __init__(self, title):
        self.title = title
        self.is_available = True

    def mark_as_borrowed(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed {self.title}")
        else:
            print(f"Sorry, '{self.title}' is currently not available")

    def mark_as_returned(self):
        self.is_available = True
        ...


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter the title of the book: ")
        book = Book(title)
        self.books.append(book)

    def borrow_book(self):
        title = input("Enter the title of the book to borrow: ")
        for book in self.books:
            if book.title == title:
                book.mark_as_borrowed()
                break
        else:
            print(f"No book in library with the title '{title}'")
            

    def return_book(self):
        ...

    def view_books(self):
        print("\nAvailable books:")
        for book in self.books:
            print(f"- {book.title}") if book.is_available is True else None

    def run(self):
        while True:
            print("\n1. Add Book\n2. Borrow Book\n3. Return Book\n4. View Available Books\n5. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                ...
            elif choice == '4':
                self.view_books()
            elif choice == '5':
                break

if __name__ == "__main__":
    library = Library()
    library.run()