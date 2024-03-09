# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".

# Author: Francesco Troja

import requests
import json

url_start = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/'
url_end = '/JSON-stat/1.0/en'

def get_all_as_file(dataset):
    with open ('cso.json', 'wt') as fp:
        json.dump(get_all(dataset), fp, indent= 4)

def get_all(dataset):
    url = url_start + dataset + url_end
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve the dataset.")
    


if __name__ == '__main__':
    get_all_as_file('FIQ02')