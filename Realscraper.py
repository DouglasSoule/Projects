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
tables = soup.findAll('tbody')
# print(tables)
scores_table = tables[0]
# print(scores_table)
schedule_table = tables[1]
# print(schedule_table)
# extract
list_of_rows = []
for row in scores_table.findAll('tr'):
    # print(row)
    list_of_cells = []
    # loop through rows
    for cell in row.findAll('td'):
        # print(cell.text)
        list_of_cells.append(cell.text)
    # print(list_of_cells)
    list_of_rows.append(list_of_cells)
# print(list_of_rows)
# for row in list_of_rows:
    # print(row)
ordered_data = []
for data_list in list_of_rows:
    data_set = {}
    data_set['sport'] = data_list[0]
    data_set['date'] = data_list[1]
    data_set['winner'] = data_list[2]
    data_set['loser'] = data_list[4]
    data_set['score'] = f'{data_list[3]}-{data_list[5]}'
    print(data_set)
# for row in table.findAll('tr'):
    # print(row.prettify())
    # list_of_cells = []
    # for cell in row.findAll('td'):
        # list_of_cells.append(cell.text)




# write
# outfile = open('schedule.csv', 'w+')
# writer = csv.writer(outfile)
# writer.writerow(["Sport", "Date"])
