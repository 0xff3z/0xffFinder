import socket
import requests
import sys
import dns
import dns.resolver
import json
dnsResovler = dns.resolver.Resolver()
dnsResovler.timeout = 1
dnsResovler.lifetime = 1




import warnings
warnings.filterwarnings(action='ignore')







Error = '\033[91m'
Succses = '\033[92m'
Ports = [80,443,20,21,22,23,24,25,3306]

def CheckStatus():
    ip = socket.gethostbyname(f"{Hostname}")
    NewHost = (f"http://{Hostname}")
    status = requests.get(f"{NewHost}")
    StatusCode = status.status_code
    print(Succses + f" Domain :{Hostname} ", f"The ip is: {ip}: " f"Status: {StatusCode}..Ok ")
    for port in Ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)
        result = s.connect_ex((Hostname, port))
        if result == 0:
            Services = socket.getservbyport(port)
            print("=" * 50)
            print(f" Port {port} is Open",Services.format(port))
        else:
                print("=" * 50)
                print(Error, f"Port {port} is Closed")
                s.close()

def CheckStatusOfDomains():
    FileName = input("Locate Your Domains Lists :  For Example: Domains.txt ")
    with open(FileName,"r") as File:
        Lines = File.read()
        Lines = Lines.splitlines()
        for line in Lines:
           ip = socket.gethostbyname(f"{line}")
           NewHost = (f"http://{line}")
           status = requests.get(f"{NewHost}")
           StatusCode = status.status_code
           print(Succses + f" Domain :{line} ", f"The ip is: {ip}: " f"Status: {StatusCode}..Ok ")
           for port in Ports:
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               socket.setdefaulttimeout(0.2)
               result = s.connect_ex((line, port))
               if result == 0:
                   Services = socket.getservbyport(port)
                   print("=" * 50)
                   print(Succses,f" Port {port} is Open", Services.format(port))
               else:
                   print("=" * 50)
                   print(Error,f"Port {port} is Closed")
                   s.close()
           CheckEmail(line)
           CheckMXRec(line)
           CheckNSRec(line)
           CheckAAAARec(line)
           CheckARec(line)
           CheckCNAMERec(line)
           for sub in subdomains:
               url = f"http://{sub}.{line}"
               try:
                   requests.head(url,timeout=0.2)
                   print("="*50)
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
                print("=" * 50)
                print( Succses,"[+]Discovred Doamins:", url)
            except:
                ''



# def CheckEmail(Domain):
#     with open("emails.txt","r") as File:
#         Content = File.read()
#         Content = Content.splitlines()
#         for mails in Content:
#            isValid = validate_email(f'{mails}@{Domain}',smtp_timeout=10,  debug=False)
#         print(isValid)



def CheckMXRec(Domain):
    ResultMx = dnsResovler.query(Domain,"MX",raise_on_no_answer=False)
    for data in ResultMx:
        try:
         print("="*50)
         print( Succses, "[+]Discovred MX Record",data)
        except dns.resolver.query.NoAnswer:
            pass
        except:
            pass



def CheckARec(Domain):
    ResultA = dns.resolver.query(Domain,"A",raise_on_no_answer=False)
    for data in ResultA:
        try:
            print("=" * 50)
            print(Succses,"[+]Discovred A Record",data)
        except dns.resolver.query.NoAnswer:
            pass
        except:
            pass






def CheckNSRec(Domain):
    ResultCNAME = dns.resolver.query(Domain,"NS")
    for data in ResultCNAME:
        try:
            print("=" * 50)
            print(Succses,"[+]Discovred NS Record",data)
        except dns.resolver.query.NoAnswer:
            pass
        except:
            pass


def CheckAAAARec(Domain):
    ResultAAAA = dns.resolver.query(Domain,"AAAA",raise_on_no_answer=False)
    for data in ResultAAAA:
        try:
            print("=" * 50)
            print(Succses,"[+]Discovred AAAA Record",data)
        except dns.resolver.queryr.NoAnswer:
            pass
        except KeyError:
            ''



def CheckCNAMERec(Domain):
    ResultCNAME= dns.resolver.query(Domain,"CNAME",raise_on_no_answer=False)
    for data in ResultCNAME:
        try:
            print("=" * 50)
            print(Succses,"[+]Discovred CNAME Record",data)
        except dns.resolver.query.NoAnswer:
            pass
        except:
            pass


def CheckEmail(Domain):
    with open("emails.txt", "r") as File:
        Lines = File.read()
        Lines = Lines.splitlines()
        for line in Lines:
            params = {
                'access_key': 'ed5679bd98e1e3b38f6a03e4bbba510d',
                'email': f'{line}@{Domain}'
            }
            Res = requests.get(f"http://apilayer.net/api/check?",params)
            Response = Res.json()
            print("="*50)
            print(Succses,"Email : ",Response["email"])
            print(Succses,"FormatValid? :",Response["format_valid"])
            print(Succses,"MX Found ?",Response["mx_found"])
            print(Succses,"SMTP Check ? :",Response["smtp_check"])




# def CheckZone(Domain):
#     ResultZone = dns.zone.from_xfr(dns.query.xfr(Domain))
#     for data in ResultZone:1

#         try:
#             print(Succses," [+]Discovred AAAA Record",data)
#         except DNSException as e:
#             print(e)
#



def CheckDNSRec():
    CheckEmail(Hostname)
    CheckMXRec(Hostname)
    CheckARec(Hostname)
    CheckNSRec(Hostname)
    CheckAAAARec(Hostname)
    CheckCNAMERec(Hostname)

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
        print("=" * 50)
        print(Succses," DNS Records :")
        CheckDNSRec()
        SubDomains()
    except KeyboardInterrupt:
        print(Error, "Canceled By User")

    except socket.gaierror:
        print(Error, "Enter Valid Domain")
    except requests.exceptions.InvalidURL:
        print("Enter Valid Domain")
    except OSError:
        sys.exit()


if inputUser == "2":
    try:
      CheckStatusOfDomains()
    except KeyboardInterrupt :
        print(Error,"Canceled By User")



