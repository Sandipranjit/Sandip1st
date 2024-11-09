import requests
import json

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
result = response.json()

#print(json.dumps(result, indent=4))
#print(result)
print(result['value'])
