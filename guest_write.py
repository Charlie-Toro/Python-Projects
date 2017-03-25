# Guest
# Caleb Bell
# requests user's name and then writes to a file


name = input("Please enter your name: ")

with open('guest.txt', 'w') as file_object:
    file_object.write(name)
