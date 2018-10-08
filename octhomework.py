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


            try:
                # print(response.json()['results'])
                # print(response.json()['results'][0])
                # print(response.json()['results'][0]['address_components'])
                address_components = response.json()['results'][0]['address_components']



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
    print(f'Some stuff about where I do journalism at my favorite place in the world, the DA newsroom: I do journalistic things for the student newspaper at {geolocator["clean_address"][:-5]}, at latitude {geolocator["latitude"]} and longitude {geolocator["longitude"]}, in {geolocator["county"]}, {geolocator["state_long"]}, {geolocator["country"]}.')
#This output sentence should connect to the address I am requesting to see, which in this case is the address of the DA.

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
#This is the address of the DA, my favorite place in the world.

def ping_api(address):
    p = {'address': address, 'key': geojson_key}
    # print(requests.get(geojson_stub, params=p))
    return requests.get(geojson_stub, params=p)
#I want the address information of the MIC as well, so I repeat the process that I used to find the longitude and latitude for the DA. All I have to change once I rewrite this is the address itself and the output sentence.)

def get_geolocation_data(address):
        county = ''
        state_long = ''
        state_short = ''
        country = ''

        response = ping_api(address)
        if response.status_code == 200:
            # print(response.json())


            try:
                # print(response.json()['results'])
                # print(response.json()['results'][0])
                # print(response.json()['results'][0]['address_components'])
                address_components = response.json()['results'][0]['address_components']


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
    print(f'Some stuff about where I do journalism for school: The address information for the MIC is {geolocator["clean_address"][:-5]}, at latitude {geolocator["latitude"]} and longitude {geolocator["longitude"]}, in {geolocator["county"]}, {geolocator["state_long"]}, {geolocator["country"]}.')
#Here I'm changing the output sentence so it is different than the one that was for the DA, my favorite place in the world.

def geolocate(address):
    geolocator_data = get_geolocation_data(address)
    if geolocator_data:
        write_output_sentence(geolocator_data)
    else:
        print(geolocator_data)


if __name__ == '__main__':
    address = '62 Morrill Way, Morgantown, WV 26506'
    # address = '62 Morrill Way, Morgantown, WV 26506'
    geolocate(address)
    #Since I want this address to be different from the one that is listed for the DA, my favorite place in the world, I simply change it to the address for MIC, which is the location I'm seeking locational information for. 
