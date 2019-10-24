import pythonwhois  # i'm using this http://cryto.net/pythonwhois
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

def whoisweb():
    print(''+R+'Example - example.com')
    h = raw_input(''+T+'' + color.UNDERLINE + 'Website>' + color.END)
    domains = [h]
    for dom in domains:
        details = pythonwhois.get_whois(dom)
        print details['contacts']['registrant'] 