import requests
from Magasins import Magasins as Mags
from bs4 import BeautifulSoup
import re

url0 = 'https://www.ldlc.com/recherche/pc%20portable%20gamer/'

url = 'https://www.materiel.net/recherche/pc%20gamer%20portable/+fb-C000000806,C000001041.html'

# renvoie le domaine et le protocole de l'url


def baseurl(url):
    base = ''
    elt = url.split('/')
    if len(elt) > 3:
        base = elt[0]+'//'+elt[2]+'/'
    return(base)


# ---------------- test de baseurl sur Ma
if False:
    # test sur les urls de Mags
    for Mag in Mags:
        base = baseurl(Mag['url'])
        print(base)
# -------------------------------------

# ---- on charge l'url
response = requests.get(url)
# installation du de lxml
# parser la reponse
soup = BeautifulSoup(response.content, 'lxml')
link = soup.find_all(class_='c-product__link o-link--reset')
# recherche des liens

# print(pic[1].img['src'])

for elt in link:
    print(elt['href'])
    if elt.a:
        print(elt.a['href'])
