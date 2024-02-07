"""divタグのintroductionクラス要素の取得"""
from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.python.org')
soup = BeautifulSoup(html.text, 'lxml')

intro = soup.find_all('div', {'class': 'introduction'})
print(intro)