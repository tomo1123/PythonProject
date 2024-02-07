"""titleタグの要素の取得"""
from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.python.org')
soup = BeautifulSoup(html.text, 'lxml')
headers = soup.find_all('h2')
print(headers)