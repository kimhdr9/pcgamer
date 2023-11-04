from flask import Flask, redirect, url_for, render_template, request
# from bs4 import BeautifulSoup
# import requests
from scrappcgamer import PCGamer
from Magasins import Magasins
import pandas as pd
# évite d'appeller Magasins.Magasins
# materiel.net des pc gamers
# url recherche des pc gamers sur materiel.net

pcgamer = []

for Mag in Magasins:
    pc = PCGamer(Mag['url'], Mag['ClassTitre'],
                 Mag['ClassPrix'], Mag['ClassDescription'])
    pcgamer.append(pc)
# lancement de FlasK
app = Flask(__name__)


@app.route('/produit/<int:id>')
def produit(id):
    if (id < 5):
        return render_template('index.html', produits=pcgamer[id], site=Magasins[id]['site'], type=Magasins[id]['type'], id=id)
    else:
        return render_template('404.html'), 404


@app.route('/')
def home():
    return render_template('index.html', produits=pcgamer[0], site=Magasins[0]['site'], type=Magasins[0]['type'])


@app.route('/download/<int:id>')
def download(id):
    if (id < 5):
        page = str(id)
        url = 'http://127.0.0.1:5000/produit/'+page
        df = pd.read_html(url)
        df[0].to_csv('download.csv', sep=';')
        return redirect('/')
    else:
        return render_template('404.html'), 404


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
