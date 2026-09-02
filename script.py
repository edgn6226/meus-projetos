
import requests
import pprint
nome=str(input("Qual o seu nome? "))
parametro = {
    "name":nome,
    "country_id":"BR"
 }
url = "https://api.agify.io/"
dados=requests.get(url,params=parametro)
dado=dados.json()
print(dados.status_code)
pprint.pprint(dado)