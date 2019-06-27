from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import math


def getIndeedRatings(company):
	'''
	function used to scrap ratings from indeed website.
	Require company name as argument
	'''
	url = 'https://www.indeed.co.in/cmp?from=snapshot-cmp-search-header&q={}'.format(company)
	html = urlopen(url)
	soup = BeautifulSoup(html,'html.parser')

	value = soup.find(itemprop='ratingValue').string

	print(value)
	# ratingValue(value)


getIndeedRatings('google')	

def getIndeedReviews(company):
	'''
	function used to scrap reviews from indeed website.
	Require company name as argument
	'''
	url = 'https://www.indeed.co.in/cmp/{}/reviews'.format(company)
	html = urlopen(url)
	soup = BeautifulSoup(html,'html.parser')

	print(soup.find_all(itemprop='reviewBody')[0].string)
	print('\n')
	if soup.find_all(itemprop='reviewBody')[1].string is not None:
		print(soup.find_all(itemprop='reviewBody')[1].string)
		print('\n')
	else:	
		print(soup.find_all(itemprop='reviewBody')[2].string)
	

# getIndeedReviews('decathlon-sports')



def generateIndeedLogo(company):
	url = 'https://www.indeed.co.in/cmp?from=discovery-cmp-search&q={}'.format(company)
	html = urlopen(url)
	soup = BeautifulSoup(html,'html.parser')
	item = str(soup.find_all(itemprop='logo'))
	if item[27]=='/':
		print('No Link is available')
	else:
		print(item[27:len(item)-4])





def getLinkedinEmployees(company):
	url = 'https://in.linkedin.com/company/{}'.format(company)
	html = requests.get(url,headers={'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3',
						'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
						'accept-encoding':'gzip, deflate, sdch, br'})
	soup = BeautifulSoup(html.text,'html.parser')

	print(html)	

# getLinkedinEmployees('adobe')	



def getRatings(rating):
	decimal,whole = math.modf(float(rating))
	whole = int(whole)
	decimal = round(decimal,1)
	if decimal<0.25:
		whole
	elif decimal>=0.25 and decimal<0.75:
		whole += 0.5		
	else:
		whole += 1

	new_decimal,new_whole = math.modf(whole)
	
	if new_decimal==0:		
		print([int(new_whole)])
	else:
		print([int(new_whole),1])	


def getAmbitionReviews(company):
	url = 'https://www.ambitionbox.com/reviews/{}-reviews'.format(company)
	html = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36'})
	soup = BeautifulSoup(html.text,'html.parser')

	print(soup.find_all('p')[17].text)
	print(soup.find_all('p')[18].text)
	

# getAmbitionReviews('makemytrip')	

def getAmbitionRatings(company):
	url = 'https://www.ambitionbox.com/reviews/{}-reviews'.format(company)
	html = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36'})
	soup = BeautifulSoup(html.text,'html.parser')

	print(soup.find_all('span')[0].text)
	# getRatings(soup.find_all('span')[0].text)


getAmbitionRatings('oyo')	
