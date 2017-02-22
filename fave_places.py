#Favorite Places
#Caleb Bell
#stores favorite places of people in a dictionary

favorite_places = {
    'eric': ['paris','raleigh','durham'],
    'charles': ['manilla','bangkok','Las Vegas'],
    'jessica': ['hong kong','nice','savannah'],
    'michelle': ['san francisco','san diego','seattle'],

}

for person, place in favorite_places.items():
    print(person.title() + "'s favorite places are: ")
    for pla in place:
        print(pla.title())

