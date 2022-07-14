import requests

url = 'http://localhost:5000/api/summarize'
r = requests.post( url, json = { 'text' : "" })

print(r.json())