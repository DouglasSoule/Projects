#!usr/local/bin/env python3

# external imports
import requests
# project-level imports
from secret_settings import geojson_stub, geojson_key


def ping_api(address):
    p = {'address': address, 'key': geojson_key}
    # print(requests.get(geojson_stub, params=p))
    return requests.get(geojson_stub, params=p)


def get_geolocation_data(address):
        county = ''
        state_long = ''
        state_short = ''
        country = ''

        response = ping_api(address)
        if response.status_code == 200:
            # print(response.json())

            # addresses are self-reported and human-entered; they will always be
            # a little messy and the API will always miss a few
            try:
                # print(response.json()['results'])
                # print(response.json()['results'][0])
                # print(response.json()['results'][0]['address_components'])
                address_components = response.json()['results'][0]['address_components']

                # the API is maddeningly stingy with lookups -- especially for data
                # that can move index positions. I feel dirty writing a loop here.
                # But Google made me.
                for line in address_components:
                    if line['types'][0] == 'administrative_area_level_2':
                        county = line['long_name']
                    elif line['types'][0] == 'administrative_area_level_1':
                        state_long = line['long_name']
                        state_short = line['short_name']
                    elif line['types'][0] == 'country':
                        country = line['long_name']

                geolocator = {}

                geolocator['clean_address'] = response.json()['results'][0]['formatted_address']
                geolocator['latitude'] = response.json()['results'][0]['geometry']['location']['lat']
                geolocator['longitude'] = response.json()['results'][0]['geometry']['location']['lng']
                geolocator['county'] = county
                geolocator['state_long'] = state_long
                geolocator['state_short'] = state_short
                geolocator['country'] = country

                # print(geolocator)
                return geolocator

            except IndexError:
                return None


def write_output_sentence(geolocator):
    # print(geolocator)
    print(f'Some stuff about where I live: My address is {geolocator["clean_address"][:-5]}, at latitude {geolocator["latitude"]} and longitude {geolocator["longitude"]}, in {geolocator["county"]}, {geolocator["state_long"]}, {geolocator["country"]}.')


def geolocate(address):
    geolocator_data = get_geolocation_data(address)
    if geolocator_data:
        write_output_sentence(geolocator_data)
    else:
        print(geolocator_data)


if __name__ == '__main__':
    address = '284 Prospect St., Morgantown, WV'
    # address = '1284 Prospect St., Morgantown, WV'
    geolocate(address)

if __name__ == '__main__':
    address = '284 Prospect St., Morgantown, WV'
    # address = '1284 Prospect St., Morgantown, WV'
    geolocate(address)
