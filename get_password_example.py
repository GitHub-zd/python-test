import getpass

passwd = getpass.getpass(prompt='enter your password:')
if passwd.lower() == 'zd1234':
    print('welcome')
else:
    print('the password entered is incorrent')

    