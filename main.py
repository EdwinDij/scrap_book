import requests
from bs4 import BeautifulSoup
for i in range (1, 51):
    url1 = "http://books.toscrape.com/catalogue/page-"+ str(i)+".html"
    print(url1)
    page = requests.get(url1)
    soup = BeautifulSoup(page.content, "html.parser")
    all_title = soup.find_all("h3")
    title = []
    for titles_sc in all_title:
            title.append((str(titles_sc.find('a')).split('title=', 1)[1]).split('>', 1)[0])
            print(title)