import os

print("Enter Your Host")
hostname = input()

response = os.system("ping -c 1 " + hostname)
if response == 0:
    print(hostname + "Good")
else:
    print(hostname + "Not Good")

