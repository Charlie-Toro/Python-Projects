# user profile
# Caleb Bell
# creates user profile based on a key-value


def build_profile(first, last, **info):
    profile = {}
    profile['fname'] = first
    profile['lname'] = last
    for key,value in info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Caleb', 'Bell', location='Laurel', DOB='8/4/86')
print(user_profile)