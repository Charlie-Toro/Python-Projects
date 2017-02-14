#Pizzas
#Caleb Bell
#Stores name of favorite pizzas and demonstrates lists and loops

pizzas = ['cheese','hawaiian','pepperoni']

for pizza in pizzas:
    print(pizza.title() + " is a pizza that I like!")
    
print("Pizza is my favorite dish!")

#4-11 appending to pizza program

pizzas.append("mushroom")
friend_pizzas = pizzas[:]
friend_pizzas.append('mexican')

print("My favorite pizzas are ")

for pizza in pizzas:
    print(pizza.title())
    
print("")
print("My friend's favorite pizzas are ")

for pizza in friend_pizzas:
    print(pizza.title())