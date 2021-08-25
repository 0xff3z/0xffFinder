import socket
import requests
Error = '\033[91m'
Succses = '\033[92m'

print("Select One")
inputUser = input('''
1 - One Domain
2 - Comming Soon Multiple Domains
''')

if inputUser == "":
    print("Error Select One")

if inputUser == "1":
    print("Enter Your Host")
    hostname = input()
    ip = socket.gethostbyname(f"{hostname}")
    newhost = (f"http://{hostname}")
    status = requests.get(f"{newhost}")
    statuscode = status.status_code
    if statuscode == 200:
        socket.gethostbyname(f"{hostname}")
        requests.get(f"{newhost}")
        print(Succses, f"Domain: {newhost}", " == ", f"The ip is : {ip}" " == ", f"Status ..Ok {statuscode}")
    else:
        print(Error, f"Domain: {ip}", " == ", f"The ip is : {ip}" " == ", f"Status ..Error {statuscode}")

if inputUser == "2":
    filepath = "Domains.txt"
    certpath = 'cert.pem'
    with open(filepath) as file:
        text = file.read()
        text = text.splitlines()

        for i in text:
            prograss = i
            ip = i.split()[0]
            ip = socket.gethostbyname(f"{ip}")
            newhost = (f"http://{ip}")
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
            }
            session = requests.Session()
            status = requests.get(f"{newhost}", headers=headers)
            statuscode = status.status_code
            if statuscode == 200:
                session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
                socket.gethostbyname(f"{ip}")
                requests.get(f"{newhost}", headers=headers)
                print(Succses, "Domain:", f"{prograss}", f" And The ip is : {ip}" " == ", f"Status ..Ok {statuscode}")
            else:
                print(Error, f"Domain: {prograss}",  f" And The ip is : {ip}" " == ", f"Status ..Error {statuscode}")
                file.close()
