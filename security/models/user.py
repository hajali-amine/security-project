class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        print("First name: {}\n Last name: {}\n Email: {}\n "
              .format(self.first_name, self.last_name, self.email))
