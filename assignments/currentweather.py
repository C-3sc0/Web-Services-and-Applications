# Using Using the URL: https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m
# Write a program that will print out the current temperature on the console (and only the temperature)
# Look at the documentation (below) and print out the current wind direction (10m) as well.
# https://open-meteo.com/

# Author: Francesco Troja

import requests
import json

url = 'https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m'
response = requests.get(url)
data = response.json()

#store the API content in a json file
with open ('weather-assignment-topic2.json', 'w') as fp:
    json.dump(data,fp, indent=4)

temperature = data['current']['temperature_2m']
temp_grade = data['current_units']['temperature_2m']

print (f'The current temperature is {temperature}{temp_grade}')

# last task: print out the current wind direction (10m) as well

new_url = 'https://api.open-meteo.com/v1/forecast?latitude=38.132&longitude=13.3356&current=temperature_2m,wind_speed_10m,wind_direction_10m&forecast_days=1'
new_response = requests.get(new_url)
new_data = new_response.json()

#store the API content in a json file
with open ('w-a-extra-taask.json', 'w') as fp:
    json.dump(new_data,fp, indent=4)

wind_direction = new_data['current']['wind_direction_10m']
wind_grade = new_data['current_units']['wind_direction_10m']

print (f'The current wind direction is {wind_direction}{wind_grade}')