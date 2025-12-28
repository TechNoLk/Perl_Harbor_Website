import scapy.all as scapy

import optparse

def values():
    parse = optparse.OptionParser()
    parse.add_option("-i","--ipaddress",dest="ip",help="Enter IP Address and subnet marsk")
    return parse.parse_args()

def mainprogramme(ip):
    scapy.arping(ip)

(option,arg) = values()
mainprogramme(option.ip)
