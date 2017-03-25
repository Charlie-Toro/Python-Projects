# guest book
# Caleb Bell
# Prompts users for name and writes to a file


name = ''

with open("guestbook.txt", 'a') as file_object:

    while True:
        name = input("Please enter your name for the guest list: ")
        content = file_object.write(name + ' visited here\n')
        print(name + ' visited here\n')
        if name.upper() == 'DONE':
            break

