#fave num
#Caleb Bell
#uses a dictionary to store individuals' favorite numbers

fave_nums = {
    'James': [345, 234, 2],
    'Alex': [23, 12, 32],
    'Chris': [123, 23, 12],
    'Jenna': [2, 12, 12],
    'Felicia': [69, 2, 43],
}

for person, nums in sorted(fave_nums.items()):
    print(person.title() + " 's favorite numbers are: ")
    for num in nums:
        print(num)