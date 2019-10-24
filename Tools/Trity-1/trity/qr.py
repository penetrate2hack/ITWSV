# coding=utf-8
import os
import time
import qrcode
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
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta

def gen_qrcode():
    url = raw_input(''+T+'' + color.UNDERLINE + 'Website or text>' + color.END)
    print ""+C+"Enter the name of the output file without the extension"
    name = raw_input(''+T+'' + color.UNDERLINE + 'Output>' + color.END)
    qr = qrcode.QRCode(5, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(url)
    qr.make()
    im = qr.make_image()
    time.sleep(1)

    qr_img_path = os.path.join(name + ".png")

    if os.path.isfile(qr_img_path):
        os.remove(qr_img_path)
    # save the image out
    im.save(qr_img_path, format='png')
    # print that its been successful
    print(""+G+"[!] " + color.UNDERLINE + "QRCode has been generated!" + color.END)