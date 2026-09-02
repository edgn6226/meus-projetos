import pprint
from sqlite3.dbapi2 import Date

import requests
parametro={
    "format":"json",
    "qterm":"Brazil",
    "fl":"docdt,count",


}
URL  ="https://search.worldbank.org/api/v3/wds?"
dados = requests.get(URL, params=parametro)
data = dados.json()
print(dados.status_code)
if data["total"] > 0:
    print(data["total"])
    pprint.pprint(data)
else:
    print("Nenhum encontrado")