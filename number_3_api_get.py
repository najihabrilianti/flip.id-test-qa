import requests

url = "https://reqres.in/api/users?page=2"
response = requests.get(url) 

for index in response.json()['data'] :
    print(index)