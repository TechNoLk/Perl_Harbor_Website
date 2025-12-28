import subprocess
import optparse

def parseValue():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="enter interface ID")
    parse.add_option("-m","--mac",dest="macAddress",help="change mac address")
    return parse.parse_args()

def macChange(interface, macAddress):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",macAddress])
    subprocess.call(["ifconfig",interface,"up"])

(op,ar) = parseValue()
macChange(op.interface,op.macAddress)
 