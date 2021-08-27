import socket
import requests


print("Enter Your Target")
host = input()

ip = socket.gethostbyname(f"{host}")
newhost = (f"http://{host}")
status = requests.get(f"{newhost}")


print(ip,status)

