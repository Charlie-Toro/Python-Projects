# Deli
# Caleb Bell
# Takes order of sandwiches and stores them in list

sandwich_orders = ['PB &J', 'Reuben', 'Ham & Cheese', 'Turkey', 'Tuna']
finished_sandwiches = []

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print('Your ' + made_sandwich + ' has been completed')
    finished_sandwiches.append(made_sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)


