# Addition
# Caleb Bell
# Prompts for 2 numbers and catches error if text provided


def addition(num1, num2):
    try:
        print(int(num1) + int(num2))
    except ValueError:
        print("Sorry, you provided a non-numeric input")


number1 = input('Please enter first number: ')
number2 = input('Please enter second number: ')

addition(number1, number2)
