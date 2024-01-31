# pip install openmeteo-requests
# pip install requests-cache retry-requests numpy pandas
# https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m
# &latitude=52.52,48.85&longitude=13.41,2.35
# Düsseldorf 51.22172 6.77616
# &forecast_days=16
# https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&forecast_days=5
# https://api.open-meteo.com/v1/forecast?latitude=51.22172&longitude=6.77616&forecast_days=5
# https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2024-01-15&end_date=2024-01-29&hourly=temperature_2m
# https://archive-api.open-meteo.com/v1/archive?latitude=51.22172&longitude=6.77616&start_date=2019-03-08&end_date=2019-03-08

import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

#location_search = 'location/search/'
#location = 'location/'

# Aufgabe 1.1
#base_url = 'https://wwww.metaweather.com/api/'
#params ={'query': 'berlin'}
# headers = {"Content-Type": 'application/json'}
#response = requests.get(base_url + location_search. params)
#    'https://wwww.metaweather.com/api/location/search/',
#    params=params,
#    headers=headers
#)
#json = result.json()
#print('response json: ', json)
#print('response code: ', response.status_code)
#print('print woeid: ', json[0]['woeid'])

# Aufgabe 1.2

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 51.22172,
	"longitude": 6.77616,
	"hourly": "temperature_2m"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s"),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)

# Aufgabe 1.3

#response_wetter_berlin_march = requests.get(base_url + location + str(woeid) + '2019/3/8')
#print('response_wetter_berlin_march json: ', response_wetter_berlin_march.json())


# Setup the Open-Meteo API client with cache and retry on error

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 51.22172,
	"longitude": 6.77616,
	"start_date": "2019-03-08",
	"end_date": "2019-03-08",
	"hourly": "temperature_2m"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s"),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)
