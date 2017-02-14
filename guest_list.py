#Guest list
#Caleb Bell
#Prints a list of invitations to guest

guests = ['barack obama','Michelle Obama','Will Smith','Thandie Newton']

message = ",it would be an honor if you could come for dinner!"

print(guests[0].title() + message)
print(guests[1] + message)
print(guests[2] + message)
print(guests[3] + message)

print("It is a shame that Will Smith cannot make it.")

guests[2] = 'Halle Berry'

print('')
print(guests[0].title() + message)
print(guests[1] + message)
print(guests[2] + message)
print(guests[3] + message)

print("")
print("It turns out that there will be more guests coming to dinner.")

add_guest = guests.insert(0 , "Morgan Freeman")
add_guest2 = guests.insert(2 , "Samuel Jackson" )
add_guest3 = guests.append("Hilliary Clinton")

print("")
print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2] + message)
print(guests[3] + message)
print(guests[4] + message)
print(guests[5] + message)
print(guests[6] + message)

print("")
print("Sadly, Only 2 people can come to the dinner party now.")

uninvite1 = guests.pop(6) #first guest to invite
print("Sorry "+ uninvite1 +" but I must cancel your invitation.")
uninvite2 = guests.pop(5)
print("Sorry " + uninvite2 + " but I must cancel your invitation")
uninvite3 = guests.pop(4)
print("Sorry " + uninvite3 + " but I must cancel your invitation.")
uninvite4 = guests.pop(3)
print("Sorry " + uninvite4 + " but I must cancel your invitation.")
uninvite5 = guests.pop(2)
print("Sorry " + uninvite5 + " but I must uninvite you.")

print("")
print(guests[1] + " you are still invited to the party.")
print(guests[0] + " you are still invited to the party.")
print(len(guests))

del guests[1]
del guests[0]
print(guests)



