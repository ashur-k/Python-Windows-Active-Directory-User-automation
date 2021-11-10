from os import error
from pyad import *
from decouple import config



# Setting defaults login details to WindowsServer
# Taking values from python-decouple-set-environment
LDAP_SERVER_NAME = config('LDAP_SERVER_NAME')
LDAP_ADMINISTRATOR_NAME = config('LDAP_ADMINISTRATOR_NAME')
LDAP_ADMINISTRATOR_PASSWORD = config('LDAP_ADMINISTRATOR_PASSWORD')


def change_password(
  user_name, 
  user_new_password, 
  ldap_server = LDAP_SERVER_NAME, 
  ldap_administrator_name = LDAP_ADMINISTRATOR_NAME, 
  ldap_administrator_password = LDAP_ADMINISTRATOR_PASSWORD
  ):
  
  # Logging Into Windows Server
  pyad.set_defaults(
    ldap_server=ldap_server, 
    username=ldap_administrator_name, 
    password=ldap_administrator_password
  )
  ''' try block with cn getting user name
      changing user password and printing
      success message
  '''
  
  try:
    cn=pyad.aduser.ADUser.from_cn(user_name)
    pyad.aduser.ADUser.set_password(cn, password=user_new_password)
    password_change_at = pyad.adobject.ADObject._get_password_last_set(cn)
    print(f"{user_name} password is successfully changed at {password_change_at}")
  except:
    print("Update password failed")

if __name__ == "__main__":
  # Calling change password method and user details
  change_password('thanburry0', '100Fred100')
  