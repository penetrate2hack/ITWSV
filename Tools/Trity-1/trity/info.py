import os, io, platform, sys, socket
from time import sleep
from urllib2 import urlopen

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan 

mac_address = os.popen("cat /sys/class/net/eth0/address").read()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
localaddr = s.getsockname()[0] # local subnet
ipaddr = urlopen('http://ip.42.pl/raw').read()
def_gw_device = os.popen("route | grep '^default' | grep -o '[^ ]*$'").read()

def info():
    print ""+W+"+--------------------------+"
    print "|"+C+" Mac Address: " + mac_address + ""+W+"+--------------------------+"
    print "|"+R+" Local address: " + localaddr
    print ""+W+"+--------------------------+"
    print "|"+G+" IP: " + ipaddr
    print ""+W+"+--------------------------+"
    print "|"+T+" Operating System: " + platform.system()
    print ""+W+"+--------------------------+"
    print "|"+P+" Name: " + platform.node()
    print ""+W+"+--------------------------+"
    print "|"+O+" Interface: " + def_gw_device +W+"+--------------------------+"
