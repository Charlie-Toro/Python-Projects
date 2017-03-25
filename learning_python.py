# learning python
# Caleb Bell
# reads file learning_python.txt


file = "learning_python.txt"

with open(file) as file_object:
    contents = file_object.read()
    print(contents * 3)


with open(file) as file_object:
    for line in file_object:
        print(line * 3)

with open(file) as file_object:
    content = file_object.readline()


print(content*3)

with open(file) as file_object:
    for line in file_object:
        print(line.replace('Python', 'c'))