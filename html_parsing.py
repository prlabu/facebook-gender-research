import json
import datetime
import csv
import time
import re
from HTMLParser import HTMLParser

# I first intended to use an API to scrape data from the facebook api, but it only allows data to be gathered from open groups. As the Rice facebook groups are generally closed, I am getting data manually by downloading an HTML file (ew) and parsing it with a module called BeautifulSoup, which queries and traverses the html file. 

# Originally, my idea was to go through the Rice Facebook groups, analysing posts with respect to gender. I was not exactly sure how I was going to deal with gender because Facebook currently provides options for "Female", "Male", and "Custom", which provides more than 50 options for gender. I planned to experiment with the data on post length, basic post content, and number reactions. At first, I encountered problems with permissions, but kept working to get around them - because it's usually possible. 

# Becoming familiar with the Facebook API took a fair amount of time, especially figuring out which access tokens permitted which types of data. I created a separate account with an app called "Gender in Rice Facebook Groups" that allows basic interaction with the API. However, this type of setup usually requires the user to grant permission to an application to access fields in their profile.

# I considered simply going to an open group, like "CNN," and getting the comments from users, and then retreiving gender from their profile page. I could go manually and look at a user's gender, but when I tried to automotize it with the Facebook API, permissions were denied. Thus, it seems that I have to be friends with a user to retrieve their gender.  

# Given this information, I am now going to gather data from my own Facebook feed and run gendered analyses on it. I hope to pass the script on/allow people to run it from their accounts to allow people to better understand gender affects their facebook. 

# After doing a bit more research, it turns out that I cannot even retrieve the data of my friends and their posts. I am limited to my friends who have installed the Facebook Graph API Explorer, or a similar app that grants permission to Facebook 

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






