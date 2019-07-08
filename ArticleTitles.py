#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Topics: libraries, requests, beautifulsoup
"""
# download package - requests
# usually packages will have .py files
import requests
from bs4 import BeautifulSoup # bs4 is a package, BeautifulSoup is a class in bs4

# make a request, website sends response
url = 'https://www.nytimes.com/'
r = requests.get(url)
print(r) # <Response [200]> status code 200 --> OK


# get content
r_html = r.text # inside the variable r_html, you have the HTML of the page as a string
print(r_html)

# To read/parse, use BeautifulSoup package
soup = BeautifulSoup(r_html)

#stories = soup.find_all(class_="balancedHeadline") # returns a list of all tags with balancedHeadline as a class
stories = soup.find_all('h2', class_='css-1qwxefa esl82me0')
print(stories)

# loop through all elements on the page with the class name
# balancedHeadline
for story in stories:
    print(story)


