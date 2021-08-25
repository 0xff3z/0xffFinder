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

        print(Succses + ip, " Status ", statuscode)

    else:

        print(statuscode + "  Not Found ")



if inputUser == "2":

    filepath = "Domains.txt"

    with open(filepath) as file:

        text = file.read()

        text = text.splitlines()

        for i in text:

            ip = i.split()[0]

            ip = socket.gethostbyname(f"{ip}")

            newhost = (f"http://{ip}")

            status = requests.get(f"{newhost}")

            statuscode = status.status_code

            if statuscode == 200:

                print(Succses + ip, " Status ", statuscode)

            else:

                print(Error ,  statuscode ,"  Not Found ")

                sys.tracebacklimit = 0

                file.close()
