from bs4 import BeautifulSoup
import requests
import pandas as pd
# materiel.net des pc gamers
# url recherche des pc gamers sur materiel.net
url = 'https://www.materiel.net/recherche/pc%20gamer%20portable/+fb-C000000806,C000001041.html'
# get de l'url
response = requests.get(url)
# installation du de lxml
# parser la reponse
soup = BeautifulSoup(response.content, 'lxml')

results = soup.find_all(class_='c-product__title')
prix = soup.find_all(class_='o-product__price')
desc = soup.find_all(class_='c-product__description')

pcgamer = []   # liste de dictionnaires

modele = []      # liste des modèles
description = []  # liste des descriptions
valeur = []    # liste des prix

i = 0
for pc in results:
    newpc = {}
    try:
        euro = prix[i]
        price = euro.text.replace('\xa0', '')
    except:
        price = 'inconnu'
    info = desc[i].text
    # print(f'{pc.text} coûte {price} info : {info}')
    # pour l'affichage
    newpc["Modele"] = pc.text
    newpc["Info"] = info
    newpc["Prix"] = price
    pcgamer.append(newpc)
    # pour la sauvegarde
    modele.append(pc.text)
    description.append(info)
    valeur.append(price)
    i += 1
# fin de la boucle
# dictionnaires des listes pour la sauvegarde en csv

dict = {'Modele': modele, 'Description': description, 'Prix': valeur}
df = pd.DataFrame(dict)
df.to_csv("Materiel.csv", sep=';')


# print(pcgamer)
