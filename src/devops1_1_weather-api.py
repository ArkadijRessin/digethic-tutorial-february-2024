import requests

# GET Requests to https://wwww.metaweather.com/api/location/search/?query=berlin

location_search = 'location/search/'
location = 'location/'

# Aufgabe 1.1
base_url = 'https://wwww.metaweather.com/api/'
params ={'query': 'berlin'}

# headers = {"Content-Type": 'application/json'}

response = requests.get(base_url + location_search. params)
#    'https://wwww.metaweather.com/api/location/search/',
#    params=params,
#    headers=headers
#)

json = result.json()
print('response json: ', json)
print('response code: ', response.status_code)
print('print woeid: ', json[0]['woeid'])

# Aufgabe 1.2

woeid = json[0]['woeid']
response_wetter_berlin = requests.get(base_url + location + woeid)

print('response_wetter_berlin json: ', response_wetter_berlin.json())
print('response_wetter_berlin code: ', response_wetter_berlin.status_code)

# json format
# https://www.geeksforgeeks.org/json-formatting-python/


# https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m
# &latitude=52.52,48.85&longitude=13.41,2.35
# Düsseldorf 51.22172 6.77616
# &forecast_days=16
# https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&forecast_days=5
# https://api.open-meteo.com/v1/forecast?latitude=51.22172&longitude=6.77616&forecast_days=5
# https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2024-01-15&end_date=2024-01-29&hourly=temperature_2m
# https://archive-api.open-meteo.com/v1/archive?latitude=51.22172&longitude=6.77616&start_date=2019-03-08&end_date=2019-03-08

# Aufgabe 1.3

response_wetter_berlin_march = requests.get(base_url + location + str(woeid) + '2019/3/8')
print('response_wetter_berlin_march json: ', response_wetter_berlin_march.json())
