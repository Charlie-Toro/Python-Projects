# filereader
# Caleb Bell
# Reads file that contains pi to 30 places


with open('pi.txt') as file_object:
    contents = file_object.read()
    print(contents)