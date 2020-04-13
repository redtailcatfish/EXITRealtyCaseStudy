import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.businessinsider.com/average-home-prices-in-every-state-washington-dc-2019-6'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
soup.find_all('div')

for data in soup.find_all('div'):
    print(data.get_text())
