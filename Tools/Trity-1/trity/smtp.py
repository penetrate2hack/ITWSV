import sys, platform, time, os, urllib
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

############################################################################
def smtp():
    attack = '@gmail.com'
    phone_num = raw_input(color.UNDERLINE + ''+T+'Victims email>' + color.END) + str(attack)
    gmail = raw_input(color.UNDERLINE + ''+T+'Your Email>' + color.END)
    password = getpass((color.UNDERLINE + ''+T+'Password>' + color.END))

    o = smtplib.SMTP("smtp.gmail.com:587")
    o.starttls()
    o.login(gmail, password)
    subject = raw_input(color.UNDERLINE + ''+T+'Subject>' + color.END)
    message = raw_input(color.UNDERLINE + ''+T+'Message to send>' + color.END)
    counter = input(color.UNDERLINE + ''+T+'How many times>' + color.END)
    spam_msg = "From: {} \r\nTo: {} \r\nSubject: {} \r\n\r\n {}".format(gmail, phone_num, subject, message)

    sleep(1)
    print ""+G+"[*] Sending..."
    for i in range(counter):
        o.sendmail(gmail, phone_num, spam_msg)
    print ''+G+'[*] Success! Emails Sent! '+W+''
