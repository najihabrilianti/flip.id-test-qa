import requests

url = "https://reqres.in/api/users"
r = requests.post(url , data = {'Name':'Anggi','Job':'QA'})
print(r)
print(r.json())

