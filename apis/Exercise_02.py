'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(url)

data = response.json()
emails = []

for i in range(len(data['data'])):
    emails.append(data['data'][i]['email'])

print(emails)
len(emails)

