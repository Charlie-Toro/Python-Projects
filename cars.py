#Cars
#Caleb bell
#Prints favorite cars and a Statement

cars = ['corvette','mustang','camaro','boxter','carrera']
message = "One day I will own a "

print(message + cars[0].title() + '.')
print(message + cars[1].title() + '.')
print(message + cars[2].title() + '.')
print(message + cars[3].title() + '.')
print(message + cars[4].title() + '.')

#4-10 Continuation

print("")
print("The first 3 cars in the list are ")

for car in cars[:3]:
    print(car.title())

print("")
print("Three items from the middle of the list are ")

for car in cars[1:4] :
    print(car.title())   

print("")
print("The last 3 items of the list are ")

for car in cars[-3:]:
    print(car.title())