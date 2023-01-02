class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):

        for _, rented_books in library.rented_books.items():
            for books_name, days in rented_books.items():
                if book_name == books_name:
                    return f'The book "{book_name}" is already rented and will be available in {days} days!'

        if author not in library.books_available:
            return
        if book_name not in library.books_available[author]:
            return

        self.books.append(book_name)

        if self.username not in library.rented_books:
            library.rented_books[self.username] = {}
        library.rented_books[self.username][book_name] = days_to_return

        library.books_available[author].remove(book_name)
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)

        library.books_available[author].appand(book_name)
        library.rented_books[self.username].remove(self.username)

    def info(self):
        return f"{', '.join(sorted(self.books))}"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
