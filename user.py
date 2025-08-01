class User:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def get_first_name(self):
        return self.firstname
    def get_last_name(self):
        return self.lastname
    def full_name(self):
        return f"{self.firstname} {self.lastname}"