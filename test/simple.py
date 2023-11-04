from flask import Flask, redirect, url_for, render_template, request
# from bs4 import BeautifulSoup
# import requests
from scrappcgamer import PCGamer
from Magasins import Magasins
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


@app.route('/materiel')
@app.route('/')
def home():
    return render_template('index.html', produits=pcgamer[0], site=Magasins[0]['site'], type=Magasins[0]['type'])


@app.route('/infomax')
def infomax():
    return render_template('index.html', produits=pcgamer[1], site=Magasins[1]['site'], type=Magasins[1]['type'])


@app.route('/ldlc')
def ldlc():
    return render_template('index.html', produits=pcgamer[2], site=Magasins[2]['site'], type=Magasins[2]['type'])


@app.route('/ssd/materiel')
def ssdmat():
    return render_template('index.html', produits=pcgamer[3], site=Magasins[3]['site'], type=Magasins[3]['type'])


@app.route('/ssd/ldlc')
def ssdldlc():
    return render_template('index.html', produits=pcgamer[4], site=Magasins[4]['site'], type=Magasins[4]['type'])


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
