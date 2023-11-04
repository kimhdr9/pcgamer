import pandas as pd

page = 1

url1 = 'http://127.0.0.1:5000/produit/1'


df = pd.read_html(url1)
# 15 first rows
print(df[0].head(15))
# save data in a csv file
df[0].to_csv('download.csv')
