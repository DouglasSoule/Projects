# python imports
# external imports
import requests
from bs4 import BeautifulSoup
#get
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
response = requests.get(url)
print(response)
html = response.content
#print(html)

# parse
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
table = soup.find('tbody', attrs={'class': 'stripe'})
# extract

# write
