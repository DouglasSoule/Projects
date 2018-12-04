# python imports
import csv
from datetime import date
from pprint import pprint
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
#print(html)

# parse
soup = BeautifulSoup(html, 'lxml')
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
            if ":" in p.text:
                # p_split = [t.strip() for t in p.text.split(":", maxsplit=1)]
                p_split = p.text.split(":", maxsplit=1)
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





address = "39.6511, -79.9605, MORGANTOWN"
params = {"address": address, "key": geojson_key}
api_response = requests.get(geojson_stub,params=params)
pprint(api_response.json())
print(len(api_response.json()['results']))




#for incident_key in incidents.keys():
    #if '.' in incidents[incident_key]['address'] and '-' in incidents[incident_key]['address']:
        #print(incidents[incident_key]['address'])
    #    print(incidents[incident_key]['type'])

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
