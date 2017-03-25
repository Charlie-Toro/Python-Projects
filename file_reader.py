# filereader
# Caleb Bell
# Reads file that contains pi to 30 places


filename = 'pi.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())