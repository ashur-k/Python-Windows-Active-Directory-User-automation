from changePassword import change_password


''' 
  Change Password Function parameters
  user cn name, whose password is required to change
  user new password aiming to change
  ldap server full name
  ldap administrator name
  ldap administrator password
'''

if __name__ == "__main__":
  change_password(
    'Ashur Kanwal', 
    '100Fred100', 
    ldap_server = 'LDAP_SERVER_NAME', 
    ldap_administrator_name = 'LDAP_ADMINISTRATOR_NAME', 
    ldap_administrator_password='LDAP_ADMINISTRATOR_PASSWORD'
    )  
