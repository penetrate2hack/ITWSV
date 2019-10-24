import os
import sys
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
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
def spoofemail():
     fromm = raw_input(''+T+'' + color.UNDERLINE + 'From name>' + color.END)
     emaill = raw_input(''+T+'' + color.UNDERLINE + 'From email>' + color.END)
     too = raw_input(''+T+'' + color.UNDERLINE + 'To email>' + color.END)
     subject = raw_input(''+T+'' + color.UNDERLINE + 'Subject>' + color.END)
     isp = raw_input(''+T+'' + color.UNDERLINE + 'Your isp>' + color.END)
     print C + "Type your message here, and when your done, press Ctrl-d." + W
     os.system('sendEmail -f "' + fromm + '<' + emaill + '>" -t ' + too + ' -u "' + subject + '" -s ' + isp)