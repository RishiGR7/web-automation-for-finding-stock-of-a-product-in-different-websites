import requests
from bs4 import BeautifulSoup
from googlesearch import search
import schedule
import time
query = 'CMX100D6'
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    b = "https://octapart.com"
    #print(j)
    if b in j:
        url = j
        print(url)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup)
        stock1 = soup.find(attrs={'class': "col-xs-3 onOrderQuantity"})
        print('mouser stock is:' + stock1)
        exit()