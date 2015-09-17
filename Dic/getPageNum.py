﻿# coding: UTF-8 
import socket
import urllib2
import traceback
#import MySQLdb
import time
from bs4 import BeautifulSoup
#from complainDetail import *

timeout = 10
socket.setdefaulttimeout(timeout)
import index


if __name__ == "__main__":
    pageNum = {}
    for i in index.kanaAlpha:
        #indexUrl = "http://www.weblio.jp/category/dictionary/nhgkt/di"
        f = urllib2.urlopen(i)
        content = f.read()        
        soup = BeautifulSoup(content)
        urlTable = soup.find(attrs={'class':'CtgryPgNIE'})
        if(urlTable==None):
            print i,1
            pageNum[i] = 1
            time.sleep(1)
            continue
        aList = urlTable.find_all('a')
        pageNum[i] = aList[-2].string
        print i,pageNum[i]
        time.sleep(1)
    print pageNum
    
