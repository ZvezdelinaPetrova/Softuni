class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        if len(name) >= self.min_length:
            return True
        return False

    def __is_mail_valid(self, mail):
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True
        return False

    def validate(self, email):
        separated = email.split("@")
        name_is = separated[0]
        separated_2 = separated[1].split(".")
        mail_is = separated_2[0]
        domain_is = separated_2[1]

        # index_of_at = email.index("@")
        # index_of_dot = email.index(".")
        # username = email[:index_of_at]
        # mail = email[index_of_at + 1: index_of_dot]
        # domain = email[index_of_dot + 1:]

        if EmailValidator.__is_name_valid(self, name_is) and EmailValidator.__is_mail_valid(self, mail_is) \
                and EmailValidator.__is_domain_valid(self, domain_is):
            return True
        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
