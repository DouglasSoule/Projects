# python imports
import csv
# external imports
import requests
from bs4 import BeautifulSoup
#get
url = 'https://police.wvu.edu/clery-act/crime-log'
response = requests.get(url)
# print(response)
html = response.content
#print(html)

# parse
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
incident_months = soup.findAll('div', attrs={'class': 'accordion__panel'})
# extract
list_of_rows = []
for month in incident_months:
    print(month.findAll('li', attrs={'class': 'incident'}))     
    # print(row.prettify())
    list_of_cells = []
#    for cell in row.findAll('td'):
    #    list_of_cells.append(cell.text)

#    print(list_of_cells[:-1])
#     list_of_rows.append(list_of_cells[:-1])
#
#
# write
# outfile = open('li class="incident"')
# writer = csv.writer(outfile)
# writer.writerow(["Date", "#", "Occured ", "Comments", "Building", "Address", "Disposition"])
