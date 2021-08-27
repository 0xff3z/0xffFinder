import socket
import requests
import sys
import re
import dns.query
import dns.zone
import dns.resolver
from dns.exception import DNSException

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'







Error = '\033[91m'
Succses = '\033[92m'
Ports = [80,443,20,21,22,23,24,25,3306]

def CheckStatus():
    ip = socket.gethostbyname(f"{Hostname}")
    NewHost = (f"http://{Hostname}")
    status = requests.get(f"{NewHost}")
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
           status = requests.get(f"{NewHost}")
           StatusCode = status.status_code
           print(Succses + f"Domain :{line} ", f"The ip is: {ip}: " f"Status: {StatusCode}..Ok ")
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
           CheckMXRec(line)
           CheckNSRec(line)
           CheckAAAARec(line)
           CheckARec(line)
           for sub in subdomains:
               url = f"http://{sub}.{line}"
               try:
                   requests.head(url,timeout=0.2)
                   print(Succses, "[+]Discovred Doamins:", url)
               except:
                   ''



file = open("subDomains.txt","r")
contentInFile = file.read()
subdomains = contentInFile.splitlines()
def SubDomains():
        for sub in subdomains:
            url = f"http://{sub}.{Hostname}"
            try:
                requests.head(url,timeout=0.2)
                print( Succses,"[+]Discovred Doamins:", url)
            except:
                ''



def CheckEmail():
    with open("emails.txt","r") as File:
        Content = File.read()
        Content = Content.splitlines()
        for mails in Content:
            if re.search(regex,f"{mails}{Hostname}"):
                print(mails,Hostname,"Valid Email")
            else:
                print(Error,mails,"Invalid")



def CheckMXRec(Domain):
    ResultMx = dns.resolver.query(Domain,"MX")
    for data in ResultMx:
        try:
         print( Succses, "[+]Discovred MX Record",data)
        except DNSException as e:
         print(e)

def CheckARec(Domain):
    ResultA = dns.resolver.query(Domain,"A")
    for data in ResultA:
        try:
            print(Succses," [+]Discovred A Record",data)
        except DNSException as e:
            print(e)


def CheckNSRec(Domain):
    ResultCNAME = dns.resolver.query(Domain,"NS")
    for data in ResultCNAME:
        try:
            print(Succses," [+]Discovred NS Record",data)
        except DNSException as e:
            print(e)

def CheckAAAARec(Domain):
    ResultAAAA = dns.resolver.query(Domain,"AAAA")
    for data in ResultAAAA:
        try:
            print(Succses," [+]Discovred AAAA Record",data)
        except DNSException as e:
            print(e)


# def CheckZone(Domain):
#     ResultZone = dns.zone.from_xfr(dns.query.xfr(Domain))
#     for data in ResultZone:
#         try:
#             print(Succses," [+]Discovred AAAA Record",data)
#         except DNSException as e:
#             print(e)
#





def CheckDNSRec():
    CheckMXRec(Hostname)
    CheckARec(Hostname)
    CheckNSRec(Hostname)
    CheckAAAARec(Hostname)
    # CheckZone(Hostname)

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
        print("DNS Records")
        CheckDNSRec()
        SubDomains()

    except socket.gaierror:
        print(Error, "Enter Valid Domain")
    except requests.exceptions.InvalidURL:
        print("Enter Valid Domain")
    except OSError:
        sys.exit()


if inputUser == "2":
    CheckStatusOfDomains()


