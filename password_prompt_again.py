import getpass

username = getpass.getuser()
print('username:',username)

while True:
    passwd = getpass.getpass("enter your password:")
    if passwd == 'zd1234':
        print('welcome')
        break
    else:
        print('the password is error')