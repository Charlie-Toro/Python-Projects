# Magician
# Caleb Bell
# Passes a list of magician names to a function and prints names


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    great = "The Great "
    magic = [great + magician for magician in magicians]
    return magic


magic = ['zambini', 'disappearo', 'magico']


mag = make_great(magic)
show_magicians(mag)


