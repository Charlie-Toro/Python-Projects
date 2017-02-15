#rivers
#Caleb Bell
#practices looping through dictionaries by key-values of rivers and countries

rivers = {
    'Seine': 'France',
    'Nile': 'Egypt',
    'Ganges': 'India',

}

for river in rivers.keys():
    print(river + ' is a beautiful river')

for name in rivers.keys():
    print(name)

for country in rivers.values():
    print(country)