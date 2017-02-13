#Check user
#Caleb Bell
#Simulates website checking for unique user names

current_users = ['kmaloney','clbell4','zilke','vania','Ctopping','mmires']
new_users = ['ctopping','mmires','ecabellon','njacobs2','bflynn','mcavett']

for current_user in current_users:
    current_user.lower()
    
    for user in new_users:
        user.lower()
        if user in current_users:
            print('USERNAME IN USE!PLEASE CHOOSE ANOTHER!')
        else:
            print(user + " IS AVAILABLE!")