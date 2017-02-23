# sandwiches
# Caleb Bell
# Builds a sandwich based on user's taste


def make_sandwich(*ingredients):
    for ingredient in ingredients:
        print(ingredient)


print("Your sandwich consists of: ")
make_sandwich('pickles', 'ham', 'cheese', 'mustard', 'ketchup', 'anchovies')
