import json
import datetime
import csv
import time
import re
from HTMLParser import HTMLParser



class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        flag = 'aria-label'
        if (flag in list(map(lambda attr: attr[0], attrs))):
            pass
    
    def handle_data(self, data):
        if (data == 'News Feed'):
            print 'news feed found'
    

parser = MyHTMLParser()
try:
    f = open('2120fb-page.html')
    html = f.read()
    parser.feed(html)
except Exception as e:
    print e


print "wow still running"






