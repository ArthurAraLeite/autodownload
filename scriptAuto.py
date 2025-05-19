import requests
from bs4 import BeautifulSoup

#Id do Jogo da Steam
app_id = input('Write gameID: ')

#Id de uma coleção de mods 
colecao_id = input("Write collectionID: ")

url = f'https://steamcommunity.com/sharedfiles/filedetails/?id={colecao_id}'
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

#Encontra todos os <a> com 'href' contendo 'filedetails/?id=',
links = soup.find_all('a', href=lambda href: href and 'filedetails/?id=' in href)

#Extrai os IDs dos hrefs únicos (sem repetições),
ids = sorted(set(link['href'].split('id=')[-1] for link in links))

# Caminho para o arquivo .bat
arquivo_bat = 'baixar_mods.bat'

# Escreve os comandos no arquivo
with open(arquivo_bat, 'w', encoding='utf-8') as f:
    for item_id in ids:
        f.write(f'workshop_download_item {app_id} {item_id}\n')

print(f'Arquivo "{arquivo_bat}" criado com {len(ids)} mods.')