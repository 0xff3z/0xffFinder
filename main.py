import socket
import requests
import sys






Error = '\033[91m'
Succses = '\033[92m'
Ports = [80,443,20,21,22,24,25,3306]

def CheckStatus():
    ip = socket.gethostbyname(f"{Hostname}")
    NewHost = (f"http://{Hostname}")
    status = requests.head(f"{NewHost}")
    StatusCode = status.status_code
    print(Succses + f"Domain :{Hostname} ", f"The ip is: {ip}: " f"Status: {StatusCode}..Ok ")
    for port in Ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)
        result = s.connect_ex((Hostname, port))
        if result == 0:
            Services = socket.getservbyport(port)
            print(f"Port {port} is Open",Services.format(port))
        else:
                print(Error, f"Port {port} is Closed")
                s.close()


def CheckStatusOfDomains():
    with open("Domains.txt","r") as File:
        Lines = File.read()
        Lines = Lines.splitlines()
        for line in Lines:
           ip = socket.gethostbyname(f"{line}")
           NewHost = (f"http://{line}")
           status = requests.head(f"{NewHost}")
           StatusCode = status.status_code
           print(Succses + f"Domain :{line} ", f"The ip is: {ip}: " f"Status: {StatusCode}..Ok ")
           for sub in subdomains:
               url = f"http://{sub}.{line}"
               try:
                   requests.head(url)
                   print(Succses, "[+]Discovred Doamins:", url)
               except:
                   print(Error, "Not Found", url)

           for port in Ports:
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               socket.setdefaulttimeout(0.2)
               result = s.connect_ex((line, port))
               if result == 0:
                   Services = socket.getservbyport(port)
                   print(f"Port {port} is Open", Services.format(port))
               else:
                   print(Error, f"Port {port} is Closed")
                   s.close()

file = open("subDomains.txt","r")
contentInFile = file.read()
subdomains = contentInFile.splitlines()
def SubDomains():
        for sub in subdomains:
            url = f"http://{sub}.{Hostname}"
            try:
                requests.head(url)
                print( Succses,"[+]Discovred Doamins:", url)
            except:
                print(Error,"Not Found",url)





inputUser = input('''
1 - One Domain
2 - Multiple Domains
''')

if inputUser == "":
    print("Error Select One")


if inputUser == "1":
    print("Enter Your Host")
    Hostname = input()
    try:
        CheckStatus()
        SubDomains()
    except socket.gaierror:
        print(Error, "Enter Valid Domain")
    except requests.exceptions.InvalidURL:
        print("Enter Valid Domain")
    except OSError:
        sys.exit()


if inputUser == "2":
    CheckStatusOfDomains()




