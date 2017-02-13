#Helloadmin 
#Caleb Bell
#prints a greeting to each user logged in to a website

users = ['admin','mclair','clbell4','rowhb','vania']

if not users:
    print("We need to find some users!")
for user in users:
    if user == 'admin':
        print("Hello Admin,would you like to see a status report?")
    else:
        print('Hello' +' '+ user)