#Pizza Toppings
#Caleb Bell
# Uses a while loop to ask user for pizza toppings


toppings = ''

while toppings.lower() != 'quit':
    toppings = input("Please enter all the toppings you would like on your pizza: ")
    if toppings.lower() == 'quit':
        break
    else:
        print(toppings + " will be added to your pizza!")


