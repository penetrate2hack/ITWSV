#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

from urllib2 import Request, urlopen, URLError, HTTPError
def admin():
    def Space(j):
	    i = 0
	    while i<=j:
		    print " ",
		    i+=1


    def findAdmin():
	    f = open("link.txt","r");
	    link = raw_input(T + color.UNDERLINE + 'Site>' + color.END)
	    print "\n\nAvailable links : \n"
	    print ""+G+"[*] "+W+"Scanning..."
	    while True:
                    time.sleep(0.5)
		    sub_link = f.readline()
		    if not sub_link:
			    break
		    req_link = "http://"+link+"/"+sub_link
		    req = Request(req_link)
		    try:
			    response = urlopen(req)
		    except HTTPError as e:
			    continue
		    except URLError as e:
			    continue
		    else:
			    print ""+G+"Available -> "+W+"",req_link
    findAdmin()
