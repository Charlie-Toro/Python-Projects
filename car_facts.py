# Car Facts
# Caleb Bell
# accepts facts about a car and stores in a dictionary


def make_car(manufacturer, model, **modelfacts):
    carfacts = {}
    carfacts['manufacturer'] = manufacturer
    carfacts['model'] = model

    for key, value in modelfacts.items():
        carfacts[key] = value

    return carfacts

car = make_car('Chevrolet', 'Corvette', color='red', transmission='manual')

print(car)