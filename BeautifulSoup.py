from bs4 import BeautifulSoup
import requests

html = requests.get('http://www.python.org')
soup = BeautifulSoup(html.text, 'lxml')
headers = soup.find_all('h2')

print(headers[0].text)

