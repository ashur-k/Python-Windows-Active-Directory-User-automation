# Changing Windows Server Active Directory User's Password:
1. Download project from Git to your workspace
2. Setup virtual environment for python
   1. Use following commands to setup virutalenv in windows:
      1. pip install virtualenv
      2. virtualenv env
      3. env/scripts/activate
      4. In case if windows says scripts are not active please run following command and try again to run above command.
         1. Set-ExecutionPolicy Unrestricted -Force.
         2. For more information on about the error please read the below link.
         3. https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows/18713789.
3. Install your requirements with following commands:
   1. pip install -r requirements.txt
4. Create .env file and give following information from your windows server.
   1. LDAP_SERVER_NAME="ldap-server-name"
   2. LDAP_ADMINISTRATOR_NAME = "ldap-adminstrator-name"
   3. LDAP_ADMINISTRATOR_PASSWORD = "ldap-administrator-password" 
5. You can also give the same values in testChangePassword.py directly.
6. You need to give following 5 values in testChangePassword.py, change_password function parameters.
   1. User cn name whose password you are aiming to change.
   2. user new password that you want to set.
   3. ldap server name
   4. ldap adminstrator name
   5. ldap administrator password

Once all steps are done run python file to change user name password on window active directory domain.
codes are tested and working fine.

# Version Information:
1. All packages that are installed their version information is on requirements.txt.
2. Python version that I have use to run the codes is Python 3.10.0. 11/10/2021 it is the latest python version.
   