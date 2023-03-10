class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) > 15 or len(value) < 5:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        has_upper = [i for i in value if i.isupper()]
        if len(has_upper) <= 0:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        has_digit = [i for i in value if i.isdigit()]
        if len(has_digit) <= 0:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
