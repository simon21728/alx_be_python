class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Returns the availability of the book."""
        return not self._is_checked_out

    def __str__(self):
        """Returns the string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """Represents a collection of books in the library."""
    
    def __init__(self):
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Adds a book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Checks out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    return True
        return False
    
    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    return True
        return False
    
    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            print("\n".join(available_books))
        else:
            print("No available books.")

