'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

# response = requests.get(url)
# data = response.json()
# pprint(data['data'][-1])

body = {
    "id": 53,
    "first_name": "Old Guy",
    "last_name": "Old Guy",
    "email": "oldguy@yahoo.com"
}

response = requests.put(url, json=body)
pprint(response.status_code)

response = requests.get(url)
data = response.json()

pprint(data['data'][-1])