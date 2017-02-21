# City
# Caleb Bell
# Accepts name of city and the country it is in and prints a message


def describe_city(city_name, country='USA'):
    print(city_name + " is located in " + country)


describe_city("Los Angeles")
describe_city("Raleigh")
describe_city(city_name='Bangkok', country='Thailand')