import requests

response = requests.get(url='https://randomuser.me/api?results=10') 

data = response.json()

