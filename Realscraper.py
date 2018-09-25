# python imports
import csv
# external imports
import requests
from bs4 import BeautifulSoup
#get
url = 'http://www.wvustats.com/'
response = requests.get(url)
# print(response)
html = response.content
#print(html)

# parse
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
table = soup.find('tbody', attrs={'class': 'stripe'})
# extract
list_of_rows = []
for row in table.findAll('tr'):
    # print(row.prettify())
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)




# write
# outfile = open('schedule.csv', 'w+')
# writer = csv.writer(outfile)
# writer.writerow(["Sport", "Date"])
