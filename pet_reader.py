# Pet_reader
# Caleb Bell
# Reads dog and cat names from a file; prints exception if they don't exist


def pet_read(filename):
    try:
        with open(filename) as f_obj:
            reader = f_obj.read()
            print(reader)
    except FileNotFoundError:
        print('SORRY FILE WAS NOT FOUND')


pet_read('dogs.txt')
pet_read('cats.txt')