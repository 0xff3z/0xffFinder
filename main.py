import socket
import requests





Error = '\033[91m'
Succses = '\033[92m'

Ports = [80,443,20,21,22,24,25,3306]

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
        for port in Ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((Hostname, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()
            if result == 10035:
                print(Error,f"Port {port} is Closed")


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




