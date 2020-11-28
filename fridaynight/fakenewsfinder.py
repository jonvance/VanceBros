import pandas as pd 
import requests
import os
import datetime
from bs4 import BeautifulSoup

# Set times 
year = datetime.datetime.today().strftime('%Y')
month = datetime.datetime.today().strftime('%m')
day = datetime.datetime.today().strftime('%d')

# Create Directory
directory = '../rawdata/{0}{1}{2}/'.format(year,month,day)
if os.path.exists(directory):
	print("Path already exists")
else:
	print("Data will be directed to " + str(directory))
	os.makedirs(directory)