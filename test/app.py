from flask import Flask, redirect, url_for, render_template, request
from bs4 import BeautifulSoup
import requests
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

pcgamer = []

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
    newpc["Modele"] = pc.text
    newpc["Info"] = info
    newpc["Prix"] = price
    pcgamer.append(newpc)
    i += 1

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', pcgamer=pcgamer)


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
