# Restaurant
# Caleb Bell
# demonstrates use of classes that describes restaurant


class Restaurant:
    """restaurant class that takes cuisine type"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The name of the restaurant is: " + self.restaurant_name.title())
        print("The cuisine type is: " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open!")


restaurant = Restaurant("Nando's Peri Peri", "Peruvian Cuisine")
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()
