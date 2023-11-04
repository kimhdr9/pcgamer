from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.librairiechimere.com/listeliv.php?mots_recherche=Philip+K.+Dick&select_tri_recherche=pertinence&base=paper&page='

# headers pour faire croire que la demande vient d'un navigateur
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

#  fabrique tous les url avec le numéro de page


def get_urls():
    urls = []
    for i in range(1, 9):
        page = str(i)
        urls.append(url+page)
    return urls
#


def parse_data(urls):
    for url in urls:
        r = requests.get(url, headers=headers)
        sp = BeautifulSoup(r.text, 'lxml')
        # les livres sont rangés dans une liste
        livres = sp.find_all('h2', class_="livre_titre")
        for livre in livres:
            titre = livre.text.strip()
            prix = sp.find('span', class_="item_prix").text.strip()
            print(f'le titre est "{titre}" et le prix {prix}')
    return


if __name__ == '__main__':
    start = time.perf_counter()
    urls = get_urls()
    parse_data(urls)
    fin = time.perf_counter() - start
    print(fin)
# temps d'exécution : 11.5626669
