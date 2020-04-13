#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:57:22 2020

@author: trevorjackson
"""


import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://exitrealty.com/sitemap/agents.xml'
outfile = open('all_agents_1.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(["all_agents_1"])

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
links = soup.find_all('loc')

for link in links:
        item_link = link.get_text()
        writer.writerow([item_link])
        print(item_link)
outfile.close()