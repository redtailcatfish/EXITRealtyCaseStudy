#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:57:05 2020

@author: trevorjackson
"""


import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://exitrealty.com/sitemap/agents.xml'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
soup.find_all('loc')

for data in soup.find_all('loc'):
    print(data.get_text())