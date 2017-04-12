# Favorite Number
# Caleb Bell
# Asks user for favorite number and stores in JSON file for later use.

import json


def get_number(num):
    """Prompts user for favorite number"""

    return num


def save_number(num):
    with open('fave_num.json', 'w') as file_object:
        json.dump(num, file_object)


def load_number():
    try:
        with open('fave_num.json') as file_object:
            reader = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return reader


num = input("Please enter your favorite Number: ")
save_number(num)
print(load_number())
