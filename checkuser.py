#Check user
#Caleb Bell
#Simulates website checking for unique user names

current_users = ['kmaloney','clbell4','zilke','vania','Ctopping','mmIreS']
new_users = ['ctopping','mmires','ecabellon','njacobs2','bflynn','mcavett']


new_user = [new_user.lower() for new_user in new_users]
current_user = [current_user.lower() for current_user in current_users]

for user in new_user:
    if user in current_user:
        print("USERNAME IS ALREADY TAKEN!")
    else:
        print(user + ' IS AVAILABLE!')
