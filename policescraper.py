  # python imports
import json
import csv, json, sys
#if you are not using utf-8 files, remove the next line
#sys.setdefaultencoding("UTF-8") #set the encode to utf8
#check if you pass the input file and output file
if sys.argv[1] is not None and sys.argv[2] is not None:
    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]
    #recommended by stackflow.
    inputFile = open(incidents.json) #open json file
    outputFile = open(police.csv, 'w') #load csv file
    data = json.load(incidents.json) #load json content
    inputFile.close() #close the input file
    output = csv.writer(police.csv) #create a csv.write
    output.writerow(data[0].keys())  # header row
    for row in data:
        output.writerow(row.values()) #values row
import csv
import codecs
from datetime import date
from pprint import pprint
from collections import Counter
# external imports
import requests
from bs4 import BeautifulSoup
#project level imports
from secret_settings import geojson_stub, geojson_key
#get
url = 'https://police.wvu.edu/clery-act/crime-log'
response = requests.get(url)
# print(response)
html = response.content
with open(f"data/html/WVUPDLOG_{date.today()}", 'w+') as html_file:
    print(html, file=html_file)
#print(html)

fhtml = codecs.open(f'data/html/WVUPDLOG_{date.today()}', 'r')

# parse
soup = BeautifulSoup(fhtml.read(), 'lxml')
# print(soup.prettify())
incident_months = soup.findAll('div', attrs={'class': 'accordion__panel'})
# extract
incidents = {}
for month in incident_months:
    # print(month.findAll('li', attrs={'class': 'incident'}))
    # print('=' * 80)
    incident_parents = month.findAll('li', attrs={'class': 'incident'})
    for incident in incident_parents:
        #print(incident.findAll('div', attrs={'class': 'log-copy'}))
        #incidents = incident.findAll('div', attrs={'class': 'log-copy'})
        incident_type = incident.find('h4')
        type_text = incident_type.text
        type_list = type_text.split(':')
        incidents[type_list[0]] = {
                "type": type_list[1].strip()
        }

        p_tags = incident.findAll('p')
        for p in p_tags:
            # print(p.text)
            text = p.text.replace('\\n', '').replace('\\', '')
            if ":" in text:
                # p_split = [t.strip() for t in p.text.split(":", maxsplit=1)]
                p_split = text.split(":", maxsplit=1)
                # print(p_split)

                for idx, p in enumerate(p_split):
                    p_split[idx] = p.strip()

                # print(p_split)
                # print('*' * 80)
                incidents[type_list[0]][p_split[0].lower()] = p_split[1]

# pprint(incidents)
for incident_key in incidents.keys():
    incidents[incident_key]['scrape_date'] = f'{date.today()}'
    incidents[incident_key]['occurred_date'] = incidents[incident_key]['occurred'].split(' ')[0]
    incidents[incident_key]['occurred_time'] = incidents[incident_key]['occurred'].split(' ')[1]



# address = "39.6511, -79.9605, MORGANTOWN"
# params = {"address": address, "key": geojson_key}
# api_response = requests.get(geojson_stub,params=params)
# pprint(api_response.json())
# print(len(api_response.json()['results']))


s = '#18-03127'
parts = s.split('-')
incident_no = int(parts[1])
year = parts[0].replace('#', '')


for incident_key in incidents.keys():
    if '.' in incidents[incident_key]['address'] and '-' in incidents[incident_key]['address']:
        incidents[incident_key]['address_type'] = 'approximate'
    else:
        incidents[incident_key]['address_type'] = 'street'

j = json.dumps(incidents, sort_keys=True, indent=4)
with open('data/incidents/incidents.json', 'w+') as f:
    print(j, file=f)


# street_addresses = []
# for incident_key in incidents.keys():
#     if incidents[incident_key]['address_type'] == 'street':
#         street_addresses.append(incidents[incident_key]['address'])
#
# pprint(Counter(street_addresses).most_common(10))


        #if lat and lng:
        #    incident['location_type'] = 'approximate'
    #    else:
        #    incident['location_type'] = 'address'

    #for address_type in address:
        #address[address_type]['street'] = 'approximate'

            # print(p.text.split).replace("\n", ""))
                # print(sentence).replace("\n", ""))



    #    print('*' * 80)
# pprint(incidents)
# pprint(incidents['#18-05292'])
# for key in incidents.keys():
#     if incidents[key]['building'] == 'WVU DADISMAN HALL':
#         if incidents[key]['disposition'] == 'Clear by Arrest':
#             pprint(incidents[key])

#    for cell in row.findAll('td'):
    #    list_of_cells.append(cell.text)

#    print(list_of_cells[:-1])
#     list_of_rows.append(list_of_cells[:-1])
#
#
# write
# outfile = open('li class="incident"')
# writer = csv.writer(outfile)
# writer.writerow(["Date", "#", "Occured ", "Comments", "Building", "Address", "Disposition"]

