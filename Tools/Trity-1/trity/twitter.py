#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup as So
import urllib ,sys
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
   ENDC = '\033[0m'
def twitter():
    def get(twitter):
        try:
            u = urllib.urlopen(twitter)
            data = u.read()
            s = So(data, 'html.parser')
            details = s.find_all("span" ,{"data-is-compact":"false"})
            following = details[1].text.encode("utf-8")
            name = s.find("a" ,{"href":"/"+twitter.split("/")[-1]}).text.encode("utf-8").replace("  ","").replace("\n","")
            followers = details[2].text.encode("utf-8")
            likes = details[3].text.encode("utf-8")
            pic = s.find("a" ,{"class":"ProfileAvatar-container u-block js-tooltip profile-picture"})["href"].encode("utf-8")
            date = s.find("span" ,{"class":"ProfileHeaderCard-joinDateText js-tooltip u-dir"})["title"].encode("utf-8")
            print G + " Name: " + W + name
            print G + " Following: " + W + following
            print G + " Followers: " + W + followers
            print G + " Likes: " + W + likes
            print G + " This Account was made on: " + W + date
            print G + " Full Profile Picture: " + W + pic
        except:
            print R + "Error <Twitter_Profile_link>/<username> is not correct"
            sys.exit(0)


    u = raw_input(''+T+'' + color.UNDERLINE + 'Username>' + color.END)



    if "twitter.com" not in u:
        get("https://twitter.com/" + u)
    else:
        get(u)
