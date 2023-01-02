class Registration:

    def add_user(self, user, library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user, library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library):
        for u in library.user_records:
            if u.user_id == user_id:
                if u.username != new_username:
                    u.username = new_username
                    for e in library.rented_books:
                        if e.user_id == user_id:
                            e.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                elif u.username == new_username:
                    return f"Please check again the provided username - it should " \
                           f"be different than the username used so far!"
        return f"There is no user with id = {user_id}!"





