import getpass

try:
    p = getpass.getpass()
except Exception as error:
    print('error',error)
else:
    print('password enter:',p)