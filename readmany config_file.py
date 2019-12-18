from configparser import ConfigParser
import glob

p = ConfigParser()
files = ['hello.ini','hi.ini','zd.ini','read_simple.ini']
files_found = p.read(files)
files_mission = set(files) - set(files_found)

print("file found:",files_found)
print("file miss:",files_mission)
