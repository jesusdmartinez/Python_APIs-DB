'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(url)
data = response.json()

pprint(data['data'][-1])


# #delete entry # 53
# response = requests.delete(url + "/53")
# print(response.status_code)

