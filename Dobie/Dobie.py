import socket
import platform
import os
from scapy.all import traceroute, ICMP

def ip_parser(ip: str)->list:
    pass

if __name__=="__main__":
    print("Welcom to Dobie!\n(sniff sniff...)\nWhat website you want to go with safety route path?")
    ip=socket.gethostbyname(input("(input the link): "))
    print(f"Ok, lets trace the path from {ip}...")
    if platform.system()=="Windows":
        os.system(f"tracert {ip} > ./routers.txt")
    else:
        os.system(f"traceroute {ip} > ./routers.txt")

    f = open("routers.txt", "r")
    for x in f:
        print(x)
    f.close()



    os.remove("./routers.txt")