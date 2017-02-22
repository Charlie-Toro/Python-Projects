#Cities
#Caleb Bell
# stores cities in a dictionary with general information about the city

cities = {
'Austin': {
    'country': 'United States',
    'population': 1990437,
    'fact': "Led Zeppelin’s Robert Plant owns a house in Austin",
},

'Hong Kong': {
    'country':'China',
    'population':1357000000,
    'fact': 'The summit of Mt Everest marks the border between China and Nepal.',
},
    'Tel Aviv': {
        'country' : 'Israel',
        'population': 411800,
        'fact': 'The city is the center of economy, culture and the media of Israel.',
    },
}

for city, info in cities.items():
    country = info['country']
    pop = info['population']
    fact = info['fact']

    print(city + " is located in " + country + ' with a population of ' + str(pop))
    print(' One fact about this city is ' + fact)