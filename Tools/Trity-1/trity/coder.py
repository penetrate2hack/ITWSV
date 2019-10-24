#!/usr/bin/python
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
def encode():
    Str = raw_input(''+T+'' + color.UNDERLINE + 'String to encode>' + color.END)
    Str = Str.encode('base64','strict');
    print ""+G+"Encoded: " + Str
def decode():
    Str = raw_input(''+T+'' + color.UNDERLINE + 'String to decode>' + color.END)
    Str = Str.decode('base64','strict');
    print ""+G+"Decoded String: " + Str