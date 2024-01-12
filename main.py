from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://pt.wikipedia.org/wiki/Lista_de_concentra%C3%A7%C3%B5es_urbanas_do_Brasil_por_popula%C3%A7%C3%A3o'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find('table', class_='wikitable sortable')

tableheader = content.find_all('th')

titles = [title.text.strip() for title in tableheader]

df = pd.DataFrame(columns = titles)

dataColumn = content.find_all('tr')

for row in dataColumn[1:]:
    dataRow = row.find_all('td')
    data = [data.text.strip() for data in dataRow]

    length = len(df)
    df.loc[length] = data

print(df)    

df.to_csv('population.csv', index=False)

