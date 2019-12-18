import subprocess

subprocess.call(["touch","sample.txt"])
subprocess.call(["ls"])
print("sample file created")

subprocess.call(["rm","sample.txt"])
subprocess.call(["ls"])
print("sample file deleted")