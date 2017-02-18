#Multiple10
#Caleb Bell
#Asks user for number and determines if it is a multiple of 10

number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10")
else:
    print(str(number) + " is not a multiple of 10.")