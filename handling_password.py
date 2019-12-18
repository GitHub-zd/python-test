import sys
import paramiko
import time


ip = 'xx'
username = 'xx'
password = 'xx'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()
ssh_client.connect(hostname = ip,username = username,password = password)
print("successful connection ",ip)

ssh_client.invoke_shell()
remote_connection = ssh_client.exec_command('cd /root/; mkdir zhangduan \n')
ssh_client.close