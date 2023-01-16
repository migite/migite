from bs4 import BeautifulSoup
import requests

html = requests.get(r'http://www.supertamade.co.jp/sales/handbill/')
data = BeautifulSoup(html.content, 'html.parser')

PDF_URL = data.find('div', class_='content show').find('div', class_='handbillEntry').find('ul', class_='photoColum').find('li', class_='mgRight30').find('a').get('href')

with open('README_編集用.md', 'r', encoding = 'utf_8') as f:
	s = f.read()

with open('README.md', 'w', encoding = 'utf_8') as f:
	f.write(s.replace(r'＜＜ここが玉出PDFに置換されます＞＞', PDF_URL))