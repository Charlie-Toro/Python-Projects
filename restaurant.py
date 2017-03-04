# Restaurant
# Caleb Bell
# demonstrates use of classes that describes restaurant


class Restaurant:
    """restaurant class that takes cuisine type"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The name of the restaurant is: " + self.restaurant_name.title())
        print("The cuisine type is: " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open!")

    def set_number_served(self, numserv):
        self.number_served = numserv

    def increment_number_served(self, increment_number):
        self.number_served += increment_number
        return self.number_served


restaurant = Restaurant("Nando's Peri Peri", "Peruvian Cuisine")
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.increment_number_served(50))


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def set_flavors(self, *flavors):
        self.flavors = flavors
        return flavors

    def get_flavors(self, *flavors):
        for flavor in flavors:
            print(flavor)


ice_cream_stand = IceCreamStand("Frosty's", "Ice Cream")
ice_cream_stand.describe_restaurant()

flavors = ice_cream_stand.set_flavors('cheesecake', 'vanilla', 'chocolate', 'strawberry')

ice_cream_stand.get_flavors(flavors)






