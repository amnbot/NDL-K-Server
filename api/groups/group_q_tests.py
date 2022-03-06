import requests

BASE = 'http://127.0.0.1:5000/'

#gender = input()
#type = input()

#response = requests.get(BASE + f'idols/{gender}/{type}')
response = requests.get(BASE + f'groups/boy/allgroups/')

print(response.json())
input()
