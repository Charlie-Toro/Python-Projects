# Movie Tickets
# Caleb Bell
# Ask user their age and provides cost of movie tickets based on info provided

message = ''

while message.lower() != "done":
    age = input("Please provide your age: ")
    age = int(age)
    if age < 3:
        print("Your movie ticket is free.")
    if (age >= 3) and (age <= 12):
        print("Your movie ticket will cost $10")
    if age > 12:
        print("Your movie ticket will cost $15")
    message = input("Please say done when you are finished.")







