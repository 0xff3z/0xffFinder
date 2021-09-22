import random
import re
import socket
import requests
import sys
import dns
import dns.resolver
import dns.zone
import json
import threading
import builtwith
import ssl
import mechanize





Error = '\033[91m'
Succses = '\033[92m'
white = '\037[95m'
orange = "\033[0;33m"

dnsResovler = dns.resolver.Resolver()
dnsResovler.timeout = 1
dnsResovler.lifetime = 1

import warnings

warnings.filterwarnings(action='ignore')

ApiList = ["8ce4daa49a6d58deeeb26834278a295a", "ed5679bd98e1e3b38f6a03e4bbba510d", "32f5add10d2edab7c76440de0fe3b069"]

ApiList = random.choice(ApiList)


print('''

  .oooo.                .o88o.  .o88o. oooooooooooo  o8o                    .o8                     
 d8P'`Y8b               888 `"  888 `" `888'     `8  `"'                   "888                     
888    888 oooo    ooo o888oo  o888oo   888         oooo  ooo. .oo.    .oooo888   .ooooo.  oooo d8b 
888    888  `88b..8P'   888     888     888oooo8    `888  `888P"Y88b  d88' `888  d88' `88b `888""8P 
888    888    Y888'     888     888     888    "     888   888   888  888   888  888ooo888  888     
`88b  d88'  .o8"'88b    888     888     888          888   888   888  888   888  888    .o  888     
 `Y8bd8P'  o88'   888o o888o   o888o   o888o        o888o o888o o888o `Y8bod88P" `Y8bod8P' d888b



=======================
Version: V1.5.1
Developer => Abdualziz Alosaimi - 0xff3z
DeveloperAccounts =>
Twitter: 0xff3z

''')







def CheckStatus():
    ip = socket.gethostbyname(f"{Hostname}")
    NewHost = (f"http://{Hostname}")
    status = requests.get(f"{NewHost}")
    StatusCode = status.status_code
    serverreq = status.headers
    res = serverreq.get("Server")
    WebTech = builtwith.parse(f"{NewHost}")
    print(Succses + f" Domain :{Hostname} ", f"The ip is: {ip}: " f"Status: {StatusCode}..Ok ")
    print("=" * 50)
    print(" Web Technolgy : ")
    print(Succses, "Server : ", res)
    print(" Programming Language : ",WebTech.get("programming-languages"))
    print(" Cms :",WebTech.get("cms"))
    print(" JavaScript Framework :", WebTech.get("javascript-frameworks"))
    print("=" * 50)
    print("XSS Check :")
    # XSSCheck(Hostname)
    print("=" * 50)
    print(" TLS Version :")
    CheckSSLAndTLS(Hostname)
    print("=" * 50)
    GetLocatinoIp(ip)
    for port in TopPorts:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        result = s.connect_ex((Hostname, port))
        try:
         if result == 0:
            Services = socket.getservbyport(port)
            print("\033[01;37m=" * 50, "\033[01;32m")
            print(Succses,f" Port {port} is Open", Services.format(port))
        except OSError:
            pass
        except:
         s.close()



def CheckSSLAndTLS(Host):
    Host = Host
    Res = ssl.SSLContext()
    try:
     with socket.create_connection((Host, 443)) as sock:
        with Res.wrap_socket(sock,server_hostname=Host) as ssock:
            print("",ssock.version())
    except:
        pass

FileTopPorts = open("PayLoads/top100Ports.txt",'r')
TopPorts = FileTopPorts.read().splitlines()


for i in range(0,len(TopPorts)):
    TopPorts[i] = int(TopPorts[i])



def CheckStatusOfDomains():
    print("\033[0;33m")
    FileName = input("Locate Your Domains Lists :  For Example: Domains.txt ")
    with open(FileName, "r") as File:
        Lines = File.read()
        Lines = Lines.splitlines()
        for line in Lines:
            ip = socket.gethostbyname(f"{line}")
            NewHost = (f"http://{line}")
            status = requests.get(f"{NewHost}")
            StatusCode = status.status_code
            serverreq = status.headers
            WebTech = builtwith.parse(f"{NewHost}")
            res = serverreq.get("Server")
            print(Succses + f" Domain :{line} ", f"The ip is: {ip}: " f"Status: {StatusCode}..Ok ")
            GetLocatinoIp(ip)
            print("=" * 50)
            print(" Web Technolgy : ")
            print(Succses, "Server : ", res)
            print(" Programming Language : ", WebTech.get("programming-languages"))
            print(" Cms :", WebTech.get("cms"))
            print(" JavaScript Framework :", WebTech.get("javascript-frameworks"))
            try:
             for port in TopPorts:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(2)
                    result = s.connect_ex((line, port))
                    if result == 0:
                        Services = socket.getservbyport(port)
                        print("\033[01;37m=" * 50, "\033[01;32m")
                        print(Succses, f" Port {port} is Open", Services.format(port))
            except OSError:
                pass
            except:
                s.close()
            CheckMXRec(line)
            CheckNSRec(line)
            CheckAAAARec(line)
            CheckARec(line)
            CheckCNAMERec(line)
            ZoneTransfer(line)
            CheckEmail(line)
            print("  Disallow From robots.txt :")
            HiddinDir(line)
            print("=" * 50)
            CheckDir(line)
            SubDomains(line)




file = open("PayLoads/subDomains.txt", "r")
contentInFile = file.read()
subdomains = contentInFile.splitlines()


def SubDomains(Domain):
    for sub in subdomains:
        try:
            url = "http://" + sub + "." + Domain
            req = requests.get(url, )
            if req.status_code == 200:
                print("\033[01;37m=" * 50, "\033[01;32m")
                print(Succses, "[+]Discovred Sub Doamins:", url)
        except:
            pass


def CheckMXRec(Domain):
    ResultMx = dnsResovler.query(Domain, "MX", raise_on_no_answer=False)
    for data in ResultMx:
        try:
            print("\033[01;37m=" * 50, "\033[01;32m")
            print(Succses, "[+]Discovred MX Record", data)
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.Timeout:
            pass
        except dns.resolver.NoNameservers:
            pass
        except dns.resolver.NotAbsolute:
            pass
        except dns.resolver.NoMetaqueries:
            pass
        except dns.resolver.NoRootSOA:
            pass
        except:
            pass


def CheckARec(Domain):
    ResultA = dns.resolver.query(Domain, "A", raise_on_no_answer=False)
    for data in ResultA:
        try:
            print("\033[01;37m=" * 50, "\033[01;32m")
            print(Succses, "[+]Discovred A Record", data)
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.Timeout:
            pass
        except dns.resolver.NoNameservers:
            pass
        except dns.resolver.NotAbsolute:
            pass
        except dns.resolver.NoMetaqueries:
            pass
        except dns.resolver.NoRootSOA:
            pass
        except:
            pass


def CheckNSRec(Domain):
    ResultNsNAME = dns.resolver.query(Domain, "NS", raise_on_no_answer=False)
    for data in ResultNsNAME:
        try:
            print("\033[01;37m=" * 50, "\033[01;32m")
            print(Succses, "[+]Discovred NS Record", data)
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.Timeout:
            pass
        except dns.resolver.NoNameservers:
            pass
        except dns.resolver.NotAbsolute:
            pass
        except dns.resolver.NoMetaqueries:
            pass
        except dns.resolver.NoRootSOA:
            pass
        except:
            pass




def ZoneTransfer(Domain):
    try:
     print("=" * 50)
     print(" Transferred Zone :")
     SOA= dns.resolver.query(Domain,"SOA")
     Res = dns.resolver.query(SOA[0].mname,"A")
     zone = dns.zone.from_xfr(dns.query.xfr(Res[0].address, Domain))
     for n in sorted(zone.nodes.keys()):
        print(" Zones : ",zone[n].to_text(n))
    except dns.zone.BadZone:
        print(Error,"Zone Transfer Failed")
    except dns.exception.FormError:
        print(Error,"Zone Transfer Failed")
    except dns.zone.NoNS:
        pass
    except dns.zone.NoAnswer:
        pass
    except dns.zone.Timeout:
        pass
    except dns.zone.NoNameservers:
        pass
    except dns.zone.NotAbsolute:
        pass
    except dns.zone.NoMetaqueries:
        pass
    except dns.zone.NoRootSOA:
        pass
    except:
        pass







def CheckAAAARec(Domain):
    ResultAAAA = dns.resolver.query(Domain, "AAAA", raise_on_no_answer=False)
    for data in ResultAAAA:
        try:
            print("\033[01;37m=" * 50, "\033[01;32m")
            print(Succses, "[+]Discovred AAAA Record", data)
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.Timeout:
            pass
        except dns.resolver.NoNameservers:
            pass
        except dns.resolver.NotAbsolute:
            pass
        except dns.resolver.NoMetaqueries:
            pass
        except dns.resolver.NoRootSOA:
            pass
        except:
            pass


def CheckCNAMERec(Domain):
    ResultCNAME = dns.resolver.query(Domain, "CNAME", raise_on_no_answer=False)
    for data in ResultCNAME:
        try:
            print("\033[01;37m=" * 50, "\033[01;32m")
            print(Succses, "[+]Discovred CNAME Record", data)
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.Timeout:
            pass
        except dns.resolver.NoNameservers:
            pass
        except dns.resolver.NotAbsolute:
            pass
        except dns.resolver.NoMetaqueries:
            pass
        except dns.resolver.NoRootSOA:
            pass
        except:
            pass


def CheckEmail(Domain):
    with open("PayLoads/emails.txt", "r") as File:
        Lines = File.read()
        Lines = Lines.splitlines()
        for line in Lines:
            params = {
                'access_key': f'{ApiList}',
                'email': f'{line}@{Domain}'
            }
            Res = requests.get(f"http://apilayer.net/api/check?", params)
            Response = Res.json()
            print("\033[01;37m=" * 50, "\033[01;32m")
            print(Succses, "Email : ", Response["email"])
            print(Succses, "FormatValid? :", Response["format_valid"])
            print(Succses, "MX Found ?", Response["mx_found"])
            print(Succses, "SMTP Check ? :", Response["smtp_check"])


DirFilePath = open("PayLoads/DirList.txt", "r")
ContentDir = DirFilePath.read()
Dir = ContentDir.splitlines()


def CheckDir(Domain):
    try:
        for res in Dir:
            url = f"http://{Domain}/{res}"
            req = requests.get(url,allow_redirects=False)
            if req.status_code == 200:
                print(Succses, "[+] Found :", url)
    except:
        pass



def HiddinDir(Domain):
    FullDomain = f"http://{Domain}/robots.txt"
    try:
        req = requests.get(FullDomain,"html.parser").text
        Hidden = re.findall("Disallow\: \S{1,}",req)
        for i in Hidden:
            link = "[+]"+Domain+i[10:]
            print(link)
    except:
        pass


def GetLocatinoIp(Ip):
    ipApi = f'http://ip-api.com/json/{Ip}'
    req = requests.get(ipApi).json()
    print(Succses,"Countery : ",req["country"])
    print(Succses,"City : ",req["city"])
    print(Succses,"ISP :",req["isp"])
    print(Succses,"Lat :",req["lat"])
    print(Succses,"Lon :",req["lon"])

XSSPayLoads = open("PayLoads/XSSPayloads.txt", "r")
ContentXSS = XSSPayLoads.read()
XSS = ContentXSS.splitlines()













def CheckDNSRec(Domain):
    CheckMXRec(Domain)
    CheckARec(Domain)
    CheckNSRec(Domain)
    CheckAAAARec(Domain)
    CheckCNAMERec(Domain)
    # CheckEmail(Domain)
    ZoneTransfer(Domain)
    print("=" * 50)






inputUser = input(''' 
---------------------------------------------- 

\033[01;34m [1] \033[01;33m One Domain 
\033[01;34m [2] \033[01;33m Multiple Domains 
\033[01;34m [3] \033[01;33m Exit 

choose the options -)> \033[01;31m''')

if inputUser == "":
    print("Error Select One")

if inputUser == "1":
    Hostname = input("\n \033[01;33mEnter The Host \033[01;37m( \033[01;34mex : example.com \033[01;37m)-)> ")
    try:
        print("=" * 50)
        t1 = threading.Thread(target=CheckStatus())
        t1.start()
        print(Succses, " DNS Records :")
        t2 = threading.Thread(target=CheckDNSRec(Hostname))
        t2.start()
        t2.join()
        print(Succses,"Disallow From robots.txt :")
        t3 = threading.Thread(target=HiddinDir(Hostname))
        t3.start()
        t3.join()
        print("=" * 50)
        print(" Admin Directory :")
        t4 = threading.Thread(target=CheckDir(Hostname))
        t4.start()
        t4.join()
        print("=" * 50)
        t5 = threading.Thread(target=SubDomains(Hostname))
        t5.start()
        t5.join()

    except KeyboardInterrupt:
        print(Error, "Canceled By User")
        exit()
    except socket.gaierror:
        print(Error, "Enter Valid Domain")
    except requests.exceptions.InvalidURL:
        print("Enter Valid Domain")
    except OSError:
        sys.exit()






elif inputUser == "2":
    try:
        CheckStatusOfDomains()
    except KeyboardInterrupt:
        print(Error, "Canceled By User")
        exit()
elif inputUser == "3":
    print(orange,"_" * 60)
    exit(" \n \033[0;33m                    Thanks To Using My Tool")