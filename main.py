import requests
from bs4 import BeautifulSoup
import csv
title = []
price = []
for i in range (1, 51):
    url1 = "http://books.toscrape.com/catalogue/page-"+ str(i)+".html"
    page = requests.get(url1)
    soup = BeautifulSoup(page.content, "html.parser")
    all_title = soup.find_all("h3")
    all_price = soup.find_all('p', class_="price_color")
    for titles_sc in all_title:
            title.append((str(titles_sc.find('a')).split('title=', 1)[1]).split('>', 1)[0])
    for price_sc in all_price:
            price.append(price_sc.string)

header = ['titre du livre', 'prix du livre']
with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header)
    for titre, prix in zip(title, price):
        writer.writerow([titre, prix])