import requests
from bs4 import BeautifulSoup
from googlesearch import search
import schedule
import time



def mouser(part_number):
	query = part_number

	for j in search(query, tld="co.in", num=10, stop=10, pause=2):
		b = "mouser"
		if b in j:
			url = j
			print(url)

			page = requests.get(url)
			soup = BeautifulSoup(page.content, 'html.parser')
			print(soup)
			stock1 = soup.find(attrs={'class': "col-xs-3 onOrderQuantity"})
			print('mouser stock is:' + stock1)
			exit()
def digi_key(part_number):
	query = part_number

	for j in search(query, tld="co.in", num=10, stop=10, pause=2):
		b = "digikey"
		if b in j:
			url = j
			print(url)

			page = requests.get(url)
			soup = BeautifulSoup(page.content, 'html.parser')
			print(soup)
			stock2 = soup.find(attrs={'class': "jss190"})
			print('digikey stock is:' + stock2)
			exit()

def main():
	import pandas as pd
	wb = pd.read_excel('mouser.xlsx')

	for i in range(len(wb['part_number'])):
		part_number = wb['part_number'].iloc[i]
		for j in range(len(wb['query'])):
			company = wb['query'].iloc[j]
			if company is 'mouser':
				mouser(part_number)
			else:
				digi_key(part_number)
				mouser(part_number)





if __name__ == "__main__":
	schedule.every(10).minutes.do(main())
	while True:
		schedule.run_pending()
		time.sleep(1)
