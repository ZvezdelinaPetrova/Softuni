class Library:

    def __init__(self):
        self.user_records = []  # users (users objects) of the library
        self.books_available = {}  # authors (key) and the books available for each of the authors (list of strings)
                                    # {usernames: [] }
        self.rented_books = {}  # ({usernames: {book names: days to return}})

    def get_book(self, author, book_name, days_to_return, user):
        if author in self.books_available:
            for el in self.books_available[author]:
                if el == book_name:
                    user.books.append(book_name)
                    self.books_available[author].remove(el)
                    if user.username not in self.rented_books:
                        self.rented_books[user.username] = {}
                        self.rented_books[user.username][book_name] = days_to_return
                    else:
                        self.rented_books[user.username][book_name] = days_to_return
                    return f"{book_name} successfully rented for the next {days_to_return} days!"
            return f'The book "{book_name}" is already rented and will be' \
                   f' available in {self.rented_books[user.username][book_name]} days!'

    def return_book(self, author, book_name, user):
        inside = False
        for el in user.books:
            if el == book_name:
                inside = True
                user.books.remove(el)
                if author in self.books_available:
                    self.books_available[author].append(book_name)
                else:
                    self.books_available[author] = []
                    self.books_available[author].append(book_name)
        if not inside:
            return f"{user.username} doesn't have this book in his/her records!"

        for a in self.rented_books:
            if a == user.username:
                for x in self.rented_books[a]:
                    if x == book_name:
                        self.rented_books[a].pop(x)
                        break
