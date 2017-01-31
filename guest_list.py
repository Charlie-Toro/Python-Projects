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



