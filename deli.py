# Deli
# Caleb Bell
# Takes order of sandwiches and stores them in list

sandwich_orders = ['PB &J', 'Reuben', 'Ham & Cheese', 'Turkey', 'Tuna', 'Pastrami', 'Pastrami', 'Pastrami']
finished_sandwiches = []

print("Unfortunately, the deli has run out of pastrami!")

while sandwich_orders:

    while 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')

    made_sandwich = sandwich_orders.pop()
    print('Your ' + made_sandwich + ' has been completed\n')
    finished_sandwiches.append(made_sandwich)

for sandwich in finished_sandwiches:
    print(sandwich + '\n')


