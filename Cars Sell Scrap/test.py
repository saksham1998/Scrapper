from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
# import numpy as np
# import pandas as pd


def getCarTrade():
	print('CarTrade Listed Cars ')
	print('\n')
	print('\n')
	url="https://www.cartrade.com/buy-used-cars/"
	html = urlopen(url)
	soup = BeautifulSoup(html,'html.parser')

	name = []
	for names in soup.find_all(itemprop="url")[1:11]:
		name.append(re.sub(' +', ' ', names.contents[0]))
	print('Name of the cars   ',name)
	print('\n')
	print('\n')	
	price = []
	for prices in soup.find_all(class_="cr_prc")[:10]:
		price.append(prices.contents[2])
	print('Price of the cars   ',price)
	print('\n')
	print('\n')
	fuel=[]
	for fuels in soup.find_all(itemprop="fuelType")[1:11]:
		fuel.append(fuels.string)
	print("Fuel Type of the Cars   ",fuel)
	print('\n')
	print('\n')	
	mileage=[]
	for mileages in soup.find_all(itemprop="mileageFromOdometer")[1:11]:
		mileage.append(mileages.string)
	print('Mileage   ',mileage)
	print('\n')
	print('\n')
	year=[]
	for years in soup.find_all(itemprop="productionDate")[1:11]:
		year.append(years.string)
	print('Year of Bulit   ',year)
	print('\n')
	print('\n')	
getCarTrade()	

def getDroom():
	print('Droom Listed Cars:')
	print('\n')
	print('\n')
	url="https://droom.in/cars"
	html = urlopen(url)
	soup = BeautifulSoup(html,'html.parser')

	name = []
	for names in soup.find_all(class_="heading")[100:110]:
		for link in names.contents[1]:
			name.append(re.sub(' +', ' ', link.string))
	print('Name of the cars   ',name)
	print('\n')
	print('\n')	
	price = []
	for prices in soup.find_all(class_="price")[1:11]:
		if len(prices.contents) >3:
			price.append(re.sub(' +', ' ', prices.contents[4]))
		else:
			price.append(re.sub(' +', ' ', prices.contents[2]))	
	print('Price of the cars   ',price)
	print('\n')
	print('\n')
	fuel=[]
	for fuels in soup.find_all(class_="item")[1:41:4]:
		fuel.append(fuels.contents[3].string)
	print('Fuel Type of the cars   ',fuel)
	print('\n')
	print('\n')
	mileage=[]
	for mileages in soup.find_all(class_="item")[3:41:4]:
		mileage.append(mileages.contents[3].string)
	print('Mileage of the cars   ',mileage)
	print('\n')
	print('\n')
	
getDroom()	