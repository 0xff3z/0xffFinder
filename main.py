import socket
import requests
from contextlib import closing





Error = '\033[91m'
Succses = '\033[92m'

Ports = [19,20,21,22,23,24,25,80,443]

print("Select One")
inputUser = input('''
1 - One Domain
2 - Comming Soon Multiple Domains
''')

if inputUser == "":
    print("Error Select One")


if inputUser == "1":
    print("Enter Your Host")
    Hostname = input()

    try:
        ip = socket.gethostbyname(f"{Hostname}")
        NewHost = (f"http://{Hostname}")
        status = requests.get(f"{NewHost}")
        StatusCode = status.status_code
        print(Succses + f"Domain :{Hostname} ", f"The ip is: {ip}: " f"Status: {StatusCode}..Ok ")
    except socket.gaierror:
        print(Error, "Enter Valid Domain")
    except requests.exceptions.InvalidURL:
        print("Enter Valid Domain")







# if inputUser == "2":
#     print("Locate Your File Domains : Example Domains.txt")
#     hostNames = open(input())
#
#     for hostNames in hostNames:
#         ip = socket.gethostbyname(f"{hostNames}")
#         newhost = (f"http://{hostNames}")
#         status = requests.get(f"{newhost}")
#         statuscode = status.status_code
#         if statuscode == 200:
#             print(Succses + ip, " Status ", statuscode)
#         else:
#             print(statuscode + "  Not Found")




