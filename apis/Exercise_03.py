'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(url)
data = response.json()

pprint(data['data'][-1])

# #Updating a NEW GUY
# body = {
#     "first_name": "New Guy",
#     "last_name": "New Guy",
#     "email": "new@guy.com"
# }
# response = requests.post(url, json=body)
# print(response.status_code)`