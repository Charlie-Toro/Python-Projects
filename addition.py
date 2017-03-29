# Addition
# Caleb Bell
# Prompts for 2 numbers and catches error if text provided


def addition(nums=[]):
    s = 0
    for num in nums:
        s += num
        print(s)


num_list = list()

while True:
    try:
        number = input("Please enter a number(Enter Done to quit): ")
        if number.lower() == 'done':
            break
        n = int(number)
        num_list.append(n)
        addition(num_list)
    except ValueError:
        pass









