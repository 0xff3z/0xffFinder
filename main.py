import os

Error = '\033[91m'
Succses = '\033[92m'



print("Select One")
inputUser = input('''
1 - One Domain
2 - Multiple Domains
''')

if inputUser == "":
    print("Error Select One")


if inputUser == "1":
    print("Enter Your Host")
    hostname = input()
    print("Enter Number Of Packets")
    PacketsNumber = input()
    response = os.system(f"ping -c {PacketsNumber} " + hostname)
    if response == 0:
        print(Succses + hostname + "      ...Ok")
    else:
        print(Error + hostname + "       ..No Response")


if inputUser == "2":
    print("Locate Your File Domains : Example Domains.txt")
    hostNames = open(input())
    print("Enter Number Of Packets")
    PacketsNumber = input()

    for hostNames in hostNames:


        response = os.system(f"ping -c {PacketsNumber} " + hostNames)
        if response == 0:
            print(Succses + hostNames + "      ...Ok")
            print("--"*50)
        else:
            print(Error + hostNames + "     /n  ..No Response")




