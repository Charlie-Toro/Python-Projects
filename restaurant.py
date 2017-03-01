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

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type, *flavors)
        self.flavors = flavors

        def display_flavors(self):
            for flavor in self.flavors:
                print(flavor)


ice_cream_stand = IceCreamStand("Frosty's", "Ice Cream", "Vanilla", "Chocolate","Cheesecake", "Strawberry", "Mint")

ice_cream_stand.display_flavors()






