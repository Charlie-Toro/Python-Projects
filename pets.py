#Pets
#Caleb Bell
# Stores name of pet, animal type, and owner in dictionaries

fluffy = {
    'species': 'cat',
    'owner':'Charlie Brown',
}

lassie = {
    'species': 'dog',
    'owner': 'Timmy'
}

goldie = {
    'species': 'fish',
    'owner': 'Johnny',
}

slithery = {
    'species': 'snake',
    'owner': 'Roger',
}

pets = [fluffy, lassie, goldie, slithery]

for pet in pets:
    print(pet['species'] + ' belongs to ' + pet['owner'])
