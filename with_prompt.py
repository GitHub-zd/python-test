import getpass

try:
    p = getpass.getpass('please input your password:')
except Exception as error:
    print('error',error)

else:
    print("enter pw:",p)
