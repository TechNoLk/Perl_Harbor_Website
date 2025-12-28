import scapy.all as scappy

def ipadd():
    ip = input("Enter Network Range : ")
    return scappy.arping(ip)

ipadd()
