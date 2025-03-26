import requests
import json

# chamada a api mockada
url = 'http://localhost/python-training/app-api/data/restaurantes.json'
response = requests.get(url)
# print(response)

# verifica se a resposta foi bem sucedida
if response.status_code == 200:
   dados_json = response.json()
   dados_restaurante = {}
   for item in dados_json:
      nome_do_restaurante = item['Company']
      if nome_do_restaurante not in dados_restaurante:
         dados_restaurante[nome_do_restaurante] = []
      
      dados_restaurante[nome_do_restaurante].append({
         "item": item['Item'],
         "price": item['price'],
         "description": item['description']
      })
   
   print(dados_restaurante['McDonald’s'])
else:
   print(f'O erro foi {response.status_code}')

# cria arquivos json com os resultados obtidos
for nome_do_restaurante, dados in dados_restaurante.items():
   nome_do_arquivo = f'json/{nome_do_restaurante}.json'
   with open(nome_do_arquivo,'w') as arquivo_restaurante:
      json.dump(dados,arquivo_restaurante,indent=4)