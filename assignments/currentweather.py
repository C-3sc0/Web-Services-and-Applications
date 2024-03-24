# Using Using the URL: https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m
# Write a program that will print out the current temperature on the console (and only the temperature)
# Look at the documentation (below) and print out the current wind direction (10m) as well.
# https://open-meteo.com/

# Author: Francesco Troja

import requests
import json

def get_data(url):
    response = requests.get(url)
    # proceed with extracting the data if the status code is 200
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        temperature = data['current']['temperature_2m']
        temp_grade = data['current_units']['temperature_2m']
        print (f'The current temperature is {temperature}{temp_grade}')
    else:
        print(f"There is an error with your request.\n The status code is {response.status_code}.\n Please try to enter a new URL.")
        second_url = input("Enter new URL: ")
        get_data(second_url)

url = 'https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m'
get_data(url)

# last task: print out the current wind direction (10m) as well

new_url = 'https://api.open-meteo.com/v1/forecast?latitude=38.132&longitude=13.3356&current=temperature_2m,wind_speed_10m,wind_direction_10m&forecast_days=1'
new_response = requests.get(new_url)
new_data = new_response.json()

wind_direction = new_data['current']['wind_direction_10m']
wind_grade = new_data['current_units']['wind_direction_10m']

print (f'The current wind direction is {wind_direction}{wind_grade}')