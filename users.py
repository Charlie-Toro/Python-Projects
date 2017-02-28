# Users
# Caleb Bell
# Creates user and describes their attributes


class User:

    def __init__(self, first_name, last_name, location, **facts):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.facts = facts

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


new_user = User("Mark", "Perry", "Austin,TX", DOB='12/4/67', Car='Ferrari', Pets='Dog')
print(new_user.first_name)
print(new_user.last_name)
print(new_user.location)
print(new_user.facts)

new_user.describe_user()
new_user.greet_user()



