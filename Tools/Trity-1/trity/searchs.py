import search_google
class color:
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   ENDC = '\033[0m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
def googleSearch():
    lol = raw_input(color.UNDERLINE + ""+T+"Query>" + color.END)
    for url in search(lol, tld='com', lang='es', stop=50):
        print(""+G+"Site: "+W+"" + url)
