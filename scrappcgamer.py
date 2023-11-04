from bs4 import BeautifulSoup
import requests
# materiel.net des pc gamers
# url recherche des pc gamers sur materiel.net
url = 'https://www.ldlc.com/recherche/pc%20portable%20gamer/'
# get de l'url
ClassTitre = 'title-3'
ClassPrix = 'price'
ClassDesc = 'dec'


def PCGamer(url, ClassTitre, ClassPrix, ClassDesc):
    response = requests.get(url)
    # installation du de lxml
    # parser la reponse
    soup = BeautifulSoup(response.content, 'lxml')

    results = soup.find_all(class_=ClassTitre)
    prix = soup.find_all(class_=ClassPrix)
    desc = soup.find_all(class_=ClassDesc)

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
        # print(f'{pc.text} coûte {price} info : {info}')
        newpc["Modele"] = pc.text
        newpc["Info"] = info
        newpc["Prix"] = price
        pcgamer.append(newpc)
        i += 1
    return(pcgamer)

# pour tester le module


if __name__ == '__main__':
    DictPCGamer = PCGamer(url, ClassTitre, ClassPrix, ClassDesc)
    print(DictPCGamer)
