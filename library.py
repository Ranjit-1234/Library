class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book):
        if book.id in self.books:
            print("Book with ID {} already exists.".format(book.id))
        else:
            self.books[book.id] = book
            print("Book added successfully.")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book removed successfully.")
        else:
            print("Book with ID {} does not exist.".format(book_id))

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books.values():
                print("ID: {}, Title: {}, Author: {}".format(book.id, book.title, book.author))


class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author


def main():
    library = Library("My Library")

    while True:
        print("\n1. Add a book")
        print("2. Remove a book")
        print("3. Display all books")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(id, title, author)
            library.add_book(book)

        elif choice == '2':
            id = input("Enter book ID to remove: ")
            library.remove_book(id)

        elif choice == '3':
            library.display_books()

        elif choice == '4':
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
