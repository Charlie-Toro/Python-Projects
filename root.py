# root
# Caleb Bell
# imports users module and created new instance of user

from users import Admin

root = Admin('root', 'user', 'users')
root.privilege.show_privileges()

