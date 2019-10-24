import random, string, smtplib
from time import sleep
from getpass import getpass
from subprocess import call

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

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan  
def sms():
        print ""+T+" "
	print "Put the @ sign before the provider"
        provider = raw_input(color.UNDERLINE + 'Enter cellular provider>' + color.END)
        print ""+T+" "
	phone_num = raw_input(color.UNDERLINE + 'Victims phone number>' + color.END) + provider
        print ""+T+" "
	gmail = raw_input(color.UNDERLINE + 'Your email>' + color.END)
        print ""+T+" "
	password = getpass(color.UNDERLINE + 'Password>' + color.END)

        o = smtplib.SMTP("smtp.gmail.com:587")
        o.starttls()
        o.login(gmail, password)

	message = raw_input(color.UNDERLINE + 'Message>' + color.END)
        print ""+T+" "
	counter = input(color.UNDERLINE + 'How many times>' + color.END)
        print ""+T+" "
        spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(gmail, phone_num, message)
	print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
        for i in range(counter):
            o.sendmail(gmail, phone_num, spam_msg)
        sleep(0.1)
	print (color.UNDERLINE + ''+G+'[*] Successfully sent!' + color.END)