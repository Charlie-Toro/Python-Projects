# Users
# Caleb Bell
# Creates user and describes their attributes


class User:

    def __init__(self, first_name, last_name, location, **facts):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.facts = facts
        self.login_attempts = 0

    def describe_user(self):
        user_facts = {}
        print("User's first name is: " + self.first_name)
        print("User's last name is: " + self.last_name)
        print("User's location is: " + self.location)

        for key, value in self.facts.items():
            user_facts[key] = value
            print(user_facts)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self):
        attempts = self.login_attempts + 1
        return attempts

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privilege:

    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):

    def __init__(self, first_name, last_name, location, **facts):
        super().__init__(first_name, last_name, location, **facts)
        self.privilege = Privilege("make user", "delete user", "read files")





