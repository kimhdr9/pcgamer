import sqlite3
from Magasins import Magasins
import pandas as pd
# création d'un base de données
conn = sqlite3.connect('Sites.db')
c = conn.cursor()

# création d'une table
# c.execute(''' CREATE TABLE magasins( urls TEXT, titre TEXT, prix TEXT, info TEXT, site TEXT, categorie TEXT ) ''')

# for Mag in Magasins:
#     c.execute(''' INSERT INTO magasins VALUES(?,?,?,?,?,?) ''',
#               (Mag['url'], Mag['ClassTitre'], Mag['ClassPrix'], Mag['ClassDescription'], Mag['site'], Mag['type']))

# conn.commit()

if False:

    c.execute(''' SELECT * FROM magasins ''')

    results = c.fetchall()

    # print(results[0])

    Stores = []

    for row in results:
        Store = {}
        Store['url'] = row[0]
        Store['titre'] = row[1]
        Store['prix'] = row[2]
        Store['info'] = row[3]
        Store['site'] = row[4]
        Store['type'] = row[5]
        Stores.append(Store)

    print(Stores)
else:
    # utilisation de pandas pour afficher le résultat de la requête
    df = pd.read_sql_query("SELECT * FROM magasins", conn)
    print(df)

conn.close()
