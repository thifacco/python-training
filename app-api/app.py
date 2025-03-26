import requests

url = 'http://localhost/python-training/app-api/data/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
   dados_json = response.json()
   print(dados_json)
else: 
   print(f'O erro foi {response.status_code}')