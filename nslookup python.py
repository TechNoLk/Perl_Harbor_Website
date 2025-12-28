import subprocess
import optparse

def arguments():
    parse = optparse.OptionParser()
    parse.add_option("-n", "--ns" , dest="ipadd",help="nslookup")
    return parse.parse_args()

def process(ipadd):
    subprocess.call(["nslookup",ipadd])

(op,ar) = arguments()
process(op.ipadd)
