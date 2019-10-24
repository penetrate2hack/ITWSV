import zipfile

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

def zipfile():
	print ""+C+"Files have to be in the same directory - Include .zip or .txt"
	zipfilename = raw_input(''+T+'' + color.UNDERLINE + 'Zip file>' + color.END)
	dictionary = raw_input(''+T+'' + color.UNDERLINE + 'Dictionary file>' + color.END)
	print (""+G+"[*] "+W+"Cracking...")
	password = None
	zip_file = zipfilename
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zip_file.extractall(pwd=password)
				password = 'Password found: %s' % password
			except:
				pass
	print ""+G+"[!] "+W+"Password found: " + password
