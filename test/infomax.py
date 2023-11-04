from bs4 import BeautifulSoup
import requests
# materiel.net des pc gamers
# url recherche des pc gamers sur materiel.net
url = 'https://infomaxparis.com/fr/101-pc-portable-gamer'
# get de l'url
response = requests.get(url)
# installation du de lxml
# parser la reponse
soup = BeautifulSoup(response.content, 'lxml')

# print(response.content)

results = soup.find_all(class_='product-name')
prix = soup.find_all(class_='price')
desc = soup.find_all(class_='product-description-short')

pcgamer = []

i = 0
for pc in results:
    newpc = {}
    # prix
    try:
        euro = prix[i]
        price = euro.text.replace('\xa0', '')
    except:
        price = 'inconnu'
    # description
    try:
        info = desc[i].text
    except:
        info = 'inconnu'
    # impression à l'écran
    print(f'{pc.text} coûte {price} info : {info}')
    newpc["Modele"] = pc.text
    newpc["Info"] = info
    newpc["Prix"] = price
    pcgamer.append(newpc)
    i += 1

# print(pcgamer)
