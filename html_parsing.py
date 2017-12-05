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

# After doing a bit more research, it turns out that I cannot even retrieve the data of my friends and their posts. I am limited to my friends who have installed the Facebook Graph API Explorer, or a similar app that grants permission to Facebook.

# I am now considering simply doing a survey of current research regarding gender in Facebook pages. This is no nearly as interesting as investigating on my own, but the Facebook API won't allow the retrieval of gender. 

# I came across Wolfram|Alpha, and saw their tools to investigate analyze your Facebook information. This was attractive to me in that I thought it would be a great way to attract people - if they can visualize their own data, they might be able to see the potential of gender research. 

# I wanted to do the same thing - create an app that requests the information from a user in the same way most FB applications do. As I thought about how I would request this information from my friends, I realized a website displaying information relevant to the study would be nice to have, and probably ensure credibility for friends who may doubt the request. Thus, I went through the whole process of creating a webpage, prlabu.github.io (hosted by GitHub) that integrated the "Facebook login" for users. In this way, I imagined that the Facebook post would redirect to this page, and friends could grant permission to the application "Gender on Social Media Research." After permission was granted, I planned to do simple tests on post length, post frequency, and number of likes with gender as the baseline. 

# After testing with some family members, I realized that the application only granted 'public profile' information like age range, name, profile picture, and gender. I expected the change to be as simple as changing the application configuration to request more information from a user when the user logs in/grants permission. However, it turns out Facebook requires that you submit a proposal for every extra piece of information that your application requires - developers must provide screenshots explicitly revealing how their application uses the users' information. The guidelines state that applications must not use the information for purposes that don't directly benefit the user (such as creating targetted ads); because the nature of my 'application' is research, I intend to use the information exactly how Facebook restricts it. 

# Another approach that I explored is asking friends and family to approve the "Facebook Graph API Explorer", which is more tailored to simple exploration as opposed to a commercialized application that the regular API lends itself well to. The problem with this approach is that it is not straightforward. The Explorer is made for developers, and it's not obvious how to grant permission to this application. Because of this, it is difficult to post on mass media. It would result in more frustration than anything, which I tested with family. This was indeed the case. 

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






