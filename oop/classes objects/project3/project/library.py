class Library:
    def __init__(self):
        self.rented_books = {} # keep information regarding the usernames (key: str) and nested dictionary
        # as a value in which will keep information regarding the book names (key: str)
        # and days left before returning the book to the library (int) - ({usernames: {book names: days to return}}).
        self.user_records = []  # store the users (users objects) of the library
        self.books_available = {} # keep information regarding the authors
        # (key: str) and the books available for each of the authors (list of strings)

    def add_user(self, user):
        for u in self.user_records:
            if u.user_id == user.user_id:
                return f"User with id = {u.user_id} already registered in the library!"
        self.user_records.append(user)
        self.rented_books[user.username] = {}

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        for user in self.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return f"Please check again the provided username - " \
                           f"it should be different than the username used so far!"

                rented_books = self.rented_books[user.username]
                self.rented_books.pop(user.username)

                user.username = new_username
                self.rented_books[user.username] = rented_books
                return f"Username successfully changed to: {new_username} for userid: {user_id}"

        return f"There is no user with id = {user_id}!"


