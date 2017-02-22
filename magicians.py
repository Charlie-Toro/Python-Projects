# Magician
# Caleb Bell
# Passes a list of magician names to a function and prints names


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    for magician in magicians:
        magician = 'The Great ' + magician
        return magician


magic = ['zambini', 'disappearo', 'magico']

magicians = make_great(magic)
show_magicians(magicians)

