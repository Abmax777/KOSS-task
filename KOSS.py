from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
	try:
		with closing(get(url,stream=True)) as resp:
			if is_good_response(resp):
				return resp.content
			else:
				return None

	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None

def is_good_response(resp):
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code==200
		    and content_type is not None
		    and content_type.find('html')>-1 )

def log_error(e):
	print(e)

url=str(input('enter the url from where you wish to scrape'))
#url='https://timesofindia.indiatimes.com/'
raw_html=simple_get(url)
html=BeautifulSoup(raw_html,'html.parser')
#top_story=html.find_all('div',class_="media-heading headingfour")
top_story=html.find_all(('span' or 'div'),class_=("desc" or "media-heading headingfour"))
#items=top_story.find_all('a')
print(top_story)